class Student:
    def __init__(self, RAM_ID, first_name, last_name, major, minor, career_goal, hobbies_interests, courses_taken):
        self.RAM_ID = RAM_ID
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.minor = minor
        self.career_goal = career_goal
        self.hobbies_interests = hobbies_interests
        self.courses_taken = courses_taken

    #Getters and Setters
    def get_RAM_ID(self):
        return self.RAM_ID

    def set_RAM_ID(self, id):
        self.RAM_ID = id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_major(self):
        return self.major

    def set_major(self, major):
        self.major = major

    def get_minor(self):
        return self.minor

    def set_minor(self, minor):
        self.minor = minor

    def get_career_goal(self):
        return self.career_goal

    def set_career_goal(self, career_goal):
        self.career_goal = career_goal

    def get_hobbies_interests(self):
        return self.hobbies_interests

    def set_hobbies_interests(self, hobbies_interests):
        self.hobbies_interests = hobbies_interests

    def get_courses_taken(self):
        return self.courses_taken

    def set_courses_taken(self, courses_taken):
        self.courses_taken = courses_taken

    def num_of_courses(self, courses_taken):
        self.courses_taken = courses_taken
        print(len(courses_taken))

    def print_data(self, RAM_ID, first_name, last_name, major, minor, career_goal, hobbies_interests, courses_taken):
        print(f"RAM ID: {RAM_ID}")
        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Major: {major}")
        print(f"Minor: {minor}")
        print(f"Career Goal: {career_goal}")
        print(f"Hobbies and Interests: {hobbies_interests}")
        print(f"Courses Taken: {courses_taken}")


stud1 = Student("R0xxxxxx", "Darrien", "Hunt", "Programming", "", ["Software Engineer", "Database Administrator"], [
                "Coding", "Video Games", "Reading"], ["BCS 120", "BCS 160", "EGL 101", "MTH 129", "PSY 101"])

stud1.num_of_courses(["BCS 120", "BCS 160", "EGL 101", "MTH 129", "PSY 101"])
