from Item import Item
from List import List
import db

importedList: list[List] = []

def removeItem(listing1: List, item: Item) -> str:    #Remove an item from the list
    for listing in importedList:
        if listing1.getName == listing.getName:
            db.deleteItem(listing,item)
            listing.removeItem(item)
            return f"Removed item from list {listing.getName}."
    return f"Error: No such item exists in this list."

def removeList(listing: List) -> str:     #Remove a List
    for i in range(len(importedList)):
        if importedList[i].getName == listing.getName:
            db.deleteList(importedList[i])
            importedList.pop(i)
            return f"Removed List {listing.getName()}"
    return f"Error: list {listing.getName} hasn't been made."
        
def addList(listing: List) -> str:    #make a new list
    for i in importedList:
        if i.getName() == listing.getName():
            return f"Error: list {listing.getName()} already Exists."
    x = db.addList(listing)
    listing.setId(x)
    importedList.append(listing)
    return f"Added the list \"{listing.getName()}\"."
    
def addItem(item: Item) -> str:    #add an item to a list
    for i in range(len(importedList)):
        if importedList[i].getId() == item.getListId():
            for j in importedList[i].getItems():
                if j.getDesc() == item.getDesc():
                    return f"Error: item already in this list."
            x = db.addItem(item)
            item.setItemId(x)
            importedList[i].addItem(item)
            return f"Added item to {[i.getName() for i in importedList if i.getId() == item.getListId()][0]}"
    return f"Error: the list for this item doesn't exist."
    
    
def editItem(listing: List,item: Item) -> str:    #Edit an item in a list
    for i in range(len(importedList)):
        if importedList[i].getId() == listing.getId():
            for item1 in importedList[i].getItems():
                if item.getDesc() == item1.getDesc():
                    db.editItem(importedList[i], item)
                    item.setItemId(item1.getItemId())
                    item1 = item
                    return "Item has been edited."
            return f"Error: Item not found in list."
    return f"Error: list not found."

def editList(listing: List) -> str:     #Edit a list
    for i in importedList:
        if i.getId() == listing.getId():
            i.setName(listing.getName())
            db.editList(i)
            return f"List's name has been changed."
    return f"Error: No such list with the name \"{listing.getName()}\"."
                
def listAllLists():
    print("----------------List of TODOs------------------")
    for i in importedList:
        print(i)
    print("-----------------------------------------------")

importedList = db.start() 
listAllLists()
print(addList(List(0,"test1")))
print(addItem(Item(0,1,"test desc1", "1/1/2024",False)))
editItem(List(1,"test1"),Item(1,1,"test desc2", "1/1/2024", True))
editList(List(1, "test2"))
removeItem(List(0,"test2"),Item(0,1,"test desc2", "1/1/2024", True))
removeList(List(0,"test2"))
listAllLists()
db.close()