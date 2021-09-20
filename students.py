'''

# 3 
ДЗ від 18.09.2021:
1. У проекті LMS створити класи Student (переймає всі атрибути зі словника student) 
 та  Group(список студентів та назва групи). Розділити наявні функції на методи цих двох класів.
2. Документацію по класах https://docs.python.org/3/tutorial/classes.html 
 читати/усвідомлювати до пункта 9.7 включно.
3. У Beetroot LMS опрацювати уроки 12, 13.
4. Збережіть на майбутнє посилання на офіційний 
 документ по Python MRO: https://www.python.org/download/releases/2.3/mro/


'''
import json
import csv

student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender']

STUDENTS = []

TEST_STUDENTS = [
    ['Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F'],
    ['John', 'S', 'new_mail@mail.com', '21', 'London', 'M'],
    ['Andy', 'H', 'more_mail@mail.com', 'sexteen', 'Brighton', 'M']
]

class Student:

    def __init__(self, first_name, last_name, email, age, address, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.address = address
        self.gender = gender
        
    def print_student(self):
        print(self.first_name, self.last_name, self.email, self.age, self.address, self.gender)


class Student_lis:
    stud_list = []
    
    def add_student(self, *stud):
        l = Student(*stud)
        self.stud_list.append(l)
    
    def print_stud(self):
        for student in self.stud_list:
#            print(student)
            student.print_student()

    def call_stud_list(self):
        return stud_list
        

class Group:

    def __init__(self, group_name, stud_list):
        self.group_name = group_name
        self.stud_list = stud_list


def add_student():
    ''' function that adds a new student to list STUDENTS as dictionary '''

    temp_stud = []
    for field in range(len(student_fields)):
        temp_stud.append( input('Enter {}\t'.format(student_fields[field])) )
        if field == 'age':
            try:
                int(student['age'])
            except:
                student['age'] = input('Enter age as number\t')
    global_student_class_list.add_student(*temp_stud)
#    global_student_class_list.print_stud()

   
def calculate_avg_age():

    try:
        total_age = 0
        for student in STUDENTS:
            total_age += int(student['age'])
        avgerage_age = total_age / len(STUDENTS)
        print('Average age is {}'.format(avgerage_age))
    except ValueError:
        print('Cannot calculate average age')
    except Exception as e:
        print(str(e))


#1.1. Змінити функцію print_student(student) так,
# щоб вона виводила назви полів у людино-читаємому вигляді:
# кожне з великої літери, з пробілами замість "_"

def print_student(student):
    for field in student:
        print(' '.join(field.capitalize().split('_')),":", '\t', student[field])
    print('\n')


#1.2. Написати функцію print_students_list() , 
# яка виводитиме весь список студентів 
# (викликатиме у циклі print_student(student)
# для кожного студента та візуально відокремлюватиме
# вивід інформації про кожного зі студентів)

def print_students_list():
    '''Call print_student() for every student in STUDENTS'''
    global_student_class_list.print_stud()
    print(global_student_class_list)
#    for student in global_student_class_list:
        

def load_students():
    
    for test_student in TEST_STUDENTS:
        global_student_class_list.add_student(*test_student)


def dump_studens():
    ''' function that save all students as dict into file JSON stored/created in "data" folder  '''
    with open('data\\student_data.json', 'w') as file:
        json.dump(STUDENTS, file)


def dump_csv():
    ''' function that save all students as dict into file CSV stored/created in "data" folder  '''
    with open('data\\student_data.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=student_fields)
        writer.writeheader()
        for student in STUDENTS:
            writer.writerow(student)


def load_from_json(file_path='data\\student_data.json'):
    ''' function that load all students as dict from file JSON stored in "data" folder '''
    with open(file_path, 'r') as read_file:
        STUDENTS.extend(json.load(read_file))


# 2.2. закінчити функцію, яка виконує
# завантаження даних з файлу у форматі CSV.

def load_csv(file_path='data\\student_data.csv'):
    ''' function that load all students as dict from file CSV stored in "data" folder '''
    with open(file_path, 'r') as read_file:
        reader = csv.DictReader(read_file)
        for row in reader:
            STUDENTS.append(row)





ACTIONS = {
    'add': add_student,
    'avg_age': calculate_avg_age,
    'load': load_students,
    'print': print_students_list,
    'dump': dump_studens,
    'dump_csv': dump_csv,
    'load_json': load_from_json,
    'load_csv': load_csv
}

if __name__ == '__main__':
    global_student_class_list = Student_lis()
    while True:
        action = input('Desired action:\t')
        if action in ACTIONS:
            ACTIONS.get(action)()
        else:
            break

