from typing import List, Any
from appJar import gui
file_name = 'registration3.txt'
number = 'number3.txt'

testn = []
users = {}
ents = {}
# handle button events

def press(button):
    if button == 'Очистить':
        app.stop()
    else:
        usr = app.getEntry("Фамилия")
        name = app.getEntry("Имя")
        otch = app.getEntry("Отчество")
        user = usr + ' '+ name + ' ' + otch
        users['Пациент'] = user

        pwd = app.getAllOptionBoxes()

        tel = app.getEntry("Ваш телефон")
        e_mail = app.getEntry("Ваш e-mail")
        sek = app.getEntry("Паспорт")
        ents['Телефон'] = tel
        ents['E-mail'] = e_mail
        ents['Паспорт'] = sek

        users.update(pwd)
        users.update(ents)
        testn.append(users)

        with open(file_name,'a', encoding="utf-8") as f:
            f.write(str(testn) + '\n')

# content = f.read()

        with open(file_name, 'r', encoding="utf-8") as f:
            cont = f.readlines()
            print(cont)
            l = len(cont)
            print(l)
        with open(number, 'w', encoding="utf-8") as f:
            f.write(str(l))
            print("Подберите удобное для Вас время и место!")


# create a GUI variable called app
app = gui("Галина Рыбынок ", "380x350")
app.setBg("yellow")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Добро пожаловать !!")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "yellow")

app.addLabelEntry("Фамилия")
app.addLabelEntry("Имя")
app.addLabelEntry("Отчество")
app.addLabelOptionBox("- Ваш Возраст -",["18-25","26-35","36-45","46-55+"])
app.addLabelOptionBox("- Цель Визита -", ["Консультация",
                                     "Классический массаж", "СПА", "Медитация"])
app.addLabelEntry("Ваш телефон")
app.addLabelEntry("Ваш e-mail")
app.addLabelSecretEntry("Паспорт")

# link the buttons to the function called press


app.addButtons(["Ввод", 'Очистить',], press)

app.setFocus("Фамилия")


# start the GUI
app.go()