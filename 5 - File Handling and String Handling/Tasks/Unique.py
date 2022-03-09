import datetime

today = datetime.date.today()
username = "idivina"

myFile = open(f"{today}-{username}.txt", "a")
myFile.close()