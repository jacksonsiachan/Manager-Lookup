class Employee
    manager = {"Marketing": "Peter", "MIS": "Cleo", "Finance": "Cindy"}
    def __init__(self, name, group, username):
        self.name = name
        self.group = group
        self.username = username

    def create_email(self):
        return "The email address of {} is {}@gmail.com".format(self.name, self.username)

    def check_manager(self):
        if self.group in Employee.manager.keys():
           return "The manager of the group where {} belongs to is {}.".format(self.name, Employee.manager[self.group])
        else:
           return "{} group not found!".format(self.group)

employee1 = Employee("Luke", "Marketing", "lk45")
print(employee1.check_manager())               


