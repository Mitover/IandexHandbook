n = int(input())
m = int(input())
t = int(input())
totalHour = (n + (t + m) // 60) % 24
totalMinute = (m + t) % 60
print(totalHour // 10, totalHour % 10, ":", totalMinute // 10, totalMinute % 10, sep="")
