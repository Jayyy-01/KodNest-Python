try:
    # num1 = 10
    # num2 = 0
    # res = num1 // num2

    lst = [1,2,3]
    print(lst[5])

    a = int(input("Enter a number: "))
    print(f"You entered {a}")

except ZeroDivisionError:
    print("Cannot divide by Zero")
except IndexError:
    print("Index out of range")
except Exception:
    print("Invalid Input")

finally:
    print("Execution completed")