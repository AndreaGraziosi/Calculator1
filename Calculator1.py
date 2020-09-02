name = input("What is your name?")
print("Hello , " + name + " let's find out how many full moons you have lived through...")
birthmonth = int(input("What month of the year where you born? Enter only the month number"))
currentmonth = int(input("What is the month of the year today? Enter only month number "))
#print("wow! "  + name! Since your birth there have been  full Moons!)
birthyear = int(input("What year were you born? Write down the four numbers of birthyear "))
number_of_moons = (2019-(birthyear+1))*12 + ((12 - birthmonth)+ (12 - currentmonth))
print(str(number_of_moons)+ " Full Moons!")
#This calculator is called Many Moons. The calculator returns an approximate cnumber of how many full moons (excluding blue moons, the 13th moon certain years experienve) that have risen in a persons life time!
#I used Python 3.7.9 to create Many Moons
# I used the input() so that I could allow for user input
#I wanted to communicate a hello message to the reader so in line 2 I used a Hello message. The message will use the information stored in name, inputed by the user in line 1
# I converted ny numerical inputs from string to int() so that I could use those in a numerical formula
#I stored the result of my formula in the variable number_of_moons so that I could print a concatenated message for the user (converted the value in number_of_moons to a string so that I could add extra text for the message)
