languages = ["Java","Python","C++"]
print(languages[0])
print(languages[1])
print(languages[2])

languages[2] = "JavaScript"
print(languages)
languages.append("React")
print(languages)
languages.insert(2,"SQL")
print(languages)
languages.remove("Java")
print("Updated Languages : " ,languages)
print(len(languages))
languages.sort()
print("Updated Languages : " ,languages)
languages.sort(reverse=True)
print("Updated Languages : " ,languages)

if "Python" in languages:
    print("Python Found")
else:
    print("Not Found")
#Finding min and max
marks = [45,78,91,35,88]
marks.sort()
print(marks[0])
print(marks[-1])

a = [10,20,30]
b = a
b.append(40)
print(a)

m = (1,)
print(type(m))