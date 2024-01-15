print("Welcome to the tip calculator");
total_bill = float(input("What was the total bill? $"));
percentage = int(input("What percentage tip would you like to give ? 10, 12 or 15 ? "));
total_people = int(input("How many people to split the bill? "));
# calc = round((total_bill+(total_bill*percentage/100))/total_people, 2);
calc = round((total_bill/total_people)*(1 + percentage/100), 2);
print(f"Each person should pay: {calc}");

