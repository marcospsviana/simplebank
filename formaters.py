def currency_formater(val):
    return f"$ {val:.2f}"

def date_formater():
    date_time = dt.today()
    return f"{date_time.month}/{date_time.day}/{date_time.year} {date_time.hour}:{date_time.minute}:{date_time.second}"