import random
class employee(object):
    def __init__(self, name, last):
        self.name = name
        self.last = last

    @property
    def email(self):
        return self.name + self.last + '.email'


emp_1 = employee('Juan', 'Almonte')


class university(object):
    def __init__(self, name, pay, n_student):
        self.name = name
        self.pay = pay
        self.n_student = n_student


university_1 = university('O&M', '15,000', '30,000')


class students:
    #payment = university(None,'15,000',None)
    # payment = payment.pay
    def __init__(self, first, last, id_, pay=None):
        self.first = first
        self.last = last
        self.id_ = id_
        self.pay = pay


student_1 = students('Juancho', 'Diaz', 12345, university_1.pay)
student_2 = students('Rafael', 'Diaz', 12345, university_1.pay)
# print(student_1.__init__(student_1.first,student_1.last,student_1.id_))
#print(student_1.first)
#print(student_1.last)
#print(student_1.id_)
#print(student_1.pay)
class teachers:
  courses = ['Science','Spanish','History','Computer science']
  def __init__(self,first,last,course):
   self.first = first
   self.last = last
   self.course = course
teacher_1 = teachers('Manuel','Herrera',random.choice(teachers.courses))
print(teacher_1.course)