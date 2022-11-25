n = int(input()) 
temps = [int(i) for i in input().split()]

for x in temps:
    if x<0 and abs(x) in temps:
        temps.remove(x)

if temps == []:
    print(0)
else:
    print(min(temps, key=lambda x:abs(x-0)))
