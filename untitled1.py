a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Division =", a / b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Remainder =", a % b)
n = int(input("Enter a number: "))

print(n % 2 == 0)
age = int(input("Enter age: "))

print(age >= 18)
languages = ["Python", "Java", "C", "C++", "JavaScript"]

language = input("Enter a language: ")

print(language in languages)
age = int(input("Enter age: "))
percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance: "))

print(age >= 18 and percentage >= 60 and attendance >= 75)
n = int(input("Enter a number: "))

print("Positive and Even:", n > 0 and n % 2 == 0)
print("Positive and Odd:", n > 0 and n % 2 != 0)
print("Negative and Even:", n < 0 and n % 2 == 0)
print("Negative and Odd:", n < 0 and n % 2 != 0)
print("Zero:", n == 0)
amount = float(input("Enter purchase amount: "))
member = input("Premium member? yes/no: ")

print(amount >= 5000 or member == "yes")
n = int(input("Enter a three-digit number: "))

print("Hundreds digit =", n // 100)
print("Tens digit =", (n // 10) % 10)
print("Units digit =", n % 10)
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print("(a + b) * c =", (a + b) * c)
print("a + b * c =", a + b * c)

age = int(input("Enter age: "))
cgpa = float(input("Enter CGPA: "))
arrears = int(input("Enter arrears: "))
attendance = float(input("Enter attendance: "))

skills = ["Python", "Java", "C", "C++"]
skill = input("Enter required skill: ")

eligible = age >= 18 and cgpa >= 7.0 and arrears == 0 and attendance >= 75 and skill in skills

print(eligible)
balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))
card = input("Card status: ")
pin = input("PIN status: ")

eligible = card == "active" and pin == "correct" and amount > 0 and amount <= balance

print(eligible)
n = int(input("Enter a number: "))

print("Divisible by both 3 and 5:", n % 3 == 0 and n % 5 == 0)
print("Divisible by 3 but not 5:", n % 3 == 0 and n % 5 != 0)
print("Divisible by 5 but not 3:", n % 5 == 0 and n % 3 != 0)
print("Divisible by neither:", n % 3 != 0 and n % 5 != 0)
basic = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus: "))
deductions = float(input("Enter deductions: "))
tax_percent = float(input("Enter tax percentage: "))

gross = basic + bonus
tax = gross * tax_percent / 100
final_salary = gross - deductions - tax

print("Gross Salary =", gross)
print("Tax Amount =", tax)
print("Final Salary =", final_salary)
username = input("Enter username: ")
password = input("Enter password: ")
status = input("Enter account status: ")
role = input("Enter role: ")

registered_username = "admin"
registered_password = "1234"

roles = ["admin", "manager"]

login = username == registered_username and password == registered_password and status == "active" and role in roles

print(login)
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount percentage: "))
gst = float(input("Enter GST percentage: "))
membership = input("Enter membership status: ")

total = price * quantity
discount_amount = total * discount / 100
pre_gst = total - discount_amount

if membership == "premium" or pre_gst > 5000:
    discount_amount = discount_amount + total * 5 / 100

pre_gst = total - discount_amount
gst_amount = pre_gst * gst / 100
final_bill = pre_gst + gst_amount

print("Total Product Cost =", total)
print("Discount Amount =", discount_amount)
print("Price After Discount =", pre_gst)
print("GST Amount =", gst_amount)
print("Final Bill =", final_bill)
total_seconds = int(input("Enter total seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)
A = input("Enter A (True/False): ") == "True"
B = input("Enter B (True/False): ") == "True"
C = input("Enter C (True/False): ") == "True"
D = input("Enter D (True/False): ") == "True"
E = input("Enter E (True/False): ") == "True"

result = (A and B) or (C and not D and not E)

print(result)
list1 = [10, 20, 30]
list2 = [10, 20, 30]

list3 = list1

print("list1 == list2:", list1 == list2)
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list2:", list1 is not list2)
name = input("Enter student name: ")
age = int(input("Enter age: "))
cgpa = float(input("Enter CGPA: "))
attendance = float(input("Enter attendance: "))
arrears = int(input("Enter number of arrears: "))
language = input("Enter programming language: ")
coding = int(input("Enter coding score: "))
communication = int(input("Enter communication score: "))

skills = ["Python", "Java", "C", "C++"]

eligible = age >= 18 and cgpa >= 7.0 and attendance >= 75 and arrears == 0 and language in skills and coding >= 60 and communication >= 50

print("Student Name =", name)
print("Placement Eligibility =", eligible)

print("High Technical Potential:", coding >= 85)
print("Eligible:", coding >= 60 and coding <= 84)
print("Needs Improvement:", coding < 60)