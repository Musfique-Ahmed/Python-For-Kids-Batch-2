# try:
#     x = int(input("Enter the 1st num: "))
#     y = int(input("Enter the 2nd num: "))


#     result = x / y

# except ValueError:
#     print(f"Please enter a valid input!")

# except ZeroDivisionError:
#     print(f"Can't devided by ZERO!")

# finally:
#     print(result)
#     print("Program finished!")



while True:
    try:
        n = int(input("Enter a number: "))
        if n == 404:
            break
        print(f"You entered: {n}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")