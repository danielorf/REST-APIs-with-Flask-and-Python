
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        if len(self.marks) > 0:
            return sum(self.marks)/len(self.marks)
        else:
            return 0

    # def friend(self, name):
    #     return Student(name, self.school)

    @ classmethod
    def friend(cls, origin, name, *args, **kwargs):
        return cls(name, origin.school, *args, **kwargs)


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

anna = Student('Anna', 'Oxford')
print(anna.name + ', ' + anna.school)

bob = Student.friend(anna, 'Bob')
print(bob.name + ', ' + bob.school)

george = WorkingStudent('George', 'Harvard', '200000', job_title='Architect')
print(george.name + ', ' + george.school + ', ' + george.salary)

carl = WorkingStudent.friend(george, 'carl', '10', job_title='Janitor')
print(carl.name + ', ' + carl.school + ', ' + carl.salary)

steve = WorkingStudent.friend(carl, 'steve', '30', 'Software Dev')
print(steve.name + ', ' + steve.school + ', ' + steve.salary, ', ', steve.job_title)