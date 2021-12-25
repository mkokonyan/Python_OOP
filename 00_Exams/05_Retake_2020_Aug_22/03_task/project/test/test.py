from unittest import TestCase, main

from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    def setUp(self):
        self.student = StudentReportCard("Martin", 12)

    def test_init_creates_all_attributes(self):
        self.assertEqual("Martin", self.student.student_name)
        self.assertEqual(12, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_invalid_name_setter_raise(self):
        with self.assertRaises(ValueError) as ex:
            student = StudentReportCard("", 11)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_whitespace_name(self):
        student = StudentReportCard(" ", 12)
        self.assertEqual(" ", student.student_name)
        self.assertEqual(12, student.school_year)
        self.assertEqual({}, student.grades_by_subject)

    def test_school_year_invalid_value_raise(self):
        with self.assertRaises(ValueError) as ex:
            student = StudentReportCard("Martin", 0)
        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_invalid_name_and_invalid_school_year_raise(self):
        with self.assertRaises(ValueError) as ex:
            student = StudentReportCard("", 0)
        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_add_grade(self):
        self.student.add_grade("Math", 6.00)
        self.assertEqual({"Math": [6.00]}, self.student.grades_by_subject)
        self.student.add_grade("Math", 5.00)
        self.assertEqual({"Math": [6.00, 5.00]}, self.student.grades_by_subject)
        self.student.add_grade("History", 5.00)
        self.assertEqual({"Math": [6.00, 5.00], "History": [5.00]}, self.student.grades_by_subject)

    def test_add_grade_return_value(self):
        trigger = self.student.add_grade("Math", 6.00)
        self.assertEqual(None, trigger)

    def test_average_grade_by_subject_with_empty_data(self):
        self.assertEqual("", self.student.average_grade_by_subject())

    def test_average_grade_by_subject_with_added_data(self):
        self.student.add_grade("Math", 6.00)
        self.student.add_grade("Math", 5.00)
        self.student.add_grade("Math", 4.00)
        self.student.add_grade("History", 5.00)
        self.assertEqual({"Math": [6.00, 5.00, 4.00], "History": [5.00]}, self.student.grades_by_subject)
        self.assertEqual("Math: 5.00\nHistory: 5.00", self.student.average_grade_by_subject())

    def test_average_grade_for_all_subjects_zero_division_raises(self):
        with self.assertRaises(ZeroDivisionError) as ex:
            self.student.average_grade_for_all_subjects()
        self.assertEqual("division by zero", str(ex.exception))

    def test_average_grade_for_all_subjects(self):
        self.student.add_grade("Math", 6.00)
        self.student.add_grade("Math", 5.00)
        self.student.add_grade("Math", 4.00)
        self.student.add_grade("History", 5.00)
        self.assertEqual({"Math": [6.00, 5.00, 4.00], "History": [5.00]}, self.student.grades_by_subject)
        self.assertEqual("Average Grade: 5.00", self.student.average_grade_for_all_subjects())

    def test_representation(self):
        self.student.add_grade("Math", 6.00)
        self.student.add_grade("Math", 5.00)
        self.student.add_grade("Math", 4.00)
        self.student.add_grade("History", 5.00)
        self.assertEqual({"Math": [6.00, 5.00, 4.00], "History": [5.00]}, self.student.grades_by_subject)
        expected_result = "Name: Martin\n" \
                          "Year: 12\n----------\n" \
                          "Math: 5.00\n" \
                          "History: 5.00\n" \
                          "----------\n" \
                          "Average Grade: 5.00"
        self.assertEqual(expected_result, repr(self.student))


if __name__ == "__main__":
    main()
