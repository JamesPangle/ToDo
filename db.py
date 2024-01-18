import psycopg2 as psy
from Item import Item
from List import List

def start() -> list:    #  Connect to Database
    global db
    db = psy.connect(database = "todo", 
                        user = "postgres", 
                       host= 'localhost',
                       password = "killa4eva",
                       port = 5432)
    global cur
    combined:list[List] = []
    cur = db.cursor()
    
                                    #Put items from database into list
    cur.execute("SELECT * FROM Lists;")
    importedList = cur.fetchall()
    for listing in importedList:
        combined.append(List(listing[0],listing[1]))
    cur.execute("SELECT * FROM Items;")
    importedItems = cur.fetchall()
    for item in importedItems:
        for listing in combined:
            if item[1] == listing.getId():
                listing.addItem(Item(item[0], item[1], item[2], item[3], item[4]))
    return combined
def addItem(item: Item) -> int:          #Add an Item to the database
    cur.execute("INSERT INTO Items(id,desc,due,completed) VALUES (%s,%s,%s,%s) RETURNING id;",(item.getListId,item.getDesc, item.getDue, item.getCompleted))
    out = cur.fetchall()[0][0]
    return out

def addList(listing: List) -> int:          #Add a List to the database
    cur.execute("INSERT INTO Lists(name) VALUES (%s) RETURNING id;",(listing.getName()))
    out = cur.fetchall()[0][0]
    return out

def deleteList(listing: List) -> None:   #Delete a List from the database
    cur.execute("DELETE from Lists WHERE id = %s;",str(listing.getId()))
    
def deleteItem(listing:List, item: Item) -> None:   #Delete an Item from the database
    cur.execute("DELETE from Items WHERE id = %s AND list_id = %s;",(str(item.getItemId()), str(item.getListId())))
    
def editList(listing: List) -> None:     #Edit a List from the database
    cur.execute("UPDATE Lists SET name = %s WHERE id = %s;",(listing.getName(),listing.getId()))
    
def editItem(listing:List, item: Item) -> None:     #Edit an  Item from the database
    cur.execute("UPDATE Items SET list_id = %s,descr = %s,due = %s,completed = %s WHERE id = %s AND list_id = %s;", (item.getListId(),item.getDesc(),item.getDue(),item.getCompleted(), item.getItemId, item.getListId))
    
def close() -> None:    #Close the database
    cur.close()
    db.close()
    