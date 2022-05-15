from datetime import date

def dayOfWeek(YYYY, MM, DD):
  date1 = date(2022, 4, 23)
  date2 = date(YYYY, MM, DD)
  noOfDays = abs((date2-date1).days)
  if (MM == 1 and DD <= 19) or (MM == 12 and DD >= 22) :
      a = 'Capricorn'
  elif (MM == 1 and DD >= 20) or (MM == 2 and DD <= 18):
      a = 'Aquarius'
  elif (MM == 2 and DD >= 18) or (MM == 3 and DD <= 20):
      a = 'Pisces'
  elif (MM == 3 and DD >= 21) or (MM == 4 and DD <= 19):
      a = 'Aries'
  elif (MM == 4 and DD > 19) or (MM == 5 and DD < 21):
      a = 'Taurus'
  elif (MM == 5 and DD > 20) or (MM == 6 and DD < 22):
      a = 'Gemini'
  elif (MM == 6 and DD > 21) or (MM == 7 and DD < 23):
      a = 'Cancer'
  elif (MM == 7 and DD > 22) or (MM == 8 and DD < 23):
      a = 'Leo'
  elif (MM == 8 and DD > 22) or (MM == 9 and DD < 23):
      a = 'Virgo'
  elif (MM == 9 and DD > 22 ) or (MM == 10 and DD < 24):
      a = 'Libra'
  elif (MM == 10 and DD > 23) or (MM == 11 and DD < 22):
      a = 'Scorpio'
  elif (MM == 11 and DD > 21) or (MM == 12 and DD < 22):
      a = 'Sagittarius'

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
  print(f'The date you have provided is a {day} and Zodiac sign is {a}')

dayOfWeek(2002, 6, 13)