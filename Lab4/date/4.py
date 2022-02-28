from datetime import datetime, timedelta

d = datetime.today()

d1 = d - timedelta(days=9) 

timedelta = d - d1
x = timedelta.days * 86400 + timedelta.seconds

print(x)