from icalendar import Calendar, Event
from uuid import uuid1
cal = Calendar()
default_time = ("2018年4月12日16点30分" + "公历")
cal.add(name='gongzuo' ,value='123123')
cal.add(name='gongzuo' ,value='13443')
print(cal)