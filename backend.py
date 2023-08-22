from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Combobox
from sql_backend import *
# from sql_backend import *
import difflib



def showDisease():
    text_1 = Text(height = 5, width = 50)
    diseases_str = ""
    for d in predicted_diseases:
        diseases_str = diseases_str + d + "\n"
    text_1.insert(END, diseases_str)
    text_1.place(x=90,y=350)

def historyCallback(username):
    text_1 = Text(height = 5, width = 50)
    diseases_str = ""
    for d in predicted_diseases:
        diseases_str = diseases_str + d + "\n"
    text_1.insert(END, diseases_str)
    text_1.place(x=90,y=350)

def submitCallback(username, name, age, gender, blood_group, sym1, sym2, sym3):
    addUser(username, name, age, gender, blood_group)   
    getDiseaseFromSymptoms(sym1, sym2, sym3)
    showDisease()
    addDiseasesToTable(username)

def dropdown1():
    text = entry_6.get()
    if (text != ""):
        sym1_dropdown["values"] = difflib.get_close_matches(text, all_symptoms, n=10, cutoff=0.1)

def dropdown2():
    text = entry_7.get()
    if (text != ""):
        sym2_dropdown["values"] = difflib.get_close_matches(text, all_symptoms, n=10, cutoff=0.1)

def dropdown3():
    text = entry_8.get()
    if (text != ""):
        sym3_dropdown["values"] = difflib.get_close_matches(text, all_symptoms, n=10, cutoff=0.1)


window = Tk()
window.title('Disease prediction system')
window.geometry("800x800")

getAllSymptoms()

label_1 = Label(text="Username")
entry_1 = Entry(window)
label_1.place(x=90,y=60)
entry_1.place(x=200,y=60)

label_2 = Label(text="Name")
entry_2 = Entry(window)
label_2.place(x=90,y=100)
entry_2.place(x=200,y=100)

label_3 = Label(text="Age")
entry_3 = Entry(window)
label_3.place(x=90,y=140)
entry_3.place(x=200,y=140)

label_4 = Label(text="Gender")
entry_4 = StringVar()
male_4 = Radiobutton(window, text='Male', value='male', variable=entry_4, tristatevalue=0)
female_4 = Radiobutton(window, text='Female', value='female', variable=entry_4, tristatevalue=0)
label_4.place(x=90,y=180)
male_4.place(x=200,y=180)
female_4.place(x=300, y=180)

label_5 = Label(text="Blood group")
entry_5 = StringVar()
bg_options = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
bg_dropdown = Combobox(window, textvariable=entry_5, width=10, values=bg_options)
label_5.place(x=90,y=220)
bg_dropdown.place(x=200, y=220)

label_6 = Label(text="Symptom 1")
entry_6 = StringVar()
sym1_options = all_symptoms
sym1_dropdown = Combobox(window, textvariable=entry_6, width=20, values=sym1_options, postcommand=dropdown1)
label_6.place(x=90, y=260)
sym1_dropdown.place(x=90, y=280)

label_7 = Label(text="Symptom 2")
entry_7 = StringVar()
sym2_options = all_symptoms
sym2_dropdown = Combobox(window, textvariable=entry_7, width=20, values=sym2_options, postcommand=dropdown2)
label_7.place(x=290, y=260)
sym2_dropdown.place(x=290, y=280)

label_8 = Label(text="Symptom 3")
entry_8 = StringVar()
sym3_options = all_symptoms
sym3_dropdown = Combobox(window, textvariable=entry_8, width=20, values=sym3_options, postcommand=dropdown3)
label_8.place(x=490, y=260)
sym3_dropdown.place(x=490, y=280)

btn1=Button(window, text="Get History", command= lambda: historyCallback(entry_1.get()))

btn2=Button(window, text="Submit", command= lambda:
            submitCallback(entry_1.get(), entry_2.get(), entry_3.get(), entry_4.get(),
            entry_5.get(), entry_6.get(), entry_7.get(), entry_8.get()))

btn2.place(x=400, y=500)

window.mainloop()

