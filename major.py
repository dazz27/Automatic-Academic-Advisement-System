class Major:
    def __init__(self, major_name, required_courses, total_credits_required, concentration):
        self.major_name = major_name
        self.required_courses = required_courses
        self.total_credits_required = total_credits_required
        self.concentration = concentration

    #Getters and Setters
    def get_major_name(self):
        return self.major_name

    def set_major_name(self, major_name):
        self.major_name = major_name

    def get_required_courses(self):
        return self.required_courses

    def set_required_courses(self, required_courses):
        self.required_courses = required_courses

    def get_total_credits_required(self):
        return self.total_credits_required

    def set_total_credits_required(self, total_credits_required):
        self.total_credits_required = total_credits_required

    def get_concentration(self):
        return self.concentration

    def set_concentration(self, concentration):
        self.concentration = concentration

stud1 = Major("Computer Programming and Information Systems", ["BCS 109", "BCS 120", "BCS 160", "BCS 230", "BCS 215"], 123, "Software Development")