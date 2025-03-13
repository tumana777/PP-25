# import module, unittest
#
# class TestModule(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(module.add(1, 2), 3)
#         self.assertEqual(module.add(85, 37), 122)
#         self.assertEqual(module.add(-17, 37), 20)
#         self.assertEqual(module.add(-17, -37), -54)
#
#     def test_sub(self):
#         self.assertEqual(module.sub(1, 2), -1)
#         self.assertEqual(module.sub(105, 17), 88)
#         self.assertEqual(module.sub(-8, 12), -20)
#         self.assertEqual(module.sub(-10, -16), 6)
#
#     def test_mul(self):
#         self.assertEqual(module.mul(5, 7), 35)
#         self.assertEqual(module.mul(-5, 7), -35)
#         self.assertEqual(module.mul(0, 7), 0)
#         self.assertEqual(module.mul(-5, -7), 35)
#
#     def test_div(self):
#         self.assertEqual(module.div(5, 2), 2.5)
#         self.assertEqual(module.div(10, 2), 5)
#         self.assertEqual(module.div(0, 2), 0)
#
#         # self.assertRaises(ValueError, module.div, 5, 0)
#
#         with self.assertRaises(ValueError):
#             module.div(8, 0)
#
#     def test_is_sorted(self):
#         self.assertEqual(module.is_sorted([5, 6, 2, 8, 1, 3]), [1, 2, 3, 5, 6 , 8])
#         self.assertEqual(module.is_sorted([]), [])
#
#     def test_is_even(self):
#         self.assertTrue(module.is_even(6))
#         self.assertTrue(module.is_even(4))
#         self.assertTrue(module.is_even(8))
#         self.assertFalse(module.is_even(9))
#         self.assertFalse(module.is_even(3))

# import unittest
# from module import Student
#
# class TestStudent(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print("Set up class\n")
#
#     @classmethod
#     def tearDownClass(cls):
#         print("Teardown class")
#
#     def setUp(self):
#         print("Setup")
#
#         self.student1 = Student("John", "Johnson", 2000)
#         self.student2 = Student("Walter", "White", 3000)
#
#     def tearDown(self):
#         print("Teardown\n")
#
#     def test_email(self):
#         print("Testing email")
#
#         self.assertEqual(self.student1.email, "John.Johnson@gmail.com")
#         self.assertEqual(self.student2.email, "Walter.White@gmail.com")
#
#         self.student1.first_name = "Bob"
#         self.student2.first_name = "Jessy"
#
#         self.assertEqual(self.student1.email, "Bob.Johnson@gmail.com")
#         self.assertEqual(self.student2.email, "Jessy.White@gmail.com")
#
#     def test_full_name(self):
#
#         print("testing full name")
#
#         self.assertEqual(self.student1.full_name, "John Johnson")
#         self.assertEqual(self.student2.full_name, "Walter White")
#
#         self.student1.first_name = "Bob"
#         self.student2.first_name = "Jessy"
#
#         self.assertEqual(self.student1.full_name, "Bob Johnson")
#         self.assertEqual(self.student2.full_name, "Jessy White")
#
#
#     def test_apply_discount(self):
#
#         print("Testing apply discount")
#
#         self.student1.apply_discount()
#         self.student2.apply_discount()
#
#         self.assertEqual(self.student1.pay, 1800)
#         self.assertEqual(self.student2.pay, 2700)
#
#
# if __name__ == "__main__":
#     unittest.main()