# 直接导入datetime模块内的datetime类
from datetime import datetime
#
# now = datetime.now()
# print(now)

# 导入datetime模块
#import datetime
now = datetime.now()
print(now)
# 指定时间，并转换成时间格式
point_date = datetime(2018,12,5,12,22,22)
print(point_date)
print(type(point_date))

# 将datetime类转换成时间戳
Time_stamp = point_date.timestamp()
print(Time_stamp)
print(now.timestamp()) # 小数点后为毫秒，之前的为整数秒

print(datetime.fromtimestamp(Time_stamp))

# 我们北京时区为 Utc+ 8:00 时间戳转换时区为utc+0:00
print(datetime.utcfromtimestamp(Time_stamp))




#将字符串转换成时间

cday = datetime.strptime('2018-12-05 18:00:00','%Y-%m-%d %H:%M:%S')
print(cday)

