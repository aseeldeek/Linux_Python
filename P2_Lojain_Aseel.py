import matplotlib.pyplot as plt
import re
import math
# -----------------------------------------<<  Data Class  >>------------------------------------------------------------
class data:  # should be a Class to asses it using other clasees
    array1 = ['1190587.txt', '1190707.txt','1200928.txt']
    ListCourses = ['ENCS2110', 'ENEE2103', 'ENEE2307', 'ENCS2340', 'ENCS1202', 'ENEE2307', 'ENCS311', 'ENEE2408',
                   'ENCS3320', 'ENCS3340', 'ENEE3309', 'ENCS4101', 'ENCS4110', 'ENEE4104', 'ENCS5200', 'ENCS3390',
                   'ENEE5300', 'ENEE539']
    StudentID = []
    StudentsAvgList = []  # saveing students overall average
    StudentHours = []
# ----------------------------------------<< Admin Class  >>-------------------------------------------------------------
class Admin:
    def __init__(self):
        pass
    # __________________________________________________________________________________________________________________
    #                                    <<  OPTION (1) >>: Add a new record file
    # __________________________________________________________________________________________________________________
    def AppendRecord(self, record):
        for x in range(len(data.array1)):
            # Rise an exection Error that the number is not unique
            if record == data.array1[x]:
                raise Exception("Error: the ID is already exists!")
        data.array1.append(record)
        # create a file for the new record
        f = open(record, "w")
        f.close()
    # __________________________________________________________________________________________________________________
    #                        <<  OPTION (2) >>: Add new semester with student course and grades
    # __________________________________________________________________________________________________________________
    def CreateARecord(self, record):
        seg = []  # list for courses
        f = open(record, "w")
        dash = "-"
        # 1st argument
        year = input("ENTER the year like this (2020-2021) ")
        while (dash not in year):  # if the dash is not included
            print("Wrong formate make sure to add dash (-) between the years")
            year = input("ENTER the year like this (2020-2021) ")

        year = year + "/"  # 2021-2020/
        f.write(year)

        # 2nd argument
        Semester = input("ENTER the 1, 2, 3 for first semester/ second semester/ summer semester: ")
        # when the semester is not intager/ equals 1/ 2/ 3
        while ((Semester.isdigit() == False) | (Semester != '1') & (Semester != '2') & (Semester != '3')):
            print("Wrong formate ! " + Semester)
            Semester = input("ENTER the 1, 2, 3 for first semester/ second semester/ summer semester: ")
        Semester = Semester + " ; "  # 2021-2020/1 ;
        f.write(Semester)

        # 3ed argument
        Count = int(input("Enter number of Courses u want to add: "))
        for z in range(Count):
            Subject = input("Enter the Subject\n")
            # If the course not in the list of courses that the student can study
            while (Subject not in data.ListCourses):
                print("Not allowed!")
                Subject = input("Enter the Subject\n")
            mark = input("Enter your mark in this Course: ")
            # Less than 1 more than 99 not allowed
            while ((int(mark) < 1) | (int(mark) > 99)):
                print("Not allowed!")
                mark = input("Enter your mark in this Course: ")
            seg.append(Subject + " " + mark + ", ")  # 2021-2020/1 ; ENCS210 98, ENEE1112 65

        # Write the courses to the file
        for i in seg:
            f.write(i)
        # Close the file
        f.close()
    # __________________________________________________________________________________________________________________
    #                                <<  OPTION (3) >>: Update a specific record
    # __________________________________________________________________________________________________________________
    def UpdateRecord(self, StudentID):
        StudentExist = 0
        # Searching For the Student
        for index in range(len(data.array1)):  # For loop to search for the student the user entered.
            if data.array1[index] == StudentID:
                StudentExist = 1  # Found, StudentExist updated to --> 1.

        if (StudentExist == 1):  # If student id found
            # Raising an Exception
            try:  # We check if the file of the student id is exists
                with open(StudentID) as f:
                    print("the file of the student " + StudentID + " is found")
            except FileNotFoundError:  # If the file of the student ID not exists
                print("Exception: Sorry, the file " + StudentID + "does not exist.")
                # Raise an exception that the student file does not exists
                raise Exception("the file " + StudentID + " not exists")

            InputCourse = input("Please Enter the Course Name: ")  # Enter course name to update the mark.
            # If the course not in the list of courses that the student can study
            while (InputCourse not in data.ListCourses):
                print("Not allowed course Formate! PLease Try AGAIN!")
                InputCourse = input("Please Enter the Course Name: ")

            ReadFile = open(StudentID, "r")  # Opening the file of student ID
            flag = 0  # Sitting the flag equal to zero
            index = 0  # Sitting index equal to zero
            for line in ReadFile:  # Searching for the Course, loop through the file line by line
                index += 1
                LineNum = index
                if InputCourse in line:  # If the course is (FOUND) in the file
                    content_list = re.split(' ',line)  # Split according to the dynamometer ' ', putting the elements inside the content_list
                    for index in range(len(content_list)):  # Updating the Student Mark
                        if content_list[index] == InputCourse:
                            flag = 1
                            print("---------------------------------------------------")
                            print("The Course " + InputCourse + " is Found Successfully!")
                            print(line)
                            print("---------------------------------------------------")
                            EditedMark = input("Please Enter the new mark: ")  # Input The Edited Mark
                            while ((int(EditedMark) < 1) | (int(EditedMark) > 99)):
                                print("Not allowed!")
                                EditedMark = input("Please Enter the new mark: ")

                            # Updating the Edited Mark
                            # Change the next index of the course name --> MARK
                            content_list[index + 1] = EditedMark + ','  # Adding the ',' to the new mark

                            with open(StudentID, 'r') as fr:
                                lines = fr.readlines()
                                ptr = 1  # Pointer for position
                                with open(StudentID, 'w') as fw:  # Opening in writing mode
                                    for line in lines:  # we want to remove the line
                                        if ptr != LineNum:
                                            fw.write(line)
                                            ptr += 1
                            print("---------------------------------------------------")
                            print("\t\tThe Data is Updated Successfully! ")
                            print("---------------------------------------------------")
                            WriteFile = open(StudentID, "a+")  # Writing the new mark in the student file
                            for element in content_list:
                                WriteFile.write(element + " ")
                            break
            if flag == 0:  # If the flag is still 0, that means the course not found.
                print("--------------------------------------------")
                print("The student did not register this course !!!")
                print("The Course << ", InputCourse, " >> Not Found")
                print("--------------------------------------------")
                # Closing the file
                ReadFile.close()
        else:
            ID = StudentID.replace(".txt", "")  # To remove '.txt' from the student ID
            print("Sorry, We do not  have student with ID --> " + ID)
            # When finishing the loop, and the student is not found or the file not found
            # Then we can not update or edit on the data
    # __________________________________________________________________________________________________________________
    #                                 <<  OPTION (4) >>: Student's Statistics
    # __________________________________________________________________________________________________________________
    def StudentStatis(self, StudentID):
        StudentExist = 0
        ID = StudentID.replace(".txt", "")
        for index in range(len(data.array1)):  # Search for the student
            if data.array1[index] == StudentID:  # If student is found
                StudentExist = 1  # StudentExist updated to 1.

        if (StudentExist == 1):  # if student id found
            # Raising an Exceptionv
            try:  # We check if the file of the student id is exists
                with open(StudentID) as f:
                    print("the file of the student " + StudentID + " is found")
            except FileNotFoundError:  # If the file of the student ID not exists
                print("Exception: Sorry, the file " + StudentID + "does not exist.")
                # Raise an exception that the student file does not exists
                raise Exception("the file " + StudentID + " not exists")

            def PrintCourse(exists, course):
                if exists == False:
                    print(course)

            InputIDList = []
            grades = []
            hoursPerSem = []
            avgPerSem = []
            TakenCourses = []
            with open(StudentID, 'r') as file:
                for line in file:
                    Year_Courses = line.strip().split(
                        ';')  # Split with dynamometer ';',[ 'YEAR/Semester','Courses Marks' ]
                    # Spliting the second digit of the list (Year_Courses) according to the dynamometer ','
                    # to get a list of Course-Mark elements as [ 'Course1 mark1', 'Course2 Mark2' ....etc]
                    Course_Mark = Year_Courses[1].split(",")
                    for i in range(len(Course_Mark)):
                        if Course_Mark[i] == '':
                            Course_Mark.remove(Course_Mark[i])
                    list3 = []  # lists of all the lists
                    for i in range(len(Course_Mark)):
                        z = Course_Mark[i].strip().split(" ")
                        list3.extend(z)
                    for i in range(
                            len(Course_Mark)):  # Will be used to campare the taken courses and the list af all courses
                        z = Course_Mark[i].strip().split(" ")
                        TakenCourses.extend(z)
                    numbers = []
                    courses = []
                    for j in range(len(list3)):
                        if list3[j].isdigit() == True:
                            numbers += [list3[j]]
                        else:
                            courses += [list3[j]]

                    grades.extend(numbers)  # Saving each sudent grades
                    numbers = [int(i) for i in numbers]  # conver a string list to integer list
                    Houres = []
                    for i in range(len(courses)):
                        for j in range(len(courses[i])):
                            # checks if a character is digit or not, if yes -> take the seonced digit and break the loop
                            if (courses[i][j].isdigit() == True):
                                Houres += [courses[i][j + 1]]
                                break
                    # Convert a string list to integer list
                    Houres = [int(i) for i in Houres]
                    sumofHours = sum(Houres)  # Calculating the sum of hours
                    hoursPerSem.append(sumofHours)  # saving each student hours per semester
                    products = [a * b for a, b in zip(Houres, numbers)]  # find the product of 2 lists
                    avg = sum(products) / sumofHours  # find the average
                    avgPerSem.append(format(avg, ".2f"))  # saving each sudent hours per semester

            grades = [int(i) for i in grades]  # Conveting the grades list into integers
            hoursPerSem = [int(i) for i in hoursPerSem]  # Conveting the hoursPerSem list into integers
            SemNUM = 0
            print(
                "-------------------------***<<  Printing Student's Information  >>***------------------------------------")

            # 1. Student's avg per semester.from
            print("****NUMBER 1: Student's avg per semester****")
            for x in range(len(avgPerSem)):
                SemNUM = SemNUM + 1
                print("The Avg for semester " + str(SemNUM) + " :" + avgPerSem[x])
            print("_______________________________")

            # 2.Number of Taken Hours.
            print("****NUMBER 2: The Number of taken hours****")
            print("The number of the taken hours for the studentwith ID << " + ID + " >> :" + str(sum(hoursPerSem)))
            print("_______________________________")

            # 3. Overall Avg -->GPA
            print("***NUMBER 3: The Overall student Average****")
            for i in range(0, len(avgPerSem)):
                avgPerSem[i] = float(avgPerSem[i])
            if(len(avgPerSem)==0):
                studentsAvg=0
            else:
                studentsAvg = sum(avgPerSem) / len(avgPerSem)
            print("The Overall student Avg with ID << " + ID + " >> :", format(studentsAvg, ".2f"))
            print("_______________________________")

            # 4. Remainig Courses
            print("****NUMBER 4:The list of Remaining Courses****")
            for i in data.ListCourses:
                if i in TakenCourses:
                    VALID = True
                else:
                    VALID = False
                PrintCourse(VALID, i)
            print("_______________________________")

        else:
            print("Sorry, We do not  have student with ID --> " + ID)
    # __________________________________________________________________________________________________________________
    #                                    <<  OPTION (5) >>: Global Statistics
    # __________________________________________________________________________________________________________________
    def StudentGlobal(self):  # 4 spaces
        grades = []  # for saving student grades
        hoursPerSem = []
        HoursPerSemAvg = []
        avgPerSem = []
        StudentCount = 0

        for id in range(len(data.array1)):
            with open(data.array1[id], 'r') as file:
                StudentCount += 1  # count number of students
                Sid = data.array1[id].replace(".txt", "");
                data.StudentID.append(Sid)
                for line in file:
                    grade_data = line.strip().split(';')
                    list2 = grade_data[1].split(",")
                    for i in range(len(list2)):
                        if list2[i] == '':
                            list2.remove(list2[i])
                    list3 = []  # lists of all the lists
                    for i in range(len(list2)):
                        z = list2[i].strip().split(" ")
                        list3.extend(z)
                    numbers = []
                    courses = []
                    for j in range(len(list3)):
                        if list3[j].isdigit() == True:
                            numbers += [list3[j]]
                        else:
                            courses += [list3[j]]
                    grades.extend(numbers)  # saving each sudent grades
                    numbers = [int(i) for i in numbers]  # conver a string list to integer list
                    Houres = []
                    for i in range(len(courses)):
                        for j in range(len(courses[i])):
                            if (courses[i][j].isdigit() == True):  # checks if a character in ENCS1237 is digit or not, if yes -> take the seonced digit and break the loop
                                Houres += [courses[i][j + 1]]
                                break
                    Houres = [int(i) for i in Houres]  # Conver a string list to integer list
                    sumofHours = sum(Houres)
                    hoursPerSem.append(sumofHours)  # saving each sudent hours per semester  ( houre list )
                    products = [a * b for a, b in zip(Houres, numbers)]  # find the product of 2 lists
                    avg = sum(products) / sumofHours  # find the average
                    avgPerSem.append(format(avg, ".2f"))  # saving each sudent hours per semester

                hoursPerSem = [int(i) for i in hoursPerSem]  # convert the list to a int list
                if (len(hoursPerSem) ==0):
                    hoursAvgPerSem=0
                else:
                    hoursAvgPerSem = sum(hoursPerSem) / len(hoursPerSem)
                HoursPerSemAvg.append(math.ceil(hoursAvgPerSem))
                data.StudentHours.append(sum(hoursPerSem))
                hoursPerSem.clear()  # cleare the list to save the next student semesters averages

                for i in range(0, len(avgPerSem)):  # convert the list to a float list
                    avgPerSem[i] = float(avgPerSem[i])
                if (len(avgPerSem)==0):
                    studentAvg=0
                else:
                    studentAvg = sum(avgPerSem) / len(avgPerSem)  # find the overall average for each student
                data.StudentsAvgList.append(format(studentAvg, ".2f"))  # save the average
                # cleare the list to save the next student semesters averages
                avgPerSem.clear()
        # Convert the lists from string to integer and the students list to float
        grades = [int(i) for i in grades]
        hoursPerSem = [int(i) for i in hoursPerSem]
        for i in range(0, len(data.StudentsAvgList)):
            data.StudentsAvgList[i] = float(data.StudentsAvgList[i])

        AvgHours = sum(HoursPerSemAvg) / StudentCount
        AvgOverall_students = sum(data.StudentsAvgList) / StudentCount

        print("\n\nOverall students average is:", format(AvgOverall_students, ".2f"), "%")
        print("Student average hours per semester is:", math.ceil(AvgHours), "hours\n\n")
        #  ---> plot syudent grades distribution
        n, m, patche = (plt.hist(grades, bins=10))

        color = ["#F6D860", "#95CD41", "#6E3CBC", "#7267CB", "#B8E4F0", "#F6D860", "#FFF1AF", "#D47AE8", "#FFBC97",
                 "#009DAE"]

        for i in range(len(n)):
            c = color[i]
            patche[i].set_fc(c)

        plt.xlabel("Students Grades per Semester")
        plt.ylabel("Count")
        plt.title("Distribution of students grades")
        plt.show()
    # __________________________________________________________________________________________________________________
    #                                     <<  OPTION (6) >>: Searching: here
    # __________________________________________________________________________________________________________________
    def SearchForanID(self):
        equal = []
        more = []
        less = []
        answer = int(input("Enter 1 to search based on Avarge /  0  to search based on Hours: "))
        if (answer == 1):
            avg = float(input("Enter the wanted average: "))
            for i in range(len(data.StudentsAvgList)):

                if (avg == data.StudentsAvgList[i]):
                    equal.append(data.StudentID[i])
                elif (avg < data.StudentsAvgList[i]):
                    more.append(data.StudentID[i])
                else:
                    less.append(data.StudentID[i])
        elif (answer == 0):
            hours = float(input("Enter the wanted Hours: "))
            for i in range(len(data.StudentHours)):

                if (hours == data.StudentHours[i]):
                    equal.append(data.StudentID[i])
                elif (hours < data.StudentHours[i]):
                    more.append(data.StudentID[i])
                else:
                    less.append(data.StudentID[i])
        else:
            print("Unvalid Answer, try 0 / 1 ")
        print("-------------------------------------------------------")
        print("<< Students's ID equal the entered value     >>")
        for i in range(len(equal)):
            print(" " + str(i + 1) + ". " + (equal[i]))
        print("-------------------------------------------------------")
        print("<< Students's ID more than the entered value >>")
        for i in range(len(more)):
            print(" " + str(i + 1) + ". " + (more[i]))
        print("-------------------------------------------------------")
        print("<< Students's ID less than the entered value >>")
        for i in range(len(less)):
            print(" " + str(i + 1) + ". " + (less[i]))
        print("-------------------------------------------------------\n")

