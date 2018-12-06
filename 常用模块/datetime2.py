from datetime import  datetime,timedelta,timezone

# now = datetime.now()
# print(now)
#
# stamp = now.timestamp()
# print(stamp)
#
# now1 = datetime.utcfromtimestamp(stamp)
# print(now1)

# 将now1 时间对象 转换成 str
# Str_time = now1.strftime('%F %T')
# print(Str_time)
#
# # 加减时间
# print(now)
# print(now - timedelta(hours=10,days=1,minutes=50,seconds=42))
# # 创建时区
# tz_utc_8 = timezone(timedelta(hours=8))
# dt = now.replace(tzinfo=tz_utc_8)
# print(now)
default_utc_dt = datetime.now(tz=timezone.utc)  # 生成一个datetime类实例，传入默认时区类timezone.utc
print(default_utc_dt)
bj_timezone = timezone(timedelta(hours=8))  # 生成北京时区类实例
bj_utc_dt = default_utc_dt.astimezone(tz=bj_timezone)  # 北京datetime类实例时区指定为bj_timezone
print(bj_utc_dt)  # 





