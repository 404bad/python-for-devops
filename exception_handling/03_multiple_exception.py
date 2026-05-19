try:
    number =  int(input("Enter number: "))
    result =  10 / number

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except:
    print("Something's wrong.")
else:
    print(result)
finally:
    print("Program done")
