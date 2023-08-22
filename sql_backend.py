import csv
import mysql.connector
import tkinter.messagebox

predicted_diseases = ["NULL", "NULL", "NULL"]
all_symptoms = []

def getDiseaseFromSymptoms(sym1, sym2, sym3):
    db = mysql.connector.connect(host="localhost", user="root", passwd="1234", db="disease_spv")
    cur = db.cursor()
    query = "SELECT disease FROM diseasetb\
    WHERE %s IN (symptom1, symptom2, symptom3) \
    AND %s IN (symptom1, symptom2, symptom3) \
    AND %s IN (symptom1, symptom2, symptom3)"

    args = (sym1, sym2, sym3)
    cur.execute(query, args)
    myDiseases = cur.fetchall()
    for index in range(len(myDiseases)):
        predicted_diseases[index] = myDiseases[index][0]
    cur.close()
    db.close()


def addUser(username, name, age, gender, blood_group):
    db = mysql.connector.connect(host="localhost", user="root", passwd="pavitra", db="disease_spv")
    cur = db.cursor()
    query = 'INSERT INTO user_history(username, name, age, gender, blood_group)' \
        'VALUES(%s, %s, %s, %s, %s)'
    args = (username, name, age, gender, blood_group)
    cur.execute(query, args)
    db.commit()
    cur.close()
    db.close()

def getAllSymptoms():
    db = mysql.connector.connect(host="localhost", user="root", passwd="pavitra", db="disease_spv")
    cur = db.cursor()
    query = "SELECT symptom FROM symptomtb"
    cur.execute(query)
    mySymptoms = cur.fetchall()
    for s in mySymptoms:
        all_symptoms.append(s[0])
    cur.close()
    db.close()

def addDiseasesToTable(username):
    db = mysql.connector.connect(host="localhost", user="root", passwd="pavitra", db="disease_spv")
    cur = db.cursor()

    query = "UPDATE user_history \
        SET pre_disease1 = %s, \
        pre_disease2 = %s, \
        pre_disease3 = %s \
        WHERE username = %s"
    args = (predicted_diseases[0], predicted_diseases[1], predicted_diseases[2], username)
    cur.execute(query, args)
    db.commit()
    cur.close()
    db.close()





