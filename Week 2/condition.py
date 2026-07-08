name_list = []
marks_list = []
for i in range(20):
     name = input(f"Enter name for student {i+1}: ")
     marks = int(input(f"Enter marks for {name}: "))
     name_list.append(name)
     marks_list.append(marks)
     name_list.append(name)
     marks_list.append(marks)
     if marks >= 90:
         print("You have scored A+")
     elif marks >=80 and marks <90:
         print("You have scored A")
     elif marks >=70 and marks <80:
         print("You have scored B+")
     elif marks >=60 and marks <70:
         print("You have scored B")
     elif marks >=50 and marks <60:
         print("You have scored C+")
     elif marks >=40 and marks <50:
         print("You have scored C")
     else:
         print("Sorry You have Failed")