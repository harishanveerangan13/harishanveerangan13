import datetime
from datetime import date
import pytz

tday = datetime.date.today()

tdelta = datetime.timedelta(hours=7) #value of 7 days from current time

# # print(tday + tdelta)
#
# bday = datetime.date(2022, 5, 13)
#
# tillbday = bday - tday
#
# print(tillbday.total_seconds())
#
# d = datetime.time(9, 30, 45, 100000)
# print(d.hour)
# print(d.minute)
# print(d.second)
# print(d.microsecond)
# t = datetime.datetime(2008, 2, 14, 3, 34, 35, 100000) #put hours, minutes, seconds, microseconds, days, month, year altogether
# #
# print(t.month)
#
# bruh = t + tdelta
#
# print(bruh)


# dt = datetime.datetime.today()
# dtnow = datetime.datetime.now()
# dtutc = datetime.datetime.utcnow()
#
#
# print(dt,"\n", dtnow,"\n", dtutc)
#
# dt = datetime.datetime(2021, 12, 18, 3, 43, 43, tzinfo= pytz.UTC)
# print(dt)

bruh = datetime.datetime