def month_acronym(long_month_name):
#long_month_name = "January"
    datetime_object = datetime.datetime.strptime(long_month_name, "%B")
    month_number = datetime_object.month
    month_number = str(month_number)
    datetime_object = datetime.datetime.strptime(month_number, "%m")
    month_name = datetime_object.strftime("%b")
    return month_name
