from datetime import datetime

future = input("Enter a future date (YYYY-MM-DD): ")
future_date = datetime.strptime(future, "%Y-%m-%d")
today = datetime.today()
days_left = (future_date - today).days
print("Days left:", days_left)
