seasons  = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter a month (1-12): "))

if month in [12,1,2]:
    seasons = seasons[0]
elif month in [3,4,5]:
    seasons = seasons[1]
elif month in [6,7,8]:
    seasons = seasons[2]
elif month in [9,10,11]:
    seasons = seasons[3]
else:
    print("Invalid month entered")

print(f"The seasons is: {seasons}")