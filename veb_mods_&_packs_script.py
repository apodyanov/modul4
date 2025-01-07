# Программа для тренировки скорости письма
# MVP minimum viable product
'''
- генерация текста
- работа с пользователем
- обработка результата
- вывод данных
- сохранение данных
'''
import pandas as pd


def gen_text(n = 5):
    import names
    l = [names.get_full_name() for i in range(n)]
    text = ', '.join(l)
    return text

def user_input(text):
    from time import time, sleep
    print('Приготовьтесь перепечатывать текст')
    sleep(1)
    for i in range(3,0,-1):
        print(i)
        sleep(1)
    start = time()
    user_text = input(text+'\n: ')
    stop = time()
    user_time = stop - start
    return int(user_time), user_text

def similarity(s1, s2):
    import difflib
    matcher = difflib.SequenceMatcher(None,s1, s2)
    return int(matcher.ratio()*100)

def output(text, sim, user_time):
    from datetime import datetime
    print(f'Ваша скорость набора текста {int(len(text)/user_time*60)} символов в минуту, а точность {sim} %')
    # сохранение данных в виде таблицы: имя/время/длина текста/точность/дата
    df = pd.read_csv('table.csv')
    df.loc[len(df)] = [input('Введите ваше имя: '), user_time, len(text), sim, datetime.today()]
    print(df)
    df.to_csv('table.csv', index=False)


text = gen_text()
user_time, user_text = user_input(text)
sim = similarity(text, user_text)
output(text, sim, user_time)

