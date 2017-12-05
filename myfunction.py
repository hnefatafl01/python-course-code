def minutes_to_hours(seconds, min=70):
    hours = min/60.0 + seconds/3600
    return hours

print(minutes_to_hours(240,10))
print(minutes_to_hours(300))


def currency_converter(rate,euros):
    dollars=euros*rate
    return dollars

print(currency_converter(100,1000))
