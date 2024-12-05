# create a class of student that takes name and marks of 3 subject as argument in constructor
#then create a method to print thr avg of subjects


class student:
    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        print("adding details to school database ............")
        print(f"name of student is : {name}")
        print(f"marks of subject 1 is : {marks1}")
        print(f"marks of subject 2 is : {marks2}")
        print(f"marks of subject 3 is : {marks3}")

    def avg_of_subject(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        return print(f"the average marks  of three subject is :{avg}")

print("******* WELCOME TO ABC SCHOOL OF CODING *******")

student_name = input("please enter the name of student : ")
marks_one = int(input(" enter the marks of subject one : "))
marks_two = int(input(" enter the marks of subject two : "))
marks_three = int(input(" enter the marks of subject three : "))


student1 = student(student_name, marks_one, marks_two, marks_three)
student1.avg_of_subject()
