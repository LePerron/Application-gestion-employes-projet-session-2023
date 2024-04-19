import datetime

date = "01/04/2024"

date_formatee = datetime.datetime.strptime(date, "%d/%m/%Y")
if date_formatee <= datetime.datetime.now():
    print("yea")