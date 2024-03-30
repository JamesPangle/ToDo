from Item import Item
from List import List
import db

importedList: list[List] = []

def removeItem(listing1: List, item: Item) -> str:    #Remove an item from the list
    for listing in importedList:
        if listing1.getName() == listing.getName():
            for i in listing.getItems():
                if i.getItemId() == item.getItemId() or i.getDesc() == item.getDesc():
                    db.deleteItem(listing,i)
                    listing.removeItem(i)
                    return f"Removed item from {listing.getName()}."
            return f"Error: could not find \"{item.getDesc()}\" in {listing.getName()}."
    return f"Error: no such item exists in this list."

def removeList(listing: List) -> str:     #Remove a List
    for i in range(len(importedList)):
        if importedList[i].getName() == listing.getName():
            for m in importedList[i].getItems():
                db.deleteItem(importedList[i],m)
            db.deleteList(importedList[i])
            importedList.pop(i)
            return f"Removed List {listing.getName()}"
    return f"Error: list {listing.getName()} hasn't been made."
        
def addList(listing: List) -> str:    #make a new list
    for i in importedList:
        if i.getName() == listing.getName():
            return f"Error: list {listing.getName()} already exists."
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
            db.editList(i)
            return f"List's name has been changed."
    return f"Error: No such list with the name \"{fro.getName()}\"."

def getListId(name:str) -> str:
    for listing in importedList:
        if listing.getName() == name:
            return str(listing.getId())
    return f"Error: No listing named {name}."

def listAllLists():
    print("----------------List of TODOs------------------")
    for i in importedList:
        print(i)
    print("-----------------------------------------------")

importedList = db.start() 
listAllLists()
print(addList(List(0, "test1")))
print(addItem(Item(0,int(getListId("test1")),"test desc1", "1/1/2024",False)))
listAllLists()
print(editItem(List(0, "test1"),Item(0,int(getListId("test1")),"test desc1", "", True), Item(0,int(getListId("test1")),"test desc2", "1/1/2024", True)))
print(editList(List(0, "test1"), List(0, "test2")))
listAllLists()
print(removeItem(List(0, "test2"),Item(0,int(getListId("test2")),"test desc2", "1/1/2024", True)))
listAllLists()
print(removeList(List(0, "test2")))
listAllLists()
db.close()