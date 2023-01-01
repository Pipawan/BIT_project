from random import *
alphabets = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
home_town = ["Rampur", "Khadrauli", "Meghauli",
             "Gitanagar", "Kamalnagar", "Bikashchok"]
programming_knowledge = ["python", "java", "html", "c++"]
# name section


def name_of_student():
    # first letter must be capital and name length should be 3-9.
    name = choice(alphabets).upper()
    n = randint(2, 9)
    for i in range(n):
        name = name+choice(alphabets)
    return name

# id_card section


def id_card_num():
    id_card = "id-"
    for i in range(6):  # id card number lenght must be 6 digit.
        id_card = id_card+choice(digits)
    return id_card

# home town section


def home_town_name():
    home_town_of_student = choice(home_town)
    return home_town_of_student

# programming knowledge


def programming_knowledge_of_studnet():
    programm = choice(programming_knowledge)
    return programm

# call section


def get_data_of_student():
    print("Student name: ", name_of_student())
    print("id card number of studnet: ", id_card_num())
    print("home town of student: ", home_town_name())
    print("Programming knowledge:", programming_knowledge_of_studnet())


# For 36 student data:
for i in range(36):
    get_data_of_student()
    print()
