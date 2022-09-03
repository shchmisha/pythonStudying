num_days = int(input("how many days: "))
total = 0
temp = []
for i in range(num_days):
    day  =  int(input('what temp for day' + str(i+1) + ': '))
    temp.append(day)
    total+= temp[i]


avg = total/num_days
print(avg)

above = 0
for i in temp:
    if i > avg:
        above+=1

print(above)