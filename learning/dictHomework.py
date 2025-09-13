subjectsDict = {}
studentsDict = {}

while True:
    details = input("Enter subject details - NAME,MAX Numbers: ")
    if details != "done" :
        subject = details.split(",")
        subjectsDict[subject[0]] = int(subject[1])
    else:
        break

while True:
    marksDict = {}
    studentName = input("Enter student name: ")
    if studentName == "done" :
        break

    while True:
        subject = input("Enter student subject details - subject, passing numbers: ")
        if subject != "done" :
            s = subject.split(",")
            marksDict.update({s[0]:int(s[1])})

            print(marksDict)
        else:
             break

    studentsDict.update({studentName: marksDict})
    print(studentsDict)

while True:
    print("Menu:",
          "1. show total percentage of given student",
          "2. show percentage marks of a given subject of each student",
          "3. show the max percent of a given subject and the name of student",
          "4. quit", sep="\n")

    menu = int(input("Enter above option to continue..."))
    if menu == 1:
        TotalMarks = 0
        studentTotalMarks = 0

        for i in subjectsDict.values():
            TotalMarks = TotalMarks + int(i)

        name = input("Enter student name: ")

        subjects = studentsDict[name]
        for i in subjects.values():
            studentTotalMarks = studentTotalMarks + int(i)

        print(name, ", Total percentage:", (studentTotalMarks / TotalMarks) * 100, "%")

    elif menu == 2:
        subName = input("Enter subject name: ")
        for student in studentsDict:
            for subject in studentsDict[student]:
                if subject == subName:
                    print(student, ": ", (studentsDict[student][subject] / subjectsDict[subName]) * 100, "%")

    elif menu == 3:
        topper = {}
        subName = input("Enter subject name: ")
        outOfSubValue = subjectsDict[subName]
        maxFlag=0
        for student in studentsDict:
            subjectValue = studentsDict[student][subName]
            percent = (subjectValue / outOfSubValue) * 100
            if percent >maxFlag:
                maxFlag = percent
                # print(maxFlag)
                topper.update({
                    "Name": student,
                    "Subject": subName,
                    "Total": percent,
                })
        # print(maxFlag,topper)
        print("Subject :", topper['Subject'], "| Topper Student: ", topper['Name'], "| Percentage: ", topper['Total'], "%" )

    elif menu == 4:
        break