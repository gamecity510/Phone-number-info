from phonenumbers import parse
from phonenumbers import geocoder
from phonenumbers import carrier
number = input('target phone number:  ')
number = parse(number)
print(geocoder.description_for_number(number,"en"))
print(carrier.name_for_number(number,"en"))

