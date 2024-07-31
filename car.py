command=""
has_car_started= False
while command != "quit":
    command= input(" >").lower()
    if command == "start":
        if has_car_started:
            print("Car is already started")
        else:
            has_car_started=True
            print("Car started")
    elif command == "stop":
        if not has_car_started:
            print("Car is already stopped")
        else:
            has_car_started= False
            print("Car stopped")
    elif command  == "help":
        print("""
         start to start
         stop to stop
         quit to quit the app
        """)
    elif command == "quit":
        break
    else:
         print("Sorry I don't understand")