from project.student import Student
from unittest import TestCase, main


class TestStudent(TestCase):
    def setUp(self):
        self.student_1 = Student("Peter")
        self.student_2 = Student("George", {"Python": ["OOP"],
                                            "JavaScript": ["Basics", "Fundamentals"]})

    def test_init_creates_all_attributes(self):
        self.assertEqual("Peter", self.student_1.name)
        self.assertEqual({}, self.student_1.courses)
        self.assertEqual({"Python": ["OOP"], "JavaScript": ["Basics", "Fundamentals"]}, self.student_2.courses)

    def test_enroll_updating_notes(self):
        trigger = self.student_2.enroll("Python", ["Fundamentals", "Web"])
        expected_result = {"Python": ["OOP", "Fundamentals", "Web"], "JavaScript": ["Basics", "Fundamentals"]}
        self.assertEqual(expected_result, self.student_2.courses)
        expected_return = "Course already added. Notes have been updated."
        self.assertEqual(expected_return, trigger)

    def test_enroll_adding_new_notes_with_add_course_attribute(self):
        trigger = self.student_2.enroll("Java", ["Fundamentals", "Web"], add_course_notes="Y")
        expected_result = {"Python": ["OOP"], "JavaScript": ["Basics", "Fundamentals"], "Java": ["Fundamentals", "Web"]}
        self.assertEqual(expected_result, self.student_2.courses)
        expected_return = "Course and course notes have been added."
        self.assertEqual(expected_return, trigger)

    def test_enroll_adding_new_notes_without_add_course_attribute(self):
        trigger = self.student_2.enroll("Java", ["Fundamentals", "Web"])
        expected_result = {"Python": ["OOP"], "JavaScript": ["Basics", "Fundamentals"], "Java": ["Fundamentals", "Web"]}
        self.assertEqual(expected_result, self.student_2.courses)
        expected_return = "Course and course notes have been added."
        self.assertEqual(expected_return, trigger)

    def test_enroll_adding_course(self):
        trigger = self.student_2.enroll("Java", ["Fundamentals", "Web"], add_course_notes="N")
        self.assertEqual([], self.student_2.courses["Java"])
        expected_return = "Course has been added."
        self.assertEqual(expected_return, trigger)

    def test_add_notes_no_course_found_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student_2.add_notes("Java", ["Fundamentals", "Web"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes(self):
        trigger = self.student_2.add_notes("Python", "Fundamentals")
        expected_result = {"Python": ["OOP", "Fundamentals"], "JavaScript": ["Basics", "Fundamentals"]}
        expected_return = "Notes have been updated"
        self.assertEqual(expected_result, self.student_2.courses)
        self.assertEqual(expected_return, trigger)

    def test_leave_course_not_exist_raise(self):
        with self.assertRaises(Exception) as ex:
            self.student_2.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course(self):
        trigger = self.student_2.leave_course("Python")
        self.assertEqual({"JavaScript": ["Basics", "Fundamentals"]}, self.student_2.courses)
        expected_return = "Course has been removed"
        self.assertEqual(expected_return, trigger)


if __name__ == '__main__':
    main()
