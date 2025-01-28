import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Редактировать данные по оценкам, предметам и ученикам
        5. Удалять данные по предметам
        6. Вывод среднего балла по каждому предмету по определенному ученику
        7. Вывод оценки по каждому предмету для определенного ученика
        8. Добавить предмет
        9. Добавить оценку ученика по предмету
        10. Выход из программы
        
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('Редактировать по оценкам, предметам и ученикам')
        student=input('Введите имя ученика для редактирования оценки ')
        class_=input('Введите предмет для редактирования оценки ')
        if student in students_marks and class_ in students_marks[student]:
            print(f'Текущие оценки по предмету{class_}: {students_marks[student][class_]}')
            n=int(input('Введите индекс оценки для редактирования начиная с 0-2:'))
            if 0 <= n <len(students_marks[student][class_]):
                n1=int(input('Введите новую оценку: '))
                students_marks[student][class_][n] = n1
                print(f'Оценка изменена. Обновленные оценки: {students_marks[student][class_]}')
            else:
                print('Некорректный индекс')
        else:
            print('Данного студента или предмета в списке нет')
    elif command == 5:
        print('Удалить данные по предметам')
        end_student=input('Введите имя студента для удаления предмета: ')
        if end_student in students:
            print(students_marks[end_student])
            end_class=input('Введите предмет')
            if end_class in classes:
                print(students_marks[end_student][end_class])
                end_mark=int(input('Введите оценку'))
                if end_mark in students_marks[end_student][end_class]:
                  (students_marks[end_student][end_class]).remove(end_mark)
                  print(students_marks[end_student])
                else:
                    print('Оценки нет')
            else:
                print('Такого предмета нет')
        else:
            print('Студента нет')
    elif command == 6:
        print('Вывод среднего балла по каждому предмету для определенного студента')
        student=input('Введите имя студента ')
        if student in students_marks.keys():
             for class_ in classes:
                            marks_sum = sum(students_marks[student][class_])
                            marks_count = len(students_marks[student][class_])
                            print(f'{classes} - {marks_sum//marks_count}')
        else:
            print('Такого студента нет')
    elif command == 7:
        print(' Вывод оценки по каждому предмету для определенного студента')
        student = input('Введите имя студента: ')
        if student in students_marks:
            print(f'Оценки студента {student}:')
            for class_, marks in students_marks[student].items():
                print(f'{class_}: {marks}')
        else:
            print(f'Студента с именем {student} нет в базе данных.')
    elif command == 8:
        print('Добавить предмет')
        new_class = input('Введите название предмета, который нужно добавить: ')
        if new_class in classes:
            print('Данный предмет уже есть в списке')
        else:
            classes.append(new_class)
        print('Предмет успешно добавлен')
        print(f'Актуальный список предметов: {classes}')
    elif command == 9:
        print('Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 10:
        print(' Выход из программы')
        break