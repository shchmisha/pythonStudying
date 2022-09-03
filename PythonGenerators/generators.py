range(100)
list(range(100))

def make_list(num):
    res = []
    for i in range(num):
        res.append(i*2)
    return res

# range() is not held in memory
