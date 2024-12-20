print("Welcome to walsal201 Spaceship")
name = input("What is your name? \n")

fleet = "iron, cobalt, manganese, molybdenum, nickel, aluminium, titanium "
print(name + ", Nice to meet you in my Space ship, what resource your are looking for to bring back to earth  from the folowing fleet menu, " + fleet + "\n\n\n" )
order = input()
price = 10000
quantity = input("How many fleet you orderd \n")
total = price * int(quantity)
print("Thank you very much, your resource order cost is:$" + str(total) + ", for ," + order +  "!,Enjoy")
