a=[]
name=input("Student Name: ")
roll_no=input("Student Roll Number: ")
a.append(name)
a.append(roll_no)
obtained_marks=0
for x  in range(0,7):
    subject=input("Subject: ")
    marks=int(input("Marks: "))
    a.append([subject, marks])
    obtained_marks=obtained_marks+marks
percentage=(obtained_marks/560)*100
a.append(f"{percentage}%")
print("================STUDENT RESULT CARD===============")
print(f"Name: {name}\nRoll No: {roll_no}")
for x in range(2,9):
    print(f"{a[x][0]} : {a[x][1]}")
print(f"Obtained Marks: {obtained_marks}/560")
print(f"Your Percentage Is {percentage}%")

print("------------------THE END----------------------")