# ------------------------------------------<<  Student Class  >>-------------------------------------------------------------
class Student:

    def __init__(self):
        pass

    def StudentStatis(self, StudentID):

        Admin.StudentStatis(self, StudentID)

    def StudentGlobal(self):
        data.StudentsAvgList.clear()
        data.StudentID.clear()
        data.StudentHours.clear()
        Admin.StudentGlobal(self)

# -------------------------------------------<<      Main     >>-------------------------------------------------------------

def mainFunction():
    print("--------------------------------------------------------------------------\n")
    print("\t > Welcome to Students Records Management System \"SRMS\" < \n")
    print("--------------------------------------------------------------------------\n")
    print("\t > Login to the System as Admin(A)/Student(S)/Exit(E): < \n")
    choice = input(">>> Please enter A for Admin / enter S for student / enter E for Exit > \n")
    # Start the program
    match choice:
        # FIRST CASE
        # --> Admin mood is activated
        case 'A' | 'a':
            while (True):
                print("**************************************************************")
                print("   Welcome to Students Records Management System \"SRMS\"")
                print("**************************************************************\n")
                print("NOTE: --> Please Choise an operation by entering it's number <--  \n")
                print("--------------------<<     Admin List    >>-------------------------- \n")
                print("1. Append new recored file.\n"
                      "2. Create a new recored file.\n"
                      "3. Update a specific record.\n"
                      "4. Find Student statistics.\n"
                      "5. Find Global statistics. \n"
                      "6. Search for a specific record\n"
                      "7. Exit the program\n")
                entered = input("Enter a number from the list: ")
                # -->  this switch case is for admin list
                match (entered):
                    # First case:  Adding recode to the list
                    case '1':
                        Admin1 = Admin()
                        record = input("Enter the Studebt ID number like \"1190587\" : ")
                        while ((record.isdigit() == False) | (len(record) < 7) | (
                                len(record) > 7)):  # checks if the entered number is valid or not
                            print("Please enter only 7 digits! ")
                            record = input("Enter the Student ID number like this \"1190587\" : ")
                        #  This is to make the student ID as a file
                        record = record + ".txt"
                        Admin1.AppendRecord(record)
                        print(data.array1)
                    # Second case:  Creating a recode and added it to the list
                    case '2':
                        Admin1 = Admin()
                        record = input("Enter the Student ID number like \"1190587\" : ")
                        while ((record.isdigit() == False) | (len(record) < 7) | (
                                len(record) > 7)):  # checks if the entered number is valid or not
                            print("Please enter only 7 digits! ")
                            record = input("Enter the Student ID number like this \"1190587\" : ")
                        #  This is to make the student ID as a file
                        record = record + ".txt"
                        Admin1.AppendRecord(record)
                        n = int(input("Enter 1 to add new record / 0 to quit the file "))
                        while (n == 1):
                            Admin1.CreateARecord(record)
                            n = int(input("Enter 1 to add new record / 0 to quit the file "))
                    case '3':
                        Admin1 = Admin()
                        # Entering the student id
                        StudentID = input("Enter the Student ID number like \"1190587\" :  ")
                        # Checking that the input Student ID is valid or not
                        while ((StudentID.isdigit() == False) | (len(StudentID) < 7) | (len(StudentID) > 7)):
                            print("Please Enter Valid Student ID..")
                            StudentID = input("Enter the Student ID number like this \"1190587\" : ")
                        StudentID = StudentID + '.txt'  # When it is valid , add the .txt to search for it
                        Admin1.UpdateRecord(StudentID)
                    case '4':
                        Admin1 = Admin()
                        StudentID = input("Enter the Student ID number like \"1190587\" :  ")  # Entering the student id
                        # Checking that the input Student ID is valid or not
                        while ((StudentID.isdigit() == False) | (len(StudentID) < 7) | (len(StudentID) > 7)):
                            # checks if the entered number is valid or not
                            print("Please Enter Valid Student ID: ")
                            StudentID = input("Enter the Studebt ID number like this \"1190587\" : ")
                        StudentID = StudentID + '.txt'
                        Admin1.StudentStatis(StudentID)
                    case '5':
                        Admin1 = Admin()
                        Admin1.StudentGlobal()
                    case '6':
                        Admin1 = Admin()
                        Admin1.StudentGlobal()
                        Admin1.SearchForanID()
                    case '7':
                        print("Exiting from the system as Admin...By!")
                        mainFunction()
                    case WrongOption:
                        print("Please Enter a Valid Operation!")
        # Second CASE
        # --> Student mood is activated
        case 'S' | 's':  # SECOND CASE
            while (True):
                print("**************************************************************")
                print("   Welcome to Students Records Management System \"SRMS\"")
                print("**************************************************************\n")
                print("NOTE: --> Please Choice an operation by entering it's number <--  \n")
                print("--------------------<<    Student List    >>-------------------------- \n")
                print("1. Find Student statistics.\n"
                      "2. Find Global statistics.\n"
                      "3. Exit the program. \n")
                entered = input("Enter a number from the list: ")
                match (entered):
                    case '1':
                        Student1 = Student()
                        StudentID = input("Enter the Student ID number like \"1190587\" :  ")  # Entering the student id
                        # Checking that the input Student ID is valid or not
                        while ((StudentID.isdigit() == False) | (len(StudentID) < 7) | (len(StudentID) > 7)):
                            # checks if the entered number is valid or not
                            print("Please Enter Valid Student ID: ")
                            StudentID = input("Enter the Studebt ID number like this \"1190587\" : ")
                        StudentID = StudentID + '.txt'
                        Student1.StudentStatis(StudentID)
                    case '2':
                        Student1 = Student()
                        Student1.StudentGlobal()
                    case '3':
                        print("Exiting from the system as Student...By!")
                        mainFunction()
                    case WrongOption:
                        print("Please Enter a Valid Operation!")

        case 'E' | 'e':
            print("Exiting from the System....By!")
            exit()
        case unknown_command:
            print("Try to login again!")

# Calling the main function
mainFunction()