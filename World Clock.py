#!/usr/bin/python3

import datetime
import pytz

print("Select a timezone:")
print("1.Turkey")
print("2.Canada(Eastern)")
print("3.Asia(Hong Kong)")
print("4.England(London)")

choice = input("Enter your choice:")

def dt_time1():
    return datetime.datetime.now(tz=pytz.timezone("Turkey"))

dt_time2 = datetime.datetime.now(tz=pytz.timezone("Canada/Eastern"))
dt_time3 = datetime.datetime.now(tz=pytz.timezone("Asia/Hong_Kong"))
dt_time4 = datetime.datetime.now(tz=pytz.timezone("Europe/London"))

if choice == "1":
    print(dt_time1())
elif choice == "2":
    print(dt_time2)
elif choice == "3":
    print(dt_time3)
elif choice == "4":
    print(dt_time4)
else:
    print("Error")
