try:
    age=int(input("Enter a age:"))
    income=20000
    risk = income/age
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Please don't divide by zero")
