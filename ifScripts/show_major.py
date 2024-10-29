
student_name = "Harvy Eliott"
student_major = "ENG"
if student_major == "BILO":
 major_name = "Biology"
 Department_Office= "Science Bldg,Room 310 "
elif student_major == "CSCI":
 major_name= "Computer Science"
 Department_Office= "Sheppard Hall, Room 314"
elif student_major == "ENG":
 major_name= "English"
 Department_Office= "Kerr Hall, Room 310"
elif student_major == "HIST":
 major_name= "History"
 Department_Office= "Kerr Hall Room 114"
elif student_major== "MKT":
 major_name= "Marketing"
 Department_Office= "Westly Hall, Room 114"
elif student_major == "ART":
 major_name = "Fine Arts"
 Department_Office = "Arts Hall, Room 188" 
else:
 major_name= "Unknown"
 Department_Office= "Office not found" 
print(student_name)
print(f"Name Of Major {major_name}") 
print(f"the office is in {Department_Office}")
