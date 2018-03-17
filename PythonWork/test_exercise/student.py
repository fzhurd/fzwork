#!/usr/bin/python
# -*- coding: utf-8 -*-

class Student(object):

    name='john'

    def __init__(self, name, age, grade):

        self.name = name
        self.age = age
        self.grade = grade


    def print_name(self):
        print self.name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


# class UniversityStudent(Student):

#     def __init__(self, name, age, grade, major):

#         super(UniversityStudent, self).__init__(name, age, grade)

#         self.major =major


#     def print_name(self):
#         print self.name+" from university"



def main():
    student1= Student('fz', 10, 1)
    student1.print_name()

    # student2 = UniversityStudent('jerry',24,4, 'medicine')
    # student2.print_name()


if __name__=="__main__":
    main()