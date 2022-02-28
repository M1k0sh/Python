from datetime import datetime, timedelta

d = datetime.today()

d1 = d - timedelta(days=1) 
print(d1)

print(d)

d3 = d + timedelta(days=1) 
print(d3)
