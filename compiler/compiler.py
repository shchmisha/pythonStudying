import copy
import imp
import re

# tokens will be dicts
# type and value of token is included

# tokens will then form expressions
# expressions will be dicts, which hold the name of the function

def tokenizer(input_expression):
    current = 0
    tokens = []
    alphabet = re.compile(r"[a-z]", re.I)
    numbers = re.compile(r"[0-9]")
    whitespace = re.compile(r"\s")

    while current < len(input_expression):
        char = input_expression[current]
        if re.match(whitespace, char):
            current = current + 1
            continue
        if char == '(':
            tokens.append({
                'type': 'left_paren',
                'value': '('
            })
            current = current + 1
            continue
        if char == ')':
            tokens.append({
                'type': 'right_paren',
                'value': ')'
            })
            current = current + 1
            continue
        if re.match(numbers, char):
            value = ''
            while re.match(numbers, char):
                value += char
                current = current + 1
                char = input_expression[current]
            tokens.append({
                'type': 'number',
                'value': value
            })
        if re.match(alphabet, char):
            value = ''
            while re.match(alphabet, char):
                value += char
                current = current + 1
                char = input_expression[current]
            tokens.append({
                'type': 'name',
                'value': value
            })
            continue
        raise ValueError("unknown character: " + char)
    return tokens

def parser(tokens):
    global current  
    current = 0
    def walk():
        global current
        token = tokens[current]
        if token.get("type") == 'number':
            current = current + 1
            return {
                'type': 'NumberLiteral',
                'value': token.get('value')
            }
        if token.get("type") == 'left_paren':
            current = current + 1
            token = tokens[current]
            node = {
                'type': 'CallExpression',
                'name': token.get('value'),
                'params': []
            }
            current = current + 1
            token = tokens[current]
            while token.get("type") != 'right_paren':
                node["params"].append(walk())
                token = tokens[current]
            current = current + 1
            return node
        raise TypeError(token.get("type"))

    ast = {
        'type': 'Program',
        'body': []
    }

    while current < len(tokens):
        ast['body'].append(walk())
    return ast




def compiler(input_expression):
    tokens = tokenizer(input_expression)
    ast = parser(tokens)
    newAst = transformer(ast)
    output = codeGenerator(newAst)