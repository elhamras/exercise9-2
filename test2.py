mostafalist = []

while True:
    data = input('Enter numbers (for finish type a)')
    if data == 'a':
        break
    mostafalist = mostafalist + [data]

print(mostafalist)

#odd_nos = list(filter(lambda x: (x % 2 != 0), mostafalist))
#print("Odd numbers in the list: ", odd_nos)



#only_odd = (data for data in mostafalist if data %2 == 1)
#print(only_odd)

evenlist = []
oddlist = []
for data in range(len(mostafalist)):
    if int(mostafalist[data]) % 2 == 0:
        evenlist.append(mostafalist[data])
    else:
        oddlist.append(mostafalist[data])

print(evenlist)
print(oddlist)