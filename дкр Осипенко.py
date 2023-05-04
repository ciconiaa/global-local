#Дана програма аналізує дані хроматографічного методу виявлення амінокислот та розраховує коефіцієнт розподілу на основі
#файлу .xlsx (за допомогою бібліотеки numpy та pandas) та запису в файл .txt
print("Розрахунок коефіцієнта розподілу хроматографії амінокислот")
choice1 = input('Напишіть як ви хочете ввест дані вимірювань - вручну (handle,h) або файлом (file,f)?\n')
if choice1 =='вручну' or choice1=='handle' or choice1=='h':
    F = int(input('Введіть фронт розчинника (в мм):\n'))
    AC_amount = int(input('Напишіть кількість амінокислот\n'))
    import numpy as np
    for i in range(AC_amount):

        a1 = list(map(float,input('Введіть відстані від старту до точки старту амінокислоти контрольного розчину '
                                  '(від 5 значень в мм):\n').split()))
        an = a1
        #print(len(an))
        if len(an) >= 5:
         S = (sum(a1) / len(a1))           # Розрахунок середнього значення
         #print(S)
         s = int(S)
         SE = np.std(a1, ddof=1)/np.sqrt(np.size(a1))
         # Розрахунок середньої квадратичної похибки середнього
         #print(SE)
         R = s/F                   # Розрахунок коефіцієнту розподілу
         #print(R)

         #вивід даних на основі вибору користувача
         choice2 = input(
             'Які дані ви хочете отримати - відповідність коефіцієнтів розподілу до середнього значення відстані (R:S),'
             ' середню відстань (S), стандартну похибку (SE), список введених даних (list) чи повний аналіз (all)?\n')
         #запис даних на основі вибору користувача
         choice3 = input('Чи бажаєте Ви записати дані в файл (yes or no)?\n')
         #відкриття або створення текстового файлу, куди будуть записуватися розрахунки
         record = open('хроматографія(handle).txt', 'a+', encoding='utf-8')
         # запис стандартної похибки
         if choice2 == 'SE':
             print('Стандартна похибка = ',SE)
             if choice3 == 'yes':
                 record.write('Стандартна похибка = ')
                 record.write(str(SE))
                 record.read()
         # запис середнього арифметичного
         elif choice2 == 'S':
             print('Середнє арифметичне розподілу точок амінокислоти =',S)
             if choice3 == 'yes':
                 record.write('\nСереднє арифметичне розподілу точок амінокислоти = ')
                 record.write(str(S))
                 record.read()
         elif choice2=='list':
             print('Список заданих точок амінокислоти: ',an)
             if choice3 == 'yes':
                 record.write('\nТочки розподілу амінокислоти = ')
                 record.write(str(an) + ' ')
                 record.read()
         # запис коефіцієнта розподілу
         elif choice2=='R':
             print('Коефіцієнт розподілу',R)
             if choice3 == 'yes':
                 record.write('\nКоефіцієнт розподілу = ')
                 record.write(str(R))
                 record.read()
         # запис залежності коефіцієнта розподілу до середнього значення розподілу
         elif choice2=='R:S':
             print(S,' (середнє значення розподілу) --- ',R,' (коефіцієнт розподілу)')
         #запис всіх даних
         elif choice2=='all':
             print('Список заданих точок амінокислоти: ',an)
             print('Середнє арифметичне розподілу точок амінокислоти =', S)
             print('Стандартна похибка = ', SE)
             print('Коефіцієнт розподілу', R)
             if choice3 == 'yes':
                 record.write('Точки розподілу амінокислоти = ')
                 record.write(str(an) + ' ')
                 record.write('\nСереднє арифметичне розподілу точок амінокислоти = ')
                 record.write(str(S))
                 record.write('\nСтандартна похибка = ')
                 record.write(str(SE))
                 record.write('\nКоефіцієнт розподілу = ')
                 record.write(str(R))
                 record.write('\n \n')
                 record.read()
         print('\n')
         #закриття файлу з результатами
         record.close()
        else:
            print('Ви ввели менше 5-ти значень точок плям амінокислот')


