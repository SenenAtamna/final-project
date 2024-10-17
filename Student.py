from Person import Person


class Student(Person):
    def __init__(self, name="", age=0, id=0, year_of_study=0, score_avg=0):
        super().__init__(name, age, id)
        self._year_of_study = year_of_study
        self._score_avg = score_avg

    def getYearOfStudy(self):
        return self._year_of_study

    def getScoreAvg(self):
        return self._score_avg

    def setYearOfStudy(self, year_of_study):
        self._year_of_study = year_of_study

    def setScoreAvg(self, score_avg):
        self._score_avg = score_avg

    def strForStudent(self):
        return self.strForPerson() + " Year: " + str(self.getYearOfStudy()) + " with Avg: " + str(self.getScoreAvg())

    def printMySelf(self):
        print(self.strForStudent())

    def informationToDic(self):
        from_person = super().informationToDic()
        from_student = {"year": self.getYearOfStudy(),
                        "score average": self.getScoreAvg()}
        from_person.update(from_student)
        return from_person

    def inputFromuser(self):
        super().inputFromuser()
        self._year_of_study = input("what year you are: ")
        self._score_avg = input("what is your average : ")
