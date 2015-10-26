__author__ = 'Jan'
check = ""
while True:
    kenteken = input("Kenteken: ")
    if kenteken == "break":
        break
    elif kenteken != check:
        print("Shit gebeurt!")
        check = kenteken
    else:
        print("Skip")

