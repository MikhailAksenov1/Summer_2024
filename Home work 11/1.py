import calendar, locale
from datetime import date
for i in range(1, 13):
    locale.setlocale(locale.LC_ALL, 'ru')
    mydate = date(2024, i, calendar.monthcalendar(2024, i)[2][3])
    print(mydate.strftime('%A %d %B %Y'))