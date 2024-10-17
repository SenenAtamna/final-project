import os
import json
import pandas as pd
from Student import Student
from Employe import Employe
from Person import Person
from Choices import Choices

def mainScreen():
    Choices.printAllOption()


def saveAllDatatoFile(list_of_people):
    people_list = []
    my_path = os.getcwd()
    for person in list_of_people:
        people_list.append(person.informationToDic())
    output_file_name = input("What is Your Output File Name ? ")
    list_of_persons_df = pd.DataFrame(people_list)
    list_of_persons_df.to_csv(os.path.join(my_path, output_file_name), index=False)
    print("Saved Successfully ")



def functhatPrintPerson(person_list, index):
    person_list[index].printMySelf()


def saveNewEntry(person_list, list_for_age_avg, person_dic):
    employee_or_student = input("you are employee or student : ")
    if employee_or_student == "student":
        per = Student()
    elif employee_or_student == "employee":
        per = Employe()
    else:
        per = Person()
    per.inputFromuser()
    person_list.append(per)
    print("ID [" + str(per.getId()) + "] Added Successfully")
    list_for_age_avg[0] = list_for_age_avg[0] + per.getAge()
    person_dic[per.getId()] = len(person_list) - 1


def searchById(user_list, user_dic):
    chosen_id = input("Which Id You Looking For : ")
    if chosen_id.isdigit() and int(chosen_id) in user_dic:
        return functhatPrintPerson(user_list, user_dic[int(chosen_id)])
    print("Id Not Found")


def printAgesAverage(list_for_calc_avg, person_list):
    if len(person_list) == 0:
        return print("There Is No Person to Calculate Age Average")
    avg = list_for_calc_avg[0] / len(person_list)
    print("The Average of ALL Ages : is " + str(avg))


def printAllNames(user_list):
    print("The names Are : ")
    for person in user_list:
        print(person.getName())
        print("")


def printAllId(user_list):
    print("The IDs Are : ")
    for person in user_list:
        print(person.getId())


def exitFunction():
    while True:
        yes_no = input("Are you Sure Want to Exit? y/n ")
        if yes_no == "y":
            return False
        elif yes_no == "n":
            return True
        else:
            print("You Can Choose just y/n")


def printAllEntry(user_list):
    for person in user_list:
        person.printMySelf()


def findPersonByLocation(list_of_person):
    chosen_index = input("Please What Index you looking for ")
    try:
        chosen_index = int(chosen_index)
        functhatPrintPerson(list_of_person, chosen_index)
    except:
        print("Index Not Found")


# Start From Here Main
people_list_all = []
people_dict_all = {}
list_for_avg_calc = [0]
check_loop = True
while check_loop:
    mainScreen()
    user_choice = input("Please Enter Your Choice: ")
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == Choices.SAVE_A_NEW_ENTRY.value:
            saveNewEntry(people_list_all, list_for_avg_calc, people_dict_all)
        elif user_choice == Choices.SEARCH_BY_ID.value:
            searchById(people_list_all, people_dict_all)
        elif user_choice == Choices.PRINT_AGES_AVERAGE.value:
            printAgesAverage(list_for_avg_calc, people_list_all)
        elif user_choice == Choices.PRINT_ALL_NAMES.value:
            printAllNames(people_list_all)
        elif user_choice == Choices.PRINT_ALL_IDS.value:
            printAllId(people_list_all)
        elif user_choice == Choices.PRINT_ALL_ENTRIES.value:
            printAllEntry(people_list_all)
        elif user_choice == Choices.PRINT_ENTRY_BY_INDEX.value:
            findPersonByLocation(people_list_all)
        elif user_choice == Choices.SAVE_ALL_ENTRY.value:
            saveAllDatatoFile(people_list_all)
        elif user_choice == Choices.EXIT.value:
            check_loop = exitFunction()
    else:
        input("The [" + user_choice + "] Dosnt Exist PRESS ENTER tO Chose Another One")
    input("Press Enter to Continue")
print("GoodBye,This Is For Git")
