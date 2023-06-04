"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

person_age = input("Please enter your age: ")
maximum_rate = 220 - int(person_age)
higher_limit = int(maximum_rate) * .85
lower_limit = int(maximum_rate) * .65
print(f"When you exercise to strenghten your heart, you should keep your heart rate between {lower_limit:.0f} and {higher_limit:.0f} beats per minute")