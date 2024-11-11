number = int(input('number?'))


year = number // 375

month = (number % 375) // 30

week = ((number % 375) % 30) // 7

day = (((number % 375) % 30) % 7)

print(f'{year} years and {month} months and {week} weeks and {day} days')

#or

year = number // 375
remaining_of_year = number % 375
month = remaining_of_year // 30
remaining_of_month = remaining_of_year % 30
week = remaining_of_month// 7
remaining_of_week = remaining_of_month % 7
day = remaining_of_week % 7

print(f'{year} years and {month} months and {week} weeks and {day} days')
