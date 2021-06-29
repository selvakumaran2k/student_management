import pandas as pd
import csv
# global data d
d=[]
# function to get in data to global variable
def data(file):
    d.clear()
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        dic={'rollNo':row['rollNo'],'name':row['name'].capitalize()}
        d.append(dic)
# function to get data out
def get_list():
    return d
def rewrite(attendence,date):
    j=0
    print(attendence)
    for i in d:
        i.update({date:attendence[j]})
        j+=1
    with open('static/filled_attendence_file.csv','w',newline="") as f:
        print('file opened')
        print('writing',d)
        wr=csv.writer(f)
        wr.writerow(['rollno','name',date])
        for i in d:
            wr.writerow(list(i.values()))



