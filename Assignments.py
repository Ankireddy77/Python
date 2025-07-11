a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))


a, b = b, a

print(a)
print(b)

#############################################################

year = int(input("Enter a year: "))

# Check for leap year
if (year % 4 == 0) and (year % 100 != 0) :
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
