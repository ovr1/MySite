from typing import List, Any
from appJar import gui
file_name = 'registration3.txt'
file_name2 = 'number.txt'

testn = []
ents = {}
# handle button events

def press(button):
    if button == 'Очистить':
        app.stop()
    else:
        e_mail = app.getEntry("Ваш e-mail")
        sek = app.getEntry("Паспорт")
        ents['E-mail'] = e_mail
        ents['Паспорт'] = sek
        inf = app.getAllOptionBoxes()
        ents.update(inf)
        testn.append(ents)

        with open(file_name2, 'a', encoding="utf-8") as f:
            f.write(str(testn)+'\n')

# content = f.read()
        with open(file_name2, 'r', encoding='utf-8') as f:
            contents = f.read()
            print(contents)
            if e_mail and sek in contents:
                ...
            else:
                print("Вы ещё не зарегистрировались. Зарегистрируйтесь пожалуйста. ")

# create a GUI variable called app
app = gui("Галина Рыбынок", "378x265")
app.setBg("yellow")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Добро пожаловать !!")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "yellow")

app.addLabelEntry("Ваш e-mail")
app.addLabelSecretEntry("Паспорт")
app.addLabelOptionBox("-Месяц-",["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"])
app.addLabelOptionBox("-Дата-",["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"])
app.addLabelOptionBox("-Время-",["10-12", "12-14", "14-16", "16-18", "18-20", "20-22"])
app.addLabelOptionBox("-Место-",["Полянка", "Тверская", "Митино"])

# link the buttons to the function called press


app.addButtons(["Отправить", 'Очистить',], press)



# start the GUI
app.go()