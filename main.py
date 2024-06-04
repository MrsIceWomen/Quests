def add_quest(quests):
    while True:
        amount = input('Введите задачу: ')
        if len(amount) <= 2:
            print('Задача не может содержать меньше 2 символов!\nВведите задачу заново...')
            continue
        else:
            comment = 'В процессе:'
            quest = {'comment': comment, 'amount': amount}
            quests.append(quest)
            print('Задача добавлена.')
            break
    print()


def show_quests(quests):
    if len(quests) >= 1:
        print('Список задач:')
        number = 0
        for quest in quests:
            number += 1
            print(str(number) + ': ' + quest['comment'] + ' ' + quest['amount'] + '.')
    else:
        print('Нет актуальных задач для выполнения.')
    print()


def complete_quest(quests):
    try:
        show_quests(quests)
        number_del = int(input('Введите номер задачи, которую вы выполнили: '))
        number = number_del - 1
        quest = quests[number]
        if quest['comment'] == 'В процессе:':
            quest['comment'] = 'Завершено:'
            print('Задача помечена как выполненая.\n'
                  'Поздравляем с выполнением ваших задач!')
        else:
            print('Задача уже была выполнена!')
    except IndexError:
        print('Нет такого номера!')
    print()


def quest_del(quests):
    try:
        show_quests(quests)
        number_del = int(input('Введите номер задачи, которую хотите удалить: '))
        number = number_del - 1
        quests.remove(quests[number])
        print('Задача успешно удалена!')
    except IndexError:
        print('Нет такого номера!')
    print()


def quests_clear(quests):
    quests.clear()
    print('Список задач полностью очищен')
    print()


def download_cloud(file,quests):
    try:
        with open(file) as fin:
            len_quests = int(fin.readline().strip())
            if len_quests == 0:
                quests = []
            else:
                for i in range(len_quests):
                    comment = fin.readline().strip()
                    amount = fin.readline().strip()
                    quest = {'comment': comment, 'amount': amount}
                    quests.append(quest)
    except FileNotFoundError:
        quests = []
        return quests


def upload_cloud(file,quests):
    with open(file, 'w') as fout:
        fout.write(str(len(quests)) + '\n')
        for quest in quests:
            fout.write(str(quest['comment']) + '\n')
            fout.write(str(quest['amount']) + '\n')



def main_code():
    download_cloud('data.txt',quests)
    print('Добро пожаловать!\n')
    while True:
        try:
            print('1. Добавить задачу.\n'
                  '2. Просмотр задач.\n'
                  '3. Отметить задачу как выполненную.\n'
                  '4. Удалить задачу.\n'
                  '5. Удалить весь список задач.\n'
                  '6. Выход.\n')
            op = int(input('Введите номер операции...'))
            if op == 1:
                add_quest(quests)
                upload_cloud('data.txt', quests)
            elif op == 2:
                show_quests(quests)
            elif op == 3:
                complete_quest(quests)
                upload_cloud('data.txt', quests)
            elif op == 4:
                quest_del(quests)
                upload_cloud('data.txt', quests)
            elif op == 5:
                quests_clear(quests)
                upload_cloud('data.txt', quests)
            elif op == 6:
                print('Всего доброго!')
                break
            else:
                print('Нет такой операции!\n')
                continue
        except ValueError:
            print('Данные введены некоректно!\nВведите цифры вместо чисел...\n')


        #основной код программы
if __name__ == '__main__':
    quests = []
    main_code()
