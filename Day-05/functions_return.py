# def cube(number):
#     return number*number*number
# print("Cube of number 3 is: ",cube(3))
# print("Cube of number 5 is: ",cube(5))
# print("Cube of number 10 is: ",cube(10))

# def full_name(first,last):
#     return first+" "+last
# print(full_name("Rajeev","Keshetty"))

# def rectangle(length,breadth):
#     return length*breadth
# print("Area of rectangle with length 3 and breadth 5 is: ",rectangle(3,5))

def power(number, p = 2):
    return number**p
print(f"{power(5)}")
print(f"{power(5,3)}")

def introduce(name,college = "IIIT Trichy"):
    print("Name of the student: ",name)
    print("Name of college: ",college)
introduce("Rajeev")
introduce("Rajeev","GNITC")

def average(*marks):
    if len(marks) == 0:
        return 0

    total = 0
    for mark in marks:
        total += mark

    return total / len(marks)
student_average = average(20,25,24,21,22)
print(student_average)

