from Item import Item
from List import List
import db


importedList: list[List] = []
importedList = db.start()
hasdb = False if importedList == [] else True

def removeItem(listing1: List, item: Item) -> str:    #Remove an item from the list
    for listing in importedList:
        if listing1.getName() == listing.getName():
            for i in listing.getItems():
                if i.getItemId() == item.getItemId() or i.getDesc() == item.getDesc():
                    if hasdb:
                        db.deleteItem(listing,i)
                    listing.removeItem(i)
                    return f"Removed item from {listing.getName()}."
            return f"Error: could not find \"{item.getDesc()}\" in {listing.getName()}."
    return f"Error: no such item exists in this list."

def removeList(listing: List) -> str:     #Remove a List
    for i in range(len(importedList)):
        if importedList[i].getName() == listing.getName():
            for m in importedList[i].getItems():
                if hasdb:
                    db.deleteItem(importedList[i],m)
            if hasdb:
                db.deleteList(importedList[i])
            importedList.pop(i)
            return f"Removed List {listing.getName()}"
    return f"Error: list {listing.getName()} hasn't been made."
        
def addList(listing: List) -> str:    #make a new list
    for i in importedList:
        if i.getName() == listing.getName():
            return f"Error: list {listing.getName()} already exists."
    if hasdb:
        x = db.addList(listing)
        listing.setId(x)
        importedList.append(listing)
    else:
        importedList.append(listing)
        importedList[-1].setId(len(importedList))
    
    return f"Added the list \"{listing.getName()}\"."
    
def addItem(item: Item) -> str:    #add an item to a list
    for i in range(len(importedList)):
        if importedList[i].getId() == item.getListId():
            for j in importedList[i].getItems():
                if j.getDesc() == item.getDesc():
                    return f"Error: item already in this list."
            if hasdb:    
                x = db.addItem(item)
                item.setItemId(x)
                importedList[i].addItem(item)
            else:
                importedList[i].addItem(item)
                importedList[-1].getItems()[-1].setItemId(len(importedList[-1].getItems()))
            return f"Added item to {[i.getName() for i in importedList if i.getId() == item.getListId()][0]}"
    return f"Error: the list for this item doesn't exist."
    
    
def editItem(listing: List,fro: Item, to: Item) -> str:    #Edit an item in a list
    x = 0
    tracker = -1
    #item1 = Item(-1,-1,"","",False)
    for check in importedList:
        for items in check.getItems():
            if check.getId() == to.getListId() and items.getDesc() == to.getDesc():
                return f"Error: this item is already in list {check.getName()}."
        if check.getId() == to.getListId():
            break
        elif check.getId() != to.getListId() and x >= len(importedList) - 1: 
            return f"Error: item's new list is not valid."
        x += 1
    for i in range(len(importedList)):
        if importedList[i].getName() == listing.getName() or importedList[i].getId() == listing.getId():
            for j in range(len(importedList[i].getItems())):
                item1 = importedList[i].getItems()[j]
                if fro.getItemId() == item1.getItemId() or fro.getDesc() == item1.getDesc():
                    to.setItemId(item1.getItemId())
                    item1 = to
                    tracker = i
                    break
                elif i == len(importedList) - 1:
                    return f"Error: item not found in list."
    if tracker >= 0:
        if hasdb:
            db.editItem(item1)
        importedList[tracker].removeItem(fro)
        importedList[x].addItem(to)
        return "Item has been edited."
    else:
        return f"Error: list not found."


def editList(fro: List, to: List) -> str:     #Edit a list
    for i in importedList:
        if i.getId() == to.getId() or i.getName() == to.getName():
            return f"This list already exists."
    for i in importedList:
        if i.getId() == fro.getId() or i.getName() == fro.getName():
            i.setName(to.getName())
            if hasdb:
                db.editList(i)
            return f"List's name has been changed."
    return f"Error: No such list with the name \"{fro.getName()}\"."

def getListId(name:str) -> str:
    for listing in importedList:
        if listing.getName() == name:
            return str(listing.getId())
    return f"Error: No listing named {name}."

def getAllLists() -> list[List]:
    return importedList

def getAllItems() -> list[Item]:
    listoItems = []
    for l in importedList:
        for i in l.getItems():
            listoItems.append(i)
    return listoItems
        

def listAllLists():
    print("----------------List of TODOs------------------")
    for i in importedList:
        print(i)
    print("-----------------------------------------------")