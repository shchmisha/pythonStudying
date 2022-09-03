# Recursion is a way of solving a problem  by having a function call itself
# - perform the same operation multiple times with different inputs
# - in every step try smaller inputs to make the program smaller
# - Base condition is needed to stop the recursion, otherwise an infinite loop will occur

# Example:
def openRussianDoll(doll):
    if doll == 1:
        print('all dolls are opened')
    else:
        openRussianDoll(doll-1)

# Why do we need recursion
# 1)
# Recursive thinking is really important in programming 
# and it helps you break down big problems into smaller ones and easier to use
# - when to choose recursion?
#   - if you can divide the problem into smimilar sub problems
#   - Design an algorithm to compute nth...
#   - Write code to list the nth...
#   - Implement a code to compute all
#   - Practice
# 2)
# The prominent usage of recursion in data structures like trees and graphs
# 3)
# Recursion is used in many alorithms(divide and conquer, greedy and dynamic programming)

