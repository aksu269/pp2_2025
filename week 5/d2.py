import datetime
x = datetime.datetime.now()
yesterday = datetime.datetime(x.year, x.month, x.day - 1)
tomorrow = datetime.datetime(x.year, x.month, x.day + 1)
print(yesterday.strftime('%x'))
print(x.strftime('%x'))
print(tomorrow.strftime('%x'))