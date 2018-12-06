import re
from datetime import datetime,timezone,timedelta

def to_timestamp(dt_str,tz_str):
    # 将字符串转换为本地dt对象
    default_dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    re_utc = re.match(r'\w{3}([\+|\-])([0-2]?[0-9])\:00$',tz_str)
    Hours = int(re_utc.group(2))
    #定义所在时区
    if re_utc.group(1) == '+':
        new_zone = timezone(timedelta(hours=Hours))
    else:
        new_zone = timezone(timedelta(hours=-Hours))
    #空时区replace为定义所在时区
    new_dt = default_dt.replace(tzinfo=new_zone)
    # 返回时间戳
    return new_dt.timestamp()
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
