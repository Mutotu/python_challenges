class Assignment:
    def __init__(self, name, github_url):
        self.name = name
        self.github_url = github_url
        self.completed = False
        self.grade = None

    def mark_done(self, grade):
        """Sets the assignment as completed and assigns a grade."""
        self.completed = True
        self.grade = grade


class Student:
    def __init__(self, name):
        self.name = name
        self.pending_homeworks = []
        self.completed_homeworks = []

    def assign_homework(self, assignment):
        """Adds the given assignment to the student's pending homework list."""
        self.pending_homeworks.append(assignment)

    def complete_homework(self, homework_name, grade):
        """
        Completes the specified homework by marking it as done,
        and moving it from pending to completed homeworks.
        """
        for assignment in self.pending_homeworks:
            if assignment.name == homework_name:
                assignment.mark_done(grade)
                self.completed_homeworks.append(assignment)
                self.pending_homeworks.remove(assignment)
                return True
        return False

    def print_outstanding_homeworks(self):
        """Prints the names of the student's pending homeworks."""
        if not self.pending_homeworks:
            print(f"{self.name} has no outstanding homeworks!")
        else:
            outstanding_homeworks = ", ".join(hw.name for hw in self.pending_homeworks)
            print(f"{self.name} still needs to turn in: {outstanding_homeworks}")


class SeiClass:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        """Adds a student to the SEI class."""
        self.students.append(student)

    def assign_homework(self, assignment):
        """Assigns the given homework to all students in the class."""
        for student in self.students:
            student.assign_homework(assignment)

    def print_avg_grade(self):
        """
        Prints the average grade for the assignments that have been completed by all students.
        """
        total_grade = 0
        num_completed_assignments = 0

        for student in self.students:
            for assignment in student.completed_homeworks:
                if assignment.grade is not None:
                    total_grade += assignment.grade
                    num_completed_assignments += 1

        if num_completed_assignments == 0:
            print("No assignments have been graded yet.")
        else:
            avg_grade = total_grade / num_completed_assignments
            print(f"Average grade for the class: {avg_grade:.2f}")


# Sample usage:
nick = Student('Nick')
sarah = Student('Sarah')
brandi = Student('Brandi')

sei30 = SeiClass('sei30')
sei30.add_student(nick)
sei30.add_student(sarah)
sei30.add_student(brandi)

assignment1 = Assignment('Bounty Hunters', 'https://github.com/WDI-SEA/mongoose-practice')

sei30.assign_homework(assignment1)

nick.complete_homework('Bounty Hunters', 98)
sarah.complete_homework('Bounty Hunters', 95)

nick.print_outstanding_homeworks()
sarah.print_outstanding_homeworks()
brandi.print_outstanding_homeworks()

# Bonus: Print average grade for the class
sei30.print_avg_grade()
