import csv

def check(regno):
    with open('validregnos.csv',newline='') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0]==regno):
                return True
        return False
                
def name(regno):
    with open('validregnos.csv',newline='') as file:
        reader=csv.reader(file)
        for row in reader:
            if(row[0]==regno):
                print("Success")
                return row[1]
        return 'NotFound'