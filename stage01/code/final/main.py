from gradebook import GradeBook
grade_system=GradeBook()
while True:
    print("grade book menu:")
    print("1.view all students")
    print("2.add student")
    print("3.find student")
    print("4.save and exit")
    print("5.delete student")
    print("6.show stats")
    choice=input("enter your choice(1-6):")
    if choice not in ["1","2","3","4","5","6"]:
        print("invalid choice.please enter a number between 1 and 6.")
        continue
    elif choice=="1":
        grade_system.show_all_students()
    elif choice=="2":
        try:
            name=input("enter student name:")
            grade=float(input("enter student grade:"))
            grade_system.add_student(name,grade)            
            grade_system.log("ADD",f"{name}:{grade}")
        except ValueError:
            print("invalid grade,please enter a valid number.")
    elif choice=="3":
        student_found=grade_system.find(input("enter student name:"))
        if student_found is not None:
            print(f"name:{student_found.name},grade:{student_found.grade}")
        else:
            print(f"student not found.")
    elif choice=="4":
        grade_system.save_and_exit()   
        print("grade book saved.exiting.")
        grade_system.log("SAVE",f"total headcount:{len(grade_system.grade_book)}")
        break
    elif choice=="5":
        name=input("enter the student name:")
        grade_system.remove_student(name)
    elif choice=="6":
        grade_system.show_stats()