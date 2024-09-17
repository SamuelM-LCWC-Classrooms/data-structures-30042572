def task_1(): # Lists
    origional_list = ["Geoff", "Jeff", "Jeffrey"]

    new_name = input("Enter a new name to add to the list: ")
    origional_list.insert(0, new_name)
    origional_list.remove("Jeff")
    new_list = origional_list.copy()

    return new_list

def task_2(): # Dictionaries
    keys = ("name", "age", "profession")
    values = ("Geoff", 35, "technician")
    person = dict(zip(keys, values))
    car = {
        "make": "Ford",
        "model": "Focus",
        "engine": 1.6,
        "colour": "blue"
    }
    person["car"] = car

    return person

def task_3(): # Tuples
    student_1 = ("Geoff", "Maths", 80)

    name = input("Enter the student's name: ")
    subject = input("Enter the subject: ")
    score = int(input("Enter the score out of 100: "))

    students = student_1 + (name, subject, score)

    return students

def task_4(): # Sets
    fruits_1 = {"apple", "banana", "cherry", "grape", "mango", "pineapple", "papaya", "sprite", "orange", "lemon", "strawberry"}
    fruits_2 = {"raspberry", "banana", "cherry", "grape", "mango", "blueberry", "papaya", "melon", "lemon", "steak"}

    fruits_1.discard("sprite")
    fruits_2.discard("steak")

    duplicate_fruits = fruits_1.intersection(fruits_2)
    individual_fruits = fruits_1.symmetric_difference(fruits_2)

    return [duplicate_fruits, individual_fruits]