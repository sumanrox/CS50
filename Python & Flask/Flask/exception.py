def keyError():
    ages={
        "Alice":23,
        "Bob":25,
        "Sven":23,
        "David":26,
        "Sid":0
    }
    choice = input("[*] Who do you wanna look up to? : ")
    try:
        print(f"{choice} age is {ages[choice]}")
        x= 10/ages[choice]
    except KeyError:
        print(f"There is no one with the name of {choice}")
    except ZeroDivisionError:
        print("Sorry the Age is Zero!")