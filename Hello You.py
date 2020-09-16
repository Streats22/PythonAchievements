while a == True:
    hello = "Hello, mijn name is {owner}. What's yours?"
    print(hello.format(owner = "Guido"))

    time.sleep (1)

    username = input("My name is:")
    print("Goededag " + username, "The date is:")

    time.sleep (1)

    import datetime

    x = datetime.datetime.now()

    print("Todays date is " + x.strftime("%d"), "van " + x.strftime ("%B"))
    while True:
             query = input('Would you like to continue Y/N')
             Fl = query[0].lower()
             if query == '' or not Fl in ['y','n']:
                print('Please enter')
             else:
                break
    if Fl == 'y':
            print("Hoezeeee!")
    if Fl == 'n':
             break
