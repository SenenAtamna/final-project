from Person import Person


class Employe(Person):
    def __init__(self, name="", age=0, id=0, field_of_work="", salary=0):
        super().__init__(name, age, id)
        self._field_of_work = field_of_work
        self._salary = salary

    def getFieldOdWork(self):
        return self._field_of_work

    def getSalary(self):
        return self._salary

    def setSalary(self, salary):
        self._salary = salary

    def setFieldOfWork(self, field_of_work):
        self._field_of_work = field_of_work

    def strForEmploye(self):
        return self.strForPerson() + " Working at: " + self.getFieldOdWork() + "My Salary: " + str(self.getSalary())

    def printMySelf(self):
        print(self.strForEmploye())

    def informationToDic(self):
        from_person = super().informationToDic()
        from_employee = {"field of work": self.getFieldOdWork(),
                         "salary": self.getSalary()}
        from_person.update(from_employee)
        return from_person

    def inputFromuser(self):
        super().inputFromuser()
        self._field_of_work = input("what is your work: ")
        self._salary = input("what is your salary : ")
