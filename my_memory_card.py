from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel)

from random import randint, shuffle
class Questions():
    def __init__(self, question, rightAnswer, wrong1, wrong2, wrong3):
        self.question = question
        self.rightAnswer = rightAnswer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([])


my_win = QWidget()
my_win.setWindowTitle("Memory Card Application")
question = QLabel("what is the capital of Egypt?")
Valy = QVBoxLayout()
Valy.addWidget(question, alignment= Qt.AlignCenter)

group = QGroupBox("Answer Opions")

rbtn_1 = QRadioButton("Cario")
rbtn_2 = QRadioButton("Giza")
rbtn_3 = QRadioButton("Alex")
rbtn_4 = QRadioButton("Suez")


hlay = QHBoxLayout()
hlay_2 = QVBoxLayout()
hlay_3 = QVBoxLayout()

hlay_2.addWidget(rbtn_1)
hlay_2.addWidget(rbtn_2)

hlay_3.addWidget(rbtn_3)
hlay_3.addWidget(rbtn_4)

hlay.addLayout(hlay_2)
hlay.addLayout(hlay_3)

group.setLayout(hlay)
Valy.addWidget(group)






ansGroup = QGroupBox("Test Result!")
lbl_ans = QLabel("Correct")
hlay_4 = QHBoxLayout()
hlay_4.addWidget(lbl_ans)
ansGroup.setLayout(hlay_4)

Valy.addWidget(ansGroup)

btn2 = QPushButton("Answer")
Valy.addWidget(btn2)


ansGroup.hide()
def show_result():
    group.hide()
    ansGroup.show()
    btn2.setText("Next Question")
answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
my_win.score = 0 
def Test():
    if answer[0].isChecked():
        check_answer("correct")
        my_win.score += 1
    else:
        check_answer("incorrect")                                                                                                                                                                                                                        
        


def ask(q: Questions):
    shuffle(answer)
    answer[0].setText(q.rightAnswer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    question.setText(q.question)
    lbl_ans.setText(q.rightAnswer)
    show_question()


def check_answer(res):
    lbl_ans.setText(res)
    show_result()



def show_question():
    group.show()
    ansGroup.hide()
    btn2.setText("Answer")

questions_list = []

q1 = Questions('what is the capital of Egypt ?', 'Cario', 'Giza', 'Alex','Suez' )
q2 = Questions('who are you ?', 'Cario', 'Giza', 'Alex','Suez' )
q3 = Questions('woher kommst du ?', 'Cario', 'Giza', 'Alex','Suez' )
q4 = Questions('what is your rank ?', 'bronze', 'silver', 'enreal', 'plat')
q5 = Questions('what levl are you in blox fruits ?', 'max level', 'mid level', 'low level', 'i dont play blox fruits')
q6 = Questions('do you play minecraft ?', 'yes i play minecraft', 'no i dont play munecraft', 'what is minecraft?', 'stop talking to me plz')

questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)
questions_list.append(q5)
questions_list.append(q6)
my_win.total = 1
def next_question():
    print()
    print("total questions: ", my_win.total)
    print("corret qustion: ", my_win.score)
    print("precentage:", my_win.score/my_win.total *100, "%")
    my_win.total += 1



    current_question = randint(0, len(questions_list)-1)    
    q = questions_list[current_question] 
    ask(q)


def click_ok():
    if btn2.text() =="Answer":
        Test()
    else:
        next_question()



btn2.clicked.connect(click_ok)



my_win.setLayout(Valy)
my_win.show()
app.exec_()