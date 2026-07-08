student = {
    "name" : "Rajeev",
    "age" : 23,
    "college" : "IIIT Trichy",
    "cgpa" : 9.55
}
print("Name : " ,{student.get("name")})
print("CGPA : " , {student.get("cgpa")})

student["Branch"] = "CSE"
print("Updated keys and their values of the student : " , student.items())

student["cgpa"] = 9.70
print("Updated CGPA : " , {student.get("cgpa")})

student.pop("age")
print("Updated keys and their values of the student : " , student.items())

print("The keys present in the dictionary are : " , student.keys())
print("The values of keys present in the dictionary are : " , student.values())
print("The keys and values(items) present in the dictionary are : " , student.items())