if choice1 == 'файлом' or choice1 == 'file' or choice1 == 'f':
    print('Переконайтеся, що Ви використовуєте формат файла .xlsx')
    import pandas
    file = pandas.read_excel('хроматографія.xlsx', sheet_name='Лист1') #пошук файла
    #друк таблиці:
    #print(file.values)
    f = file.iloc[5].values.tolist()
    del f[0]
    del f[1:6]
    f1 = (sum(f) / len(f))  # видалення непотрібних елементів
    print("Фронт розчинника:", f1)
    import numpy as np
    ac1 = file.iloc[0].values.tolist()                                 #виділення рядка
    #print(ac1)
    del ac1[0]   #видалення назви амінокислоти зі списку
    Sa1 = (sum(ac1) / len(ac1))
    SE1 = np.std(ac1, ddof=1) / np.sqrt(np.size(ac1))
    R1 = Sa1/f1
    #print("Перша амінокислота:",ac1)
    ac2 = file.iloc[1].values.tolist()
    del ac2[0]
    Sa2 = (sum(ac2) / len(ac2))
    SE2 = np.std(ac2, ddof=1) / np.sqrt(np.size(ac2))
    R2 = Sa2 / f1
    #print("Друга амінокислота:", ac2)
    ac3 = file.iloc[2].values.tolist()
    del ac3[0]
    Sa3 = (sum(ac3) / len(ac3))
    SE3 = np.std(ac3, ddof=1) / np.sqrt(np.size(ac3))
    R3 = Sa3 / f1
    #print("Третя амінокислота:",ac3)
    choice2 = input('Які дані ви хочете отримати - відповідність коефіцієнтів розподілу до середнього значення відстані (R:S),'
    ' середню відстань (S), стандартну похибку (SE), список введених даних (list) чи повний аналіз (all)?\n')
    choice3 = input('Чи бажаєте Ви записати дані в файл (yes or no)?\n')
    recordf = open('хроматографія(file).txt', 'a+', encoding='utf-8')
    if choice2 == 'SE':
             print('Стандартна похибка для першої АК = ',SE1)
             print('Стандартна похибка для другої АК = ', SE2)
             print('Стандартна похибка для третьої АК = ', SE3)
             if choice3 == 'yes':
                 recordf.write('Стандартна похибка для першої АК = \n')
                 recordf.write(str(SE1) + ' ')
                 recordf.write('Стандартна похибка для другої АК = \n')
                 recordf.write(str(SE2) + ' ')
                 recordf.write('Стандартна похибка для третьої АК = \n')
                 recordf.write(str(SE3) + ' ')
    elif choice2 == 'S':
             print('Середнє арифметичне розподілу точок першої амінокислоти =',Sa1)
             print('Середнє арифметичне розподілу точок другої амінокислоти =', Sa2)
             print('Середнє арифметичне розподілу точок третьої амінокислоти =', Sa3)
             if choice3 == 'yes':
                 recordf.write('Середнє арифметичне розподілу точок першої амінокислоти = \n')
                 recordf.write(str(Sa1) + ' ')
                 recordf.write('Середнє арифметичне розподілу точок першої амінокислоти = \n')
                 recordf.write(str(Sa2) + ' ')
                 recordf.write('Середнє арифметичне розподілу точок першої амінокислоти = \n')
                 recordf.write(str(Sa3) + ' ')
    elif choice2=='list':
             print("Перша амінокислота:", ac1)
             print("Друга амінокислота:", ac2)
             print("Третя амінокислота:", ac3)
             if choice3 == 'yes':
                 recordf.write('\nТочки розподілу першої амінокислоти = ')
                 recordf.write(str(ac1) + ' ')
                 recordf.write('\nТочки розподілу другої амінокислоти = ')
                 recordf.write(str(ac2) + ' ')
                 recordf.write('\nТочки розподілу третьої амінокислоти = ')
                 recordf.write(str(ac3) + ' ')
    elif choice2=='R':
             print('Коефіцієнт розподілу першої амінокислоти',R1)
             print('Коефіцієнт розподілу другої амінокислоти', R2)
             print('Коефіцієнт розподілу третьої амінокислоти', R3)
             if choice3 == 'yes':
                 recordf.write('Точки розподілу першої амінокислоти = \n')
                 recordf.write(str(ac1) + ' ')
                 recordf.write('Точки розподілу другої амінокислоти = \n')
                 recordf.write(str(ac2) + ' ')
                 recordf.write('Точки розподілу третьої амінокислоти = \n')
                 recordf.write(str(ac3) + ' ')
    elif choice2=='R:S':
             print(Sa1,' (середнє значення розподілу першої АК) --- ',R1,' (коефіцієнт розподілу)')
             print(Sa2, ' (середнє значення розподілу другої АК) --- ', R2, ' (коефіцієнт розподілу)')
             print(Sa3, ' (середнє значення розподілу третьої АК) --- ', R3, ' (коефіцієнт розподілу)')
    elif choice2=='all':
             print("Перша амінокислота:", ac1)
             print("Друга амінокислота:", ac2)
             print("Третя амінокислота:", ac3)
             print()
             print('Середнє арифметичне розподілу точок першої амінокислоти =', Sa1)
             print('Середнє арифметичне розподілу точок другої амінокислоти =', Sa2)
             print('Середнє арифметичне розподілу точок третьої амінокислоти =', Sa3)
             print()
             print('Стандартна похибка для першої АК = ', SE1)
             print('Стандартна похибка для другої АК = ', SE2)
             print('Стандартна похибка для третьої АК = ', SE3)
             print()
             print('Коефіцієнт розподілу першої амінокислоти',R1)
             print('Коефіцієнт розподілу другої амінокислоти', R2)
             print('Коефіцієнт розподілу третьої амінокислоти', R3)
             if choice3 == 'yes':
                 recordf.write('Точки розподілу першої амінокислоти = ')
                 recordf.write(str(ac1) + ' ')
                 recordf.write('\nСереднє арифметичне розподілу точок першої амінокислоти = ')
                 recordf.write(str(Sa1) + ' ')
                 recordf.write('\nСтандартна похибка для першої АК = ')
                 recordf.write(str(SE1) + ' ')
                 recordf.write('\nКоефіцієнт розподілу першої амінокислоти =')
                 recordf.write(str(R1) + '\n\n')

                 recordf.write('Точки розподілу другої амінокислоти = ')
                 recordf.write(str(ac2) + ' ')
                 recordf.write('\nСереднє арифметичне розподілу точок другої амінокислоти = ')
                 recordf.write(str(Sa2) + ' ')
                 recordf.write('\nСтандартна похибка для другої АК = ')
                 recordf.write(str(SE2) + ' ')
                 recordf.write('\nКоефіцієнт розподілу другої амінокислоти = ')
                 recordf.write(str(R2) + ' \n\n')

                 recordf.write('Точки розподілу третьої амінокислоти = ')
                 recordf.write(str(ac3) + ' ')
                 recordf.write('\nСереднє арифметичне розподілу точок третьої амінокислоти = ')
                 recordf.write(str(Sa3) + ' ')
                 recordf.write('\nСтандартна похибка для третьої АК = ')
                 recordf.write(str(SE3) + ' ')
                 recordf.write('\nКоефіцієнт розподілу третьої амінокислоти = ')
                 recordf.write(str(R3) + ' \n\n')
                 recordf.read()
    #закриття файлу з результатами
    recordf.close