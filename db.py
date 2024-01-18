import psycopg2 as psy
from Item import Item
from List import List

def start() -> list:    #  Connect to Database
    global db
    db = psy.connect(database = "todo", 
                        user = "killa", 
                       host= 'localhost',
                       password = "killa4eva",
                       port = 5432)
    global cur
    cur = db.cursor()
    cur.execute("SELECT * FROM Lists;")
    importedList = cur.fetchall()
    cur.execute("SELECT * FROM Items;")
    importedItems = cur.fetchall()
                                    #Put items from database into list
    global combined
    combined = []
    for i in importedList:
        combined.append((i[0],i[1],[list for list in importedItems if importedItems[1] == i[0]]))
    return combined
def addItem(item: Item) -> int:          #Add an Item to the database
    cur.execute("INSERT INTO Items(list_id,description,due_date,completed) VALUES (%s,%s,%s,%s) RETURNING item_id;",(item.getListId,item.getDesc, item.getDue, item.getCompleted))
    out = cur.fetchall()[0][0]
    return out
def addList(listing: List) -> int:          #Add a List to the database
    cur.execute("INSERT INTO Lists(list_name) VALUES (%s) RETURNING list_id;",(listing.getName()))
    out = cur.fetchall()[0][0]
    return out
def deleteList(listing: List) -> None:   #Delete a List from the database
    cur.execute("DELETE from Lists WHERE list_id = %s;",str(listing.getId()))
def deleteItem(item: Item) -> None:   #Delete an Item from the database
    cur.execute("DELETE from Items WHERE item_id = %s;",str(item.getItemId()))
def editList(listing: List) -> None:     #Edit a List from the database
    cur.execute("UPDATE Lists SET list_name = %s WHERE listing_id = %s;",(listing.getName(),listing.getId()))
def editItem(item: Item) -> None:     #Edit an  Item from the database
    cur.execute("UPDATE Items SET list_id = %s,description = %s,due_date = %s,completed = %s WHERE item_id = %s;", (item.getListId(),item.getDesc(),item.getDue(),item.getCompleted(), item.getItemId))
def close() -> None:    #Close the database
    cur.close()
    db.close()
    