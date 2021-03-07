class Course:
 def __init__(self, course_ID, course_name, subject, credits, prerequisite, required_or_elective, category):
     self.course_ID = course_ID
     self.course_name = course_name
     self.subject = subject
     self.credits = credits
     self.prerequisite = prerequisite
     self.required_or_elective = required_or_elective
     self.category = category

#Getters and Setters
def get_course_ID(self):
    return self.course_ID

def set_course_ID(self, course_id):
    self.course_ID = course_id

def get_course_name(self):
    return self.course_name

def set_course_name(self, course_name):
    self.course_name = course_name

def get_subject(self):
    return self.subject

def set_subject(self, subject):
    self.subject = subject

def get_credits(self):
    return self.credits

def set_credits(self, credits):
    self.credits = credits

def get_prerequisite(self):
    return self.prerequisite

def set_prerequisite(self, prerequisite):
    self.prerequisite = prerequisite

def get_required_or_elective(self):
    return self.required_or_elective

def set_required_or_elective(self, required_or_elective):
    self.required_or_elective = required_or_elective

def get_category(self):
    return self.category

def set_category(self, category):
    self.category = category

def print_data(self, course_ID, course_name, subject, credits, prerequisite, required_or_elective, category):
    print(f"Course ID: {course_ID}")
    print(f"Couse Name: {course_name}")
    print(f"Subject: {subject}")
    print(f"Credits: {credits}")
    print(f"Prerequisite: {prerequisite}")
    print(f"Required or Eletive: {required_or_elective}")
    print(f"Category: {category}")

