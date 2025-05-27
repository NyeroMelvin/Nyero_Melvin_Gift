class Person:
    def login(self):
        print('Login successful')

class Student(Person):
    def __init__(self, studentNumber, registrationNumber):
        self.studentNumber = studentNumber
        self.registrationNumber = registrationNumber
        print(f"StudentCreated: Student Number {self.studentNumber}, Registration Number {self.registrationNumber}")

    def login(self, enteredStudentNumber, enteredRegistrationNumber):
        if self.studentNumber == enteredStudentNumber and self.registrationNumber == enteredRegistrationNumber:
            print('Welcome dear Student! Login successful.')
            return True
        else:
            print('Incorrect student number or registration number.')
            return False

class Lecturer(Person):
    def __init__(self, employeeId, employeeName, hoursperweek):
        self.employeeId = employeeId
        self.employeeName = employeeName
        self.hoursperweek = hoursperweek
        print(f"LecturerCreated: Employee ID {self.employeeId}, Name {self.employeeName}, Hours per week {self.hoursperweek}")

    def login(self, enteredEmployeeId):
        if self.employeeId == enteredEmployeeId:
            print(f"Welcome Lecturer {self.employeeName}! Login successful.")
            return True
        else:
            print("Incorrect employee ID.")
            return False

class Staff(Person):
    def __init__(self, staffId, staffName, department):
        self.staffId = staffId
        self.staffName = staffName
        self.department = department
        print(f"StaffCreated: Staff ID {self.staffId}, Name {self.staffName}, Department {self.department}")

    def login(self, enteredStaffId):
        if self.staffId == enteredStaffId:
            print(f"Welcome Staff member {self.staffName}! Login successful.")
            return True
        else:
            print("Incorrect staff ID.")
            return False

print("\n--- Student Login ---")
student1 = Student("23/U/16401", "REG2300716401")
student1.login("23/U/16401", "REG02300716401")
student1.login("S002", "REG001")

print("\n--- Lecturer Login ---")
lecturer1 = Lecturer("L005", "Dr.Nsabagwa Mary", 15)
lecturer1.login("L005")
lecturer1.login("L006")

