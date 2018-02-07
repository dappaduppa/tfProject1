from datetime import datetime

now = datetime.now()

# print(now)
#
# print(now.year, now.month, now.day)
#
# print(now.hour, now.minute, now.second, now.microsecond)


datetime1 = datetime(2018,1,13)
datetime2 = datetime(2018,1,13, 23, 59, 59, 999999)
# delta = datetime2 - datetime1

# print(delta.days, delta.seconds)

str1 = str(datetime1)

str2 = datetime1.strftime('%Y-%m-%d')

print(str2)

str3 = "this is how the world works"