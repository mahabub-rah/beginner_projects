days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_year(year, month):
  if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
    if month == 2:
        print('29 Days in this month')
    else: 
      print(f"{days[month-1]} Days in this month" )
  else:
    print("Not Leap Year")
    print(f"{days[month-1]} days in this month")
    


leap_year(int(input('Write a year: ')), int(input('Write a Month: ')))