import calendar, locale
from datetime import date
for i in range(1, 13):
    locale.setlocale(locale.LC_ALL, 'ru')
    if calendar.monthcalendar(2024, i)[2][3] < 15:
        thu = calendar.monthcalendar(2024, i)[3][3]
    else:
        thu = calendar.monthcalendar(2024, i)[2][3]
    mydate = date(2024, i, thu)
    print(mydate.strftime('%A %d %B %Y'))