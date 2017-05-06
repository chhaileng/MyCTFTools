from datetime import date, timedelta as td

d1 = date(1993, 6, 1)
d2 = date(1994, 12, 31)
delta = d2 - d1
fw = open("DateList.txt", "w")

for i in range(delta.days + 1):
    DATE = d1 + td(days=i)

    day = '' + str(DATE.day)
    month = '' + str(DATE.month)
    year = '' + str(DATE.year)

    if len(day)==1:
        day = '0' + day
    if len(month)==1:
        month = '0' + month

    dString = day + '/' + month + '/' + year
    print dString
    fw.write(dString + '\n')

fw.close()
