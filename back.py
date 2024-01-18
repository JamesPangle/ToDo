from Item import Item
from List import List
import db

importedList: list[List] = db.start()


    
def removeItem(listing1: List, item: Item):    #Remove an item from the list
    for listing in importedList:
        if listing1.getId == listing.getId:
            db.deleteItem(listing1,item)
            listing1.removeItem(item)
            break

def removeList(listing: List):     #Remove a List
    for i in range(len(importedList)):
        if importedList[i].getId == listing.getId:
            db.deleteList(listing)
            importedList.pop(i)
            break
        
def addList(listing: List):    #make a new list
    x = db.addList(listing)
    listing.setId(x)
    importedList.append(listing)
    
def addItem(listing: List,item: Item):    #add an item to a list
    for i in range(len(importedList)):
        if importedList[i].getId == item.getListId():
            x = db.addItem(item)
            item.setItemId(x)
            importedList[i].addItem(item)
            break
    
def editItem(listing: List,item: Item):    #Edit an item in a list
    for i in range(len(importedList)):
        if importedList[i].getId == listing.getId():
            for item1 in importedList[i].getItems():
                if item.getItemId == item1.getItemId:
                    item1 = item
                    break
                