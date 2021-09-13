'''
@channel ДЗ від 11.09.2021
У поточному проекті у файлі students.py :
1. Змінити функцію print_student(student) так, щоб вона виводила назви полів у людино-читаємому вигляді: кожне з великої літери, з пробілами замість "_"
2. Написати функцію print_students_list() , яка виводитиме весь список студентів (викликатиме у циклі print_student(student)
 для кожного студента та візуально відокремлюватиме вивід інформації про кожного зі студентів)
3. Результат виконання залити у свій проект на гітхабі
У LMS:
 переглянути матеріали до заняття № 10 (контестні менеджери та файли), пройти тести
Додатково:
 подивится на CSV файли , модуль у python для роботи з csv .

Мій проект на гітхабі: https://github.com/jane-at-beetroot/basics

'''

student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender']
STUDENTS = []
TEST_STUDENTS = [
    ['Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F'],
    ['John', 'S', 'new_mail@mail.com', '21', 'London', 'M'],
    ['Andy', 'H', 'more_mail@mail.com', 'sexteen', 'Brighton', 'M']
]

def add_student():
    student = {}
    for field in student_fields:
        student[field] = input('Enter {}\t'.format(field))
        if field == 'age':
            try:
                int(student['age'])
            except:
                student['age'] = input('Enter age as number\t')
    STUDENTS.append(student)
   
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

"""        
def print_student(student):
#    print(student)
    for field in student:
        print(field, '\t', student[field])
"""


def print_student(student):
    for field in student:
        print(' '.join(field.capitalize().split('_')),":", '\t', student[field])
    print('\n')

#######################################################################################

def print_students_list():
    '''Call print_student() for every student in STUDENTS'''
    for student in STUDENTS:
            print_student(student)

#    pass

#######################################################################################

def load_students():
    for test_student in TEST_STUDENTS:
        STUDENTS.append(dict(zip(student_fields, test_student)))
#    print(STUDENTS)
       
while True:
    action = input('Desired action:\t')
    if action == 'add':
        add_student()
    elif action == 'avg_age':
        calculate_avg_age()
    elif action == 'load':
        load_students()
    elif action == 'print':
       
        '''
        for student in STUDENTS:
            print_student(student)
        '''          
        print_students_list()
    else:
        break