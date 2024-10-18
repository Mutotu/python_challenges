class Task:

    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = 'Pending'

    def complete(self):
        self.status = 'Completed'
        print(f"Task '{self.description}' is now {self.status}.")

    def __repr__(self):
        return f"Task(description={self.description}, status={self.status}, deadline={self.deadline})"


class Employee:

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role
        self.tasks = []  # List of tasks assigned to the employee

    def __repr__(self):
        return f"Employee(name={self.name}, salary={self.salary}, role={self.role})"

    def work(self):
        print(f"{self.name} is working.")

    def add_task(self, task: Task):
        self.tasks.append(task)
        print(f"{self.name} has been assigned task '{task.description}'.")

    def complete_task(self, task_description):
        for task in self.tasks:
            if task.description == task_description and task.status != 'Completed':
                task.complete()
                return True
        return False

    def get_tasks(self):
        return [task.description for task in self.tasks]

    def increase_salary(self, amount):
        self.salary += amount
        print(f"{self.name}'s salary increased by {amount} to {self.salary}")


class Manager(Employee):

    def __init__(self, name, salary, role):
        super().__init__(name, salary, role)
        self.team = []

    def assign_task(self, employee: Employee, task: Task):
        employee.add_task(task)

    def add_team_member(self, employee: Employee):
        self.team.append(employee)
        print(f"{employee.name} has been added to {self.name}'s team.")

    def review_performance(self, employee: Employee):
        completed_tasks = [task for task in employee.tasks if task.status == 'Completed']
        print(f"{employee.name} has completed {len(completed_tasks)} out of {len(employee.tasks)} tasks.")

    def __repr__(self):
        return f"Manager(name={self.name}, team_size={len(self.team)})"


class Developer(Employee):

    def __init__(self, name, salary, role, programming_language):
        super().__init__(name, salary, role)
        self.programming_language = programming_language

    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}.")

    def __repr__(self):
        return f"Developer(name={self.name}, language={self.programming_language})"


# Sample usage
task1 = Task('Build API', '2024-12-01')
task2 = Task('Develop Frontend', '2024-12-15')

dev1 = Developer('Alice', 80000, 'Developer', 'Python')
dev2 = Developer('Bob', 85000, 'Developer', 'JavaScript')
mgr = Manager('Carol', 95000, 'Manager')

mgr.add_team_member(dev1)
mgr.add_team_member(dev2)

mgr.assign_task(dev1, task1)
mgr.assign_task(dev2, task2)

dev1.complete_task('Build API')

mgr.review_performance(dev1)
mgr.review_performance(dev2)

dev1.write_code()
dev2.write_code()

dev1.increase_salary(5000)
