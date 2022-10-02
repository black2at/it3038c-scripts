import datetime

bday = input("Please enter your DOB in MM/DD/YYYY format")
secbday = datetime.datetime.strptime(bday, '%m/%d/%Y')
date = datetime.datetime.today()
age= (date - secbday).total_seconds()
print("You are ",age," seconds old")
