import codecs
from icalendar import Calendar, Event
from uuid import uuid1
school_calendar = codecs.open("school_calendar.ical", mode="a" ,encoding="utf-8")

school_calendar.write("BEGIN:VCALENDAR #日历开始\nPRODID:-//Google Inc//Google Calendar 70.9054//EN #软件信息\nVERSION:2.0 #遵循的 iCalendar 版本号\nCALSCALE:GREGORIAN #历法：公历\nMETHOD:PUBLISH #方法：公开 也可以是 REQUEST 等用于日历间的信息沟通方法\nX-WR-CALNAME:课程表\nX-WR-TIMEZONE:Asia/Shanghai #通用扩展属性，表示时区\n")
