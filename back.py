#import psycopg2
import numpy as np
new = np.array([],[])

def main():
    #   Connect to Database
    # db = psycopg2.connect(database = "todo", 
    #                     user = "killa", 
    #                    host= 'localhost',
    #                    password = "killa4eva",
    #                    port = 5432)
    # cur = db.cursor()
    cur.execute("SELECT * FROM Lists;")
    lists = cur.fetchall()
    cur.execute("SELECT * FROM Items;")
    items = cur.fetchall()
    #   Put items from database into list
    imported = np.empty((len(lists),len(lists)))
    for i in range(len(lists)):
        
    # cur.close()
    # db.close()
    
def editList(iOfList, iOfItem):
    if type(iOfList) is int:
        if type(iOfItem) is int:
            print("List is from index")
        else:
            print("List is from index, Item is unkown type")
    elif type(iOfList) is str:
        if type(iOfItem) is int:
            print("List is from index")
        else:
            print("List is from index, Item is unkown type")