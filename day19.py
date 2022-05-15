from datetime import date

def dayOfWeek(YYYY, MM, DD):
    date1 = date(2022, 4, 23)
    date2 = date(YYYY, MM, DD)
    noOfDays = abs((date2-date1).days)
    if noOfDays % 7 == 0:
        day = 'Saturday'
    elif noOfDays % 7 == 1:
        if date1 < date2:
            day = 'Sunday'
        else:
            day = 'Friday'
    elif noOfDays % 7 == 2:
        if date1 < date2:
            day = 'Monday'
        else:
            day = 'Thursday'
    elif noOfDays % 7 == 3:
        if date1 < date2:
            day = 'Tuesday'
        else:
            day = 'Wednesday'
    elif noOfDays % 7 == 4:
        if date1 < date2:
            day = 'Wednesday'
        else:
            day = 'Tuesday'
    elif noOfDays % 7 == 5:
        if date1 < date2:
            day = 'Thursday'
        else:
            day = 'Monday'
    elif noOfDays % 7 == 6:
        if date1 < date2:
            day = 'Friday'
        else:
            day = 'Sunday'
    print(f'The date you have provided is a {day}')

dayOfWeek(2002, 6, 13)