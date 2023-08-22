import csv
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", db="disease_spv")
cursor = mydb.cursor()

with open('clean_db.csv', 'r') as csvfile:
    csv_data = csv.reader(csvfile)
    csv_headings = next(csv_data)

    for row in csv_data:
        # print(row)
        cursor.execute('INSERT INTO diseasetb (disease, \
              symptom1, symptom2, symptom3, symptom4, symptom5, symptom6 )' \
              'VALUES(%s, %s, %s, %s, %s, %s, %s)',
              row)

with open('Symptom-severity.csv', 'r') as csvfile:
    csv_data = csv.reader(csvfile)
    csv_headings = next(csv_data)

    for row in csv_data:
        cursor.execute('INSERT INTO symptomtb (symptom, weight)' \
              'VALUES(%s, %s)',
              row)

#close the connection to the database.
mydb.commit()
cursor.close()
print("Done")