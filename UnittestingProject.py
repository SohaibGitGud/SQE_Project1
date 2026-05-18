import unittest
import SQE as student_system
class TestStudentSystem(unittest.TestCase):

    def setUp(self):
        student_system.students.clear()

    def test_add_student(self):
        student_system.students['101'] = {"name": "Ali", "marks": [85, 90, 88]}
        self.assertEqual(student_system.students['101']['name'], "Ali")
        self.assertEqual(len(student_system.students), 1)

    def test_duplicate_student(self):
        student_system.students['101'] = {"name": "Ali", "marks": [85, 90, 88]}
        self.assertIn('101', student_system.students)
        self.assertEqual(len(student_system.students), 1)
    def test_average_calculation(self):
        marks = [60, 70, 80]
        avg = sum(marks) / 3
        self.assertEqual(avg, 70.0)
    def test_grade_A(self):
        avg = 85
        if avg >= 80:
            grade = "A"
        self.assertEqual(grade, "A")

    def test_grade_B(self):
        avg = 70
        if avg >= 65:
            grade = "B"
        else:
            grade = "C"
        self.assertEqual(grade, "B")
    def test_grade_C(self):
        avg = 55
        if avg >= 50:
            grade = "C"
        else:
            grade = "F"
        self.assertEqual(grade, "C")

    def test_grade_F(self):
        avg = 40
        if avg >= 50:
            grade = "C"
        else:
            grade = "F"
        self.assertEqual(grade, "F")

    def test_delete_student(self):
        student_system.students['101'] = {"name": "Ali", "marks": [85, 90, 88]}
        del student_system.students['101']
        self.assertNotIn('101', student_system.students)

    def test_update_marks(self):
        student_system.students['101'] = {"name": "Ali", "marks": [85, 90, 88]}
        student_system.students['101']['marks'] = [75, 80, 85]
        self.assertEqual(student_system.students['101']['marks'], [75, 80, 85])

if __name__ == '__main__':
    unittest.main()