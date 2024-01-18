from Item import Item
from List import List
import db

importedList: list[List] = []

def removeItem(listing1: List, item: Item) -> str:    #Remove an item from the list
    for listing in importedList:
        if listing1.getId == listing.getId:
            db.deleteItem(listing1,item)
            listing1.removeItem(item)
            return f"Removed item from list {listing.getName}."
    return f"Error: No such item exists in this list."

def removeList(listing: List) -> str:     #Remove a List
    for i in range(len(importedList)):
        if importedList[i].getId == listing.getId:
            db.deleteList(listing)
            importedList.pop(i)
            return f"Removed List {listing.getName()}"
    return f"Error: list {listing.getName} hasn't been made."
        
def addList(listing: List) -> str:    #make a new list
    for i in importedList:
        if i.getId == listing.getId:
            return f"Error: list {listing.getName()} already Exists."
    x = db.addList(listing)
    listing.setId(x)
    importedList.append(listing)
    return f"Added the list \"{listing.getName()}\"."
    
def addItem(item: Item) -> str:    #add an item to a list
    for i in range(len(importedList)):
        if importedList[i].getId() == item.getListId():
            for j in importedList[i].getItems():
                if j.getItemId() == item.getItemId():
                    return f"Error: item already in this list."
            x = db.addItem(item)
            item.setItemId(x)
            importedList[i].addItem(item)
            return f"Added item to {[i.getName() for i in importedList if i.getId() == item.getListId()]}"
    return f"Error: the list for this item doesn't exist."
    
    
def editItem(listing: List,item: Item) -> str:    #Edit an item in a list
    for i in range(len(importedList)):
        if importedList[i].getId() == listing.getId():
            for item1 in importedList[i].getItems():
                if item.getItemId() == item1.getItemId():
                    db.editItem(listing, item)
                    item1 = item
                    return "Item has been edited."
            return f"Error: Item not found in list."
    return f"Error: list not found."
                
def listAllLists():
    print("----------------List of TODOs------------------")
    for i in importedList:
        print(i)
    print("-----------------------------------------------")

importedList = db.start() 
listAllLists()
db.close()