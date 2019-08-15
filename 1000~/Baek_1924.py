week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mon_day = list(map(int, input().split()))

a = 0
mon = 0

for i in range(mon_day[0] - 1):
    mon += month[i]

cal = mon + mon_day[1]
cal = cal % 7 - 1
print(week[cal])

