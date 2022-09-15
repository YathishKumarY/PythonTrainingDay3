import cal

bs = int(input("Enter the basic salary: "))
print("Your HRA is {0}".format(cal.hra(bs)))
print("Your DA is {0}".format(cal.da(bs)))
print("Your Bonus is {0}".format(cal.bonus(bs)))

