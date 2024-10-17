class Person:

    def __init__(self, name="", age=0, id=0):
        self._name = name
        self._age = age
        self._id = id

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getId(self):
        return self._id

    def setName(self, name):
        self._name = name

    def setId(self, id):
        self._id = id

    def setAge(self, age):
        self._age = age

    def strForPerson(self):
        return "Im " + self.getName() + " And Im " + str(self.getAge()) + " My Id Is : " + str(self.getId())

    def printMySelf(self):
        print(self.strForPerson())

    def informationToDic(self):
        return {"name": self.getName(),
                "id": self.getId(),
                "age": self.getAge()}

    def inputFromuser(self):
        while True:
            user_id = input("Enter Id Number ")
            user_age = input("Enter User Age ")
            if user_id.isdigit() and user_age.isdigit():
                self._id = int(user_id)
                self._age = int(user_age)
                break
            else:
                print("Something Wrong, Id and Age Should Be a Numbers Try Again ")
        self._name = input("Enter User Name ")
