name = input("What is your name?")
print("Hello , " + name + " let's find out how many full moons you have lived through...")
birthmonth = int(input("What month of the year where you born? Enter only the month number"))
currentmonth = int(input("What is the month of the year today? Enter only month number "))
#print("wow! "  + name! Since your birth there have been  full Moons!)
birthyear = int(input("What year were you born? Write down the four numbers of birthyear "))
number_of_moons = (2019-(birthyear+1))*12 + ((12 - birthmonth)+ (12 - currentmonth))
print(str(number_of_moons)+ " Full Moons!")
