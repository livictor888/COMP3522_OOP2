"""
Chain of Responsibility Pattern in a school administrative system
"""
import abc


class StudentAccount:
    """
    Encapsulates student account information. This would be the central
    student record in a school.
    """

    def __init__(self, name: str, age: int, student_id: str, program: str):
        self.student_name = name
        self.student_age = age
        self.student_id = student_id
        self.fees_due = 0
        self.program = program
        self.current_courses = []


class EnrolmentApplicationForm:
    """
    The Enrolment application form contains all the data the student
    filled out on the web enrolment system as well as a reference to
    the student account that was logged into while filling out this
    form.
    """

    def __init__(self, name: str, age: int, student_id: str,
                 courses_for_enrolment: list,student_account: StudentAccount,
                 enrolment_fees_paid: bool, school_year: int):
        """
        Instantiates a student enrolment form.
        :param name: a string
        :param age: an int, > 0
        :param student_id: a string, A_Number
        :param courses_for_enrolment: a list
        :param transcript: a Transcript
        :param student_account: a StudentAccount
        :param enrolment_fees_paid: a bool
        """
        self.name = name
        self.age = age
        self.student_id = student_id
        self.student_account = student_account
        self.courses_for_enrolment = courses_for_enrolment
        self.fees_paid = enrolment_fees_paid
        self.enrolment_year = school_year


class BaseSchoolFormHandler(abc.ABC):
    """
    Baseclass for all handlers that handle school forms. This can be
    refactored to work for all school forms, not just the enrolment
    form. Each handler can maintain a reference to another handler
    thereby enabling the chain of responsibility pattern.
    """

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handle_form(self, form: EnrolmentApplicationForm) -> (str, bool):
        """
        Each handler would have a specific implementation of how it
        processes a form.
        :param form: a EnrolmentApplicationForm
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        pass

    def set_handler(self, handler):
        """
        Each handler can invoke another handler at the end of it's
        processing of the form. This handler needs to implement the
        BaseSchoolFormHandler interface.
        :param handler: a BaseSchoolFormHandler
        """
        self.next_handler = handler


class ValidateStudentHandler(BaseSchoolFormHandler):
    """
    This handler ensures that the data on the form is in sync with that
    in the associated student account.
    """

    def handle_form(self, form: EnrolmentApplicationForm) -> (str, bool):
        """
        Checks to see if the name and student id on the form match the
        student account that was used to fill out the form.
        :param form: a EnrolmentApplicationForm
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        print("Validating student data")
        if form.name == form.student_account.student_name and \
           form.student_id == form.student_account.student_id:
            if not self.next_handler:
                return "", True
            return self.next_handler.handle_form(form)
        else:
            return "Student cannot be validated", False


class CheckCourseOfferingsHandler(BaseSchoolFormHandler):
    """
    This handler ensures that the courses being enrolled into are being
    offered in the coming academic year.
    """

    def handle_form(self, form: EnrolmentApplicationForm) -> (str, bool):
        """
        Checks each course that the student is enrolling into to ensure
        that it is being offered next year.
        :param form: a EnrolmentApplicationForm
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        print("Checking course offerings")
        enrolment_year = str(form.enrolment_year)
        for course in form.courses_for_enrolment:
            if enrolment_year not in course:
                return "Course not offered", False

        if not self.next_handler:
            return "", True
        return self.next_handler.handle_form(form)


class FeesHandler(BaseSchoolFormHandler):
    """
    Validates that the application fees have been paid by the student.
    """

    def handle_form(self, form: EnrolmentApplicationForm) -> (str, bool):
        """
        Validates that the application fees have been paid by the
        student.
        :param form: a EnrolmentApplicationForm
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        print("Checking if application fee was paid")
        if form.fees_paid:
            if not self.next_handler:
                return "", True
            return self.next_handler.handle_form(form)
        else:
            return "Application fees not paid", False


class EnrolmentSystem:
    """
    The Enrolment system is responsible for creating a chain of handlers
    that will eventually validate a EnrolmentApplicationForm and enrol
    the student into the courses selected.
    """
    def __init__(self):
        """
        Sets up the enrolment system and creates a chain of handlers.
        """

        print("\n\n--------- setup handlers ----------")
        course_handler = CheckCourseOfferingsHandler()
        student_validation_handler = ValidateStudentHandler()
        fees_handler = FeesHandler()

        # set handler order, course_handler -> student_validation -> fees_handler
        course_handler.set_handler(student_validation_handler)
        student_validation_handler.set_handler(fees_handler)
        self.handler_chain_head = course_handler

        # for demonstrating that you can start in the middle of a chain
        # only, generally this is rarely done and wouldn't be needed.
        self.middle_chain_handler = student_validation_handler

    def enrol(self, form: EnrolmentApplicationForm,
              skip_course_validation: bool = False) -> bool:
        """
        Enrols the student in the courses specified in the
        EnrolmentApplicationForm. Data validation checks are carried out
        before the student is enrolled.
        :param form:a EnrolmentApplicationForm
        :param skip_course_validation: a bool
        :return: bool, True if the student was enrolled, false otherwise
        """

        if not skip_course_validation:
            result = self.handler_chain_head.handle_form(form)
        else:
            result = self.middle_chain_handler.handle_form(form)
        #(string : 'Success' or 'Failure',  BOOLEAN)

        #result = "Student cannot be validated", False
        if result[1]:
            # passed all handlers
            for course in form.courses_for_enrolment:
                form.student_account.current_courses.append(course)
                print(f"Student enrolled in {course}")
            return True
        else:
            print(result[0])
            return False


def main():
    # --------- create form ----------
    # print("--------- create form ----------")
    student_account = StudentAccount("Zorak", 25, "A02355232", "CST Diploma")
    # enrolment_form = EnrolmentApplicationForm("Zorak", 25, "A02355232",
    #                                           ["AI for Games 2020",
    #                                            "OOP 2 2020", "Data Comms 2020",
    #                                            "Algorithms and Data Structures "
    #                                            "2020", "Career Development 2020"],
    #                                           student_account, True, 2020)
    enrolment_system = EnrolmentSystem()
    # enrolment_system.enrol(enrolment_form) # begin request

    #---------  Incorrect Data ---------
    # wrong student number
    # print("\n\n--------- Incorrect data ----------")
    # enrolment_form = EnrolmentApplicationForm("Zorak", 25, "A023532",
    #                                           ["AI for Games 2020",
    #                                            "OOP 2 2020", "Data Comms 2020",
    #                                            "Algorithms and Data Structures "
    #                                            "2020",
    #                                            "Career Development 2020"],
    #                                           student_account, True, 2020)
    # enrolment_system.enrol(enrolment_form)


    #--------- Can start from any handler -------
    # skipped check course offerings
    print("\n\n--------- Can start from any part of the chain ----------")
    enrolment_form = EnrolmentApplicationForm("Zorak", 25, "A02355232",
                                              ["AI for Games 2020",
                                               "OOP 2 2020", "Data Comms 2020",
                                               "Algorithms and Data Structures "
                                               "2020",
                                               "Career Development 2020"],
                                              student_account, True, 2020)
    enrolment_system.enrol(enrolment_form, True)




if __name__ == '__main__':
    main()

