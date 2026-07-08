skills = {"Java","Python","Java","React","Python"}
print(skills)

skills.add("SQL")
print("Updated Skill set : ", skills)

skills.remove("React")
print("Updated Skill set : ", skills)

#skills.remove("Angular") : KeyError:'Angular'
skills.discard("Angular") #No Error

frontend = {"HTML","CSS","JavaScript"}
backend =  {"Java" , "SQL" , "JavaScript"}

print("Union of frontend and backend : " ,frontend|backend)
print("Intersection of frontend and backend : " , frontend&backend)
print("Difference of frontend and backend : " , frontend-backend)

