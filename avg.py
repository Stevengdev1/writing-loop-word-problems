# avg.py project
# 11-14-2023
# by Steven D. Garcia

number_list = 0
for i in range(10):
    number = float(input("Please enter 10 real numbers: "))
    number_list += number
print("The average of these numbers is: ", number_list / 10)