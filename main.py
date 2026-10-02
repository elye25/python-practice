# ============================================================
#              ELYE STUDENT MANAGEMENT SYSTEM
#                   ONLINE PYTHON VERSION
# ============================================================

students = []


# ------------------------------------------------------------
# DISPLAY HEADER
# ------------------------------------------------------------

def header():
    print()
    print("=" * 60)
    print("          ELYE STUDENT MANAGEMENT SYSTEM")
    print("=" * 60)


# ------------------------------------------------------------
# REGISTER STUDENT
# ------------------------------------------------------------

def register_student():

    header()
    print("                 REGISTER STUDENT")
    print("-" * 60)

    name = input("Enter student name: ")
    admission = input("Enter admission number: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    form = input("Enter class/form: ")
    phone = input("Enter phone number: ")

    student = {
        "name": name,
        "admission": admission,
        "age": age,
        "gender": gender,
        "form": form,
        "phone": phone
    }

    students.append(student)

    print()
    print("Student registered successfully!")


# ------------------------------------------------------------
# VIEW STUDENTS
# ------------------------------------------------------------

def view_students():

    header()
    print("                  STUDENT LIST")
    print("-" * 60)

    if len(students) == 0:
        print("There are currently no registered students.")
        return

    for number, student in enumerate(students, 1):

        print()
        print("STUDENT", number)
        print("-" * 40)

        print("Name              :", student["name"])
        print("Admission Number  :", student["admission"])
        print("Age               :", student["age"])
        print("Gender            :", student["gender"])
        print("Class/Form        :", student["form"])
        print("Phone             :", student["phone"])


# ------------------------------------------------------------
# SEARCH STUDENT
# ------------------------------------------------------------

def search_student():

    header()
    print("                  SEARCH STUDENT")
    print("-" * 60)

    search = input("Enter name or admission number: ")

    found = False

    for student in students:

        if (
            search.lower() in student["name"].lower()
            or search.lower() in student["admission"].lower()
        ):

            print()
            print("STUDENT FOUND")
            print("-" * 40)

            print("Name             :", student["name"])
            print("Admission Number :", student["admission"])
            print("Age              :", student["age"])
            print("Gender           :", student["gender"])
            print("Class/Form       :", student["form"])
            print("Phone            :", student["phone"])

            found = True

    if not found:
        print()
        print("No matching student was found.")


# ------------------------------------------------------------
# SCHOOL INFORMATION
# ------------------------------------------------------------

def school_information():

    header()

    print("                 SCHOOL INFORMATION")
    print("-" * 60)

    print()
    print("School Name : ELYE SCHOOL")
    print("System      : Student Management System")
    print("Version     : 1.0")
    print("Developer   : ELYE")
    print()
    print("This programme manages basic student information.")


# ------------------------------------------------------------
# DASHBOARD
# ------------------------------------------------------------

def dashboard():

    header()

    print("                     DASHBOARD")
    print("-" * 60)

    total = len(students)

    male = 0
    female = 0

    for student in students:

        if student["gender"].lower() == "male":
            male += 1

        elif student["gender"].lower() == "female":
            female += 1

    print()
    print("Total Students :", total)
    print("Male Students  :", male)
    print("Female Students:", female)


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def main():

    while True:

        header()

        print()
        print("                      MAIN MENU")
        print("-" * 60)

        print("1. Register Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Dashboard")
        print("5. School Information")
        print("6. Exit")

        print("-" * 60)

        choice = input("Choose an option (1-6): ")

        if choice == "1":

            register_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            dashboard()

        elif choice == "5":

            school_information()

        elif choice == "6":

            print()
            print("=" * 60)
            print("Thank you for using ELYE Student Management System!")
            print("=" * 60)
            break

        else:

            print()
            print("Invalid option.")
            print("Please choose a number from 1 to 6.")

        input("\nPress ENTER to return to the main menu...")


# ------------------------------------------------------------
# START PROGRAMME
# ------------------------------------------------------------

main()