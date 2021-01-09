import random

# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]
print(random_list)

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)

numbers_b = [random.randint(1, 1001) for i in range(12)]

print(numbers_b)

from decimal import Decimal

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)


from datetime import datetime
birthday = datetime(1952, 10, 1, 12, 00, 00)

print(birthday.year)
#1952

print(birthday.month)
#10
print(birthday.weekday())
#4

datetime.now()
#datetime.datetime(2021, 1, 9, 14, 6, 44, 407479)

datetime.now()
#datetime.datetime(2021, 1, 9, 14, 6, 54, 453673)

datetime.now()
#datetime.datetime(2021, 1, 9, 14, 6, 57, 386692)

datetime.now() - datetime(2020, 1, 1)
#datetime.timedelta(days=374, seconds=50871, microseconds=395863)

parsed_date = datetime.strptime('Oct 1, 1952', '%b %d, %Y')
parsed_date

#datetime.datetime(1952, 10, 1, 0, 0)
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
date_string
#'Jan 09, 2021'