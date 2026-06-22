name=input("Enter name :")
age=int(input("Enter age :"))
rollno=input("enter rollno :")
branch=input("enter branch :")
college=input("enter college name :")

print("\n---------------------------")
print("STUDENT DETAILS")
print("-----------------------------")
print("name :",name)
print("age :",age)
print("Roll Number :",rollno)
print("branch :",branch)
print("college  name :",college)

print("\n----------------------------")
print("SUBJECT MARKS")
print("-----------------------------")
sub1=int(input("enter subject1 marks:"))
sub2=int(input("enter subject2 marks:"))
sub3=int(input("enter subject3 marks:"))
total_marks=sub1+sub2+sub3
average_marks=(total_marks)/3
percentage=(total_marks/300)*100

print("\n-----------------------------")
print("ACADEMIC DETAILS")
print("-----------------------------")
print("total marks:",total_marks)
print("average marks:",average_marks)
print("percentage:",percentage)

print("\n------------------------------")
print("STUDENT RESULT")
print("-----------------------------")
marks=int(input("Enter student marks :"))
if(marks>=90):
    print("GRADE A")
elif(marks>=80):
    print("GRADE B")
elif(marks>=70):
    print("GRADE C")
elif(marks>=60):
    print("GRADE D")
elif(marks>=50):
    print("GRADE E")
else:
    print("FAIL")
