# A dictionary as student list
students_list = {}


class Fullname:
    # declare names and remove whitespace
    def __init__(self, first_name="", second_name=""):
        self.first_name = first_name.strip() if first_name else ""
        self.second_name = second_name.strip() if second_name else ""

    def set_name(self, first_name, second_name):
        self.first_name = str(first_name).strip()
        self.second_name = str(second_name).strip()
        return self

# get fullname with each first letters capitalized
    def get_full_name(self):
        parts = [part for part in (self.first_name, self.second_name) if part]
        return " ".join(part.capitalize() for part in parts) if parts else ""

    def __str__(self):
        return self.get_full_name()

# student class and details
class Students:
    def __init__(self):
        self.First_name = ""
        self.Second_name = ""
        self.age = ""
        self.DOB = ""
        self.Fullname = ""
        self.Gender = ""
        self.National = ""
        self.National_ID = ""
        self.phone_number = ""
        self.email = ""
        self.Residential_Address = ""
# get student detail from the user
    def get_students_details(self):
        self.First_name = input("Student first name: ").strip()
        self.Second_name = input("Student second name: ").strip()

# display an exception message if the user do no provide student name
        if not self.First_name or not self.Second_name:
            raise ValueError("Student first and second names are required.")

# join first name and second name as fullname
        fullname_obj = Fullname(self.First_name, self.Second_name)
        self.Fullname = fullname_obj.get_full_name()

#prompt the user to enter student details
        self.age = input("Student age: ").strip()
        self.DOB = input("Student date of birth: ").strip()
        self.Gender = input("Student gender: ").strip()
        self.National = input("Student nationality: ").strip()
        self.National_ID = input("Enter national ID: ").strip()
        self.phone_number = input("Student phone number: ").strip()
        self.email = f"{self.First_name.lower()}.{self.Second_name.lower()}@gmail.com"
        self.Residential_Address = input("Enter residential address: ").strip()

# student details as a dictionary
        student_data = {
            "first_name": self.First_name,
            "second_name": self.Second_name,
            "age": self.age,
            "DOB": self.DOB,
            "Full_name": self.Fullname,
            "gender": self.Gender,
            "nationality": self.National,
            "national_ID": self.National_ID,
            "phone_number": self.phone_number,
            "email": self.email,
            "residential_address": self.Residential_Address,
        }
        # used student ID as a key for the student identity to their information
        students_list[self.National_ID] = student_data
        return student_data

class Previous_school(Students):
    def __init__(self):
        super().__init__()
        self.Previous_school = ""
        self.Cetificate_name = ""
        self.GPA = ""
        self.Major = ""
        self.Recommendation = ""
        self.Position = ""
        self.student_previous_school = {}

# required info from previou schools
    def get_previous_school_details(self):
        self.Previous_school = input("Previous school: ").strip() or "Not provided"
        self.Cetificate_name = input("Certificate name/type: ").strip() or "Not provided"
        self.GPA = input("Your GPA/Grade: ").strip() or "Not provided"
        self.Major = input("Your major: ").strip() or "Not provided"
        self.Recommendation = input("Optional - Recommendation if any: ").strip() or "Not provided"
        self.Position = input("Optional - Any Position held: ").strip() or "Not provided"
# student previous info as a dictionary
        self.student_previous_school = {
            "Previous school": self.Previous_school,
            "Certificate": self.Cetificate_name,
            "GPA": self.GPA,
            "Major": self.Major,
            "Recommendation": self.Recommendation,
            "Position": self.Position,
        }
        return self.student_previous_school

# update overall details as a student list
    def get_students_details(self):
        student_data = super().get_students_details()
        previous_school_data = self.get_previous_school_details()
        student_data.update(previous_school_data)
        students_list[self.National_ID] = student_data
        return student_data


# # Example usage: uncomment when you want to run it interactively.
# student = Previous_school()
# student.get_students_details()
# print(students_list)