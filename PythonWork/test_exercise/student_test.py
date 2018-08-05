#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
from student import *

class StudentTest(unittest.TestCase):

    def setUp(self):
        self.student1 = Student("selina", 3, 5)
        self.student2 = Student("danny", 23, 25)


    def test_name(self):

        self.assertEqual(self.student1.get_name(), 'selina')

    def test_age(self):

        self.assertEqual(self.student1.get_age(), 35)



if __name__=="__main__":
    unittest.main()
