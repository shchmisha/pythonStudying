def prodarr(arr):
    lastprod = 1

    for i in range(len(arr)):
        num = arr[i]
        prod = num * lastprod
        lastprod = prod
         
    return  prod

print(prodarr([1, 2, 3, 10]))
