from datetime import datetime

DATE_FONDATION_ENTREPRISE = datetime.strptime("23/05/2020", "%d/%m/%Y")




###################
date = "01/04/2024"

date_formatee = datetime.datetime.strptime(date, "%d/%m/%Y")
if date_formatee <= datetime.datetime.now():
    print("yea")