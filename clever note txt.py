#Переменные
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import json 
#Окно
app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle('Умные заметки')
main_win.resize(750,750)

notes_win=QWidget()
#Лейауты
main_layout = QHBoxLayout()             #Основной
layout1=QVBoxLayout()                   #Левый
layout2=QVBoxLayout()                   #Правый
layout3=QHBoxLayout()                   #Правый верх
layout4=QHBoxLayout()                   #Правый низ
#Что-то
def createnote():
    note_name, result = QInputDialog.getText(notes_win, 'Добавить заметку', 'Название заметки:')
    if result == True:
        text3show.addItem(note_name)
    data[note_name] = {"текст": "", "теги": []}
    with open("notes.txt", "w", encoding='utf-8') as file:
        file.write(str(data))           
def savenote():
    global text
    if selectednotes != 0:
        text = writetext.toPlainText()
        data[selectednotes] = {"текст": text, "теги": tegos}
        if text3show.selectedItems():
            with open("notes.txt", "w", encoding='utf-8') as file:
                file.write(str(data))
def show():
    global selectedtegs
    global selectednotes
    global tegos
    global text
    text4show.clear()
    selectednotes = text3show.selectedItems()[0].text()
    tegos = data[selectednotes]['теги']
    text = data[selectednotes]['текст']
    writetext.setText(data[selectednotes]['текст'])
    text4show.addItems(data[selectednotes]['теги'])
    selectedtegs = 0
def createteg():
    if selectednotes != 0: 
        teg_name, result = QInputDialog.getText(notes_win, 'Добавить тег', 'Название тега:')
        if result == True:
            global tegos
            text4show.addItem(teg_name)
            data[selectednotes] = {"текст": text, "теги": tegos + [teg_name]}
            with open("notes.txt", "w", encoding='utf-8') as file:
                file.write(str(data))
            tegos =  data[selectednotes]['теги']
def deletenote():
    global selectednotes
    if selectednotes != 0:
        text3show.clear()
        writetext.clear()
        text4show.clear()
        data.pop(selectednotes)
        with open("notes.txt", "w", encoding='utf-8') as file:
            file.write(str(data))
        for cc in data:
            text3show.addItem(cc)
        selectednotes = 0
def deleteteg():
    global selectedtegs
    if selectedtegs != 0:
        text4show.clear()
        tegos.remove(selectedtegs)
        data[selectednotes] = {"текст": text, "теги": tegos}
        with open("notes.txt", "w", encoding='utf-8') as file:
            file.write(str(data))
        text4show.addItems(data[selectednotes]['теги'])
        selectedtegs = 0
def tegs():
    global selectedtegs
    selectedtegs = text4show.selectedItems()[0].text()
def findteg():
    global search
    if writetext2.text() != None:
        text3show.clear()
        text4show.clear()
        writetext.clear()
        search = writetext2.text()
        for cc in data:
            for tt in data[cc]['теги']:
                if tt == search:
                    text3show.addItem(cc)
    if writetext2.text() == None or writetext2.text() == '':
        text3show.clear()
        for cc in data:
            text3show.addItem(cc)
note_name = 0
result = False
add = 0
selectedtegs = 0
selectednotes = 0
search = 0
#Обьэкты
text1 = 'Список заметок'
text1show = QLabel(text1) 
text2 = 'Список тегов'
text2show = QLabel(text2)
textbutton1 = 'Создать заметку'
button1 = QPushButton(textbutton1)
textbutton2 = 'Удалить заметку'
button2 = QPushButton(textbutton2)
textbutton3 = 'Сохранить заметку'
button3 = QPushButton(textbutton3)
textbutton4 = 'Добавить к  заметке'
button4 = QPushButton(textbutton4)
textbutton5 = 'Открепить от заметки'
button5 = QPushButton(textbutton5)
textbutton6 = 'Искать заметки по тегу'
button6 = QPushButton(textbutton6)
writetext = QTextEdit()
text3show = QListWidget()
text4show = QListWidget()
writetext2 = QLineEdit()
writetext2.setPlaceholderText('Введите тег...')
#Лейауты
layout1.addWidget(writetext)

layout2.addWidget(text1show)              
layout2.addWidget(text3show)              
layout3.addWidget(button1)                
layout3.addWidget(button2)
layout2.addLayout(layout3)                  
layout2.addWidget(button3)

layout2.addWidget(text2show)               
layout2.addWidget(text4show)               
layout4.addWidget(button4)                
layout4.addWidget(button5)
layout2.addWidget(writetext2)
layout2.addLayout(layout4)                
layout2.addWidget(button6)                  

main_layout.addLayout(layout1)
main_layout.addLayout(layout2)



with open("notes.txt", "r", encoding='utf-8') as file:
    data1 = file.read()
    data = eval(data1)
    for cc in data:
        text3show.addItem(cc)


    

button1.clicked.connect(createnote)
text3show.itemClicked.connect(show)
button4.clicked.connect(createteg)
button3.clicked.connect(savenote)
button2.clicked.connect(deletenote)
button5.clicked.connect(deleteteg)
text4show.itemClicked.connect(tegs)
button6.clicked.connect(findteg)

#Запуск
main_win.setLayout(main_layout) 
main_win.show() 

app.exec_()





