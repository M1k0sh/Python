from datetime import datetime, timedelta

d1 = datetime.today()

d2 = d1 - timedelta(days=5) 
print(d2)