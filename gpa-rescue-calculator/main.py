print("Welcome")
first=float(input("enter your first term GPA : "))
if first > 20 or first < 0:
    raise ValueError("Wrong value !")
elif first >= 16:
    print(first, "  verry good.")
elif first >= 10:
    print(first,  "  pass.")
else:
    print(first,  "fail.")


second=float(input("enter your second term GPA : "))
if second > 20 or second < 0:
    raise ValueError("Wrong value !")
elif second >= 16:
    print(second, "  verry good.")
elif second >= 10:
    print(second, "   good")
else:
    print(second, "   fail")

GPA1 = 30 - (first + second)
print(f"you need {GPA1:.2f} to pass")


third=float(input("enter your first term GPA : "))
if third > 20 or third < 0:
    raise ValueError("Wrong value !")
elif third >= 16:
    print(third, "  verry good.")
elif third >= 10:
    print(third,  "  pass.")
else:
    print(third,  "fail.")

GPA2 = (first + second + third)/3

if GPA2 > 9.99:
    print("pass")
else:
    print("fail")

print(f"{GPA2:.2f}")