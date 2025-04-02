#создай приложение для запоминания информации
#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog
import json

notes = {
    'Добро пожаловать!':
    {
        'текст': 'Это самое лучшее приложение для заметок!',
        'теги': ['добро','инструкция']
    }
}
with open('notes_data.json', 'w') as file:
    json.dump(notes,file)

#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()
main_win.resize(800,600)
main_win.setWindowTitle('Умные заметки')
#создание виджетов главного окна
Zametki = QLabel('Список заметок')
Teg = QLabel('Список тегов')

window1 = QTextEdit()
listzamet = QListWidget()
listteg = QListWidget()
btn1 = QPushButton('Создать заметку')
btn2 = QPushButton('Удалить заметку')
btn3 = QPushButton('Сохранить заметку')
btn4 = QPushButton('Добавить к заметке')
btn5 = QPushButton('Открепить от заметки')
btn6 = QPushButton('Искать заметки по тегу')
file_tag = QLineEdit()
file_tag.setPlaceholderText('Введиет тег...')

layoutGlav = QHBoxLayout()
layout1 = QVBoxLayout()
layout2 = QVBoxLayout()
layoutzam1 = QHBoxLayout()
layoutzam2 = QHBoxLayout()
layouttag1 = QHBoxLayout()
layouttag2 = QHBoxLayout()



layout1.addWidget(window1)
layout2.addWidget(Zametki)
layout2.addWidget(listzamet)
layoutzam1.addWidget(btn1)
layoutzam1.addWidget(btn2)
layoutzam2.addWidget(btn3)
layout2.addLayout(layoutzam1)
layout2.addLayout(layoutzam2)
layout2.addWidget(Teg)
layout2.addWidget(listteg)
layout2.addWidget(file_tag)
layouttag1.addWidget(btn4)
layouttag1.addWidget(btn5)
layouttag2.addWidget(btn6)

layout2.addLayout(layouttag1)
layout2.addLayout(layouttag2)
layoutGlav.addLayout(layout1)
layoutGlav.addLayout(layout2)
main_win.setLayout(layoutGlav)

def show_note():
    respamet = listzamet.selectedItems()[0].text()
    window1.setText(notes [respamet] ['текст'])
    listteg.clear()
    listteg.addItems(notes[respamet] ['теги'])

def add_note():
    note_name, ok = QInputDialog.getText(main_win, 'Добавить заметки' , 'Название заметки')
    if ok and note_name != '':
        notes[note_name] =  {'текст' : '' ,'теги': []}
        listzamet.addItem(note_name)
        # listteg.addItems(notes[note_name]['теги'])
def del_note():
    if listzamet.selectedItems():
        text_zamet = listzamet.selectedItems()[0].text()
        del notes [text_zamet]
        window1.clear()
        listzamet.clear()
        listteg.clear()
        listzamet.addItems(notes)
        with open('notes_data.json', 'w') as file:
            json.dump(notes,file)

def save_note():
    if listzamet.selectedItems():
        text_zamet = listzamet.selectedItems()[0].text()
        notes [text_zamet] ['текст'] = window1.toPlainText()
        with open('notes_data.json', 'w') as file:
            json.dump(notes,file)
def add_tag():
    if listzamet.selectedItems():
        text_zamet = listzamet.selectedItems()[0].text()
        tag = file_tag.text()
        if not tag in notes [text_zamet] ['теги']:
            notes [text_zamet] ['теги'].append(tag)
            listteg.addItem(tag)
            file_tag.clear()
        with open('notes_data.json', 'w') as file:
            json.dump(notes,file)    

def del_tag():
    if listzamet.selectedItems():
        text_zamet = listzamet.selectedItems()[0].text()
        text_tag = listteg.selectedItems()[0].text()
        notes [text_zamet] ['теги'].remove(text_tag)
        listteg.clear()
        listteg.addItems(notes [text_zamet] ['теги'])
        with open('notes_data.json', 'w') as file:
            json.dump(notes,file) 
def search_tag():
    text_tag = file_tag.text()
    if btn6.text() == ('Искать заметки по тегу') and text_tag:
        notes_filter = {}
        for note in notes:
            if text_tag in notes [note] ['теги']:
                notes_filter [note] = notes [note]
        btn6.setText('Сбросить поиск')
        listteg.clear()
        listzamet.clear()
        listzamet.addItems(notes_filter)
    elif btn6.text() == 'Сбросить поиск':
        file_tag.clear()
        listteg.clear()
        listzamet.clear()
        listzamet.addItems(notes)
        btn6.setText('Искать заметки по тегу')

btn6.clicked.connect(search_tag)
btn5.clicked.connect(del_tag)            
btn4.clicked.connect(add_tag)
btn3.clicked.connect(save_note)         
btn2.clicked.connect(del_note)
btn1.clicked.connect(add_note)
listzamet.itemClicked.connect(show_note)
with open('notes_data.json', 'r') as file:
    notes = json.load(file)
listzamet.addItems(notes)


#отображение окна приложения
main_win.show()
app.exec()