import sqlite3 as sq
from datetime import datetime
from create_bot import dp, bot, pathName
import os
from file import path
from helpers import test

dateOfWeek = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
pathName = path+'/uploads/full_shedules/';

def db_start():
    global base, cur
    base = sq.connect('db.db')
    cur = base.cursor()
    if(base):
        print('OK')
    

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO `имя таблицы` VALUES(?, ?, ?, ?)', tuple(data.values()))
        base.commit()



def subject(sem):
    arr = []
    for res in cur.execute('SELECT * FROM marks').fetchall():
        if(res[1] == sem):
            arr.append(res[2])
    arr = set(arr)
    result = list(arr)
    return result

def get_semestr():
    term = []
    for res in cur.execute('SELECT * FROM marks').fetchall():
        term.append(res[1])
    term = set(term)
    result = list(term)
    return result


async def sql_get_subjects(message):
    res = subject()
    for i in range(0, len(res)):
        await bot.send_message(message.from_user.id, res[i])


def sql_get_data(subject, semestr): 
    res = cur.execute('SELECT * FROM marks WHERE semestr=? AND name=?', (semestr, subject,)).fetchall()
    return 'exams/sem_'+res[0][1]+'/'+res[0][0]+'.docx'
    # return res[0][0] + '\n' + res[0][1]
# 
# +res[0][4]+'\n'+'На 5:'+'\n'+res[0][5]+'\n'


async def get_timetable():
    today = datetime.today()
    flag = test.diffDays()
    if(flag) :
        
        if(today.weekday() > 4):
            answer = open(pathName+'aboveline.jpg', 'rb')
            
            return answer
        else:
            answer = cur.execute('SELECT underline FROM timetable WHERE day=?', (dateOfWeek[today.weekday()],)).fetchall()
    else:
        if(today.weekday() > 4):
            answer = open(pathName+'underline.jpg', 'rb')
            return answer
        else:   
            answer = cur.execute('SELECT aboveline FROM timetable WHERE day=?', (dateOfWeek[today.weekday()],)).fetchall()
    res = '*'+dateOfWeek[today.weekday()] + ' ('+ str(today.day) + '. '+ str(today.month) + ')' + '*'+ '\n' +'\n'
    res += answer[0][0]
    return res

        