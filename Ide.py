#conditions
#Ladder if/else

olaShared = 1 
olaMicro = 2
olaMini = 3
olaSedan = 4
olaBike = 5

print("1 -> olaShared")
print("2 -> olaMicro")
print("3 -> olaMini")
print("4 -> olaSedan")
print("5 -> olaBike")
choice = int(input("What cab would you like to ride."))
print("I want to ride {}". format(choice))
print()

if choice == olaShared:
    print("olaShared is booked.Please pay rs. 50")
elif choice == olaMicro:
    print("olaMicro is booked.Please pay rs.100")
elif choice == olaMini:
    print("olaMini is booked.Please pay rs.150")
elif choice == olaSedan:
    print("olaSedan is booked.Please Pay rs. 200")
elif choice == olaBike:
    print("olaBike is booked. Please pay rs.30")
else:
    print("please select valid cab and try again")