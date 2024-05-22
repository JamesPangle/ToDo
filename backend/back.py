from Item import Item
from List import List
import db


importedList: list[List] = []
importedList = db.start()
hasdb = False if importedList == [] else True

def removeItem(id: int) -> str:    #Remove an item from the list
    for listing in importedList:
        for i in listing.getItems():
            if i.getItemId() == id:
                if hasdb:
                    db.deleteItem(listing,i)
                listing.removeItem(i.getItemId())
                return f"Removed {i.getDesc()} from {listing.getName()}."
    return f"Error: no such item exists."

def removeList(id: int) -> str:     #Remove a List
    for i in range(len(importedList)):
        if importedList[i].getId() == id:
            for m in importedList[i].getItems():
                if hasdb:
                    db.deleteItem(importedList[i],m)
            if hasdb:
                db.deleteList(importedList[i])
                nameee = importedList[i].getName()
            importedList.pop(i)
            return f"Removed List \"{nameee}\"."
    return f"Error: no such list exists."
        
def addList(name: str) -> str:    #make a new list
    listing = List(-1,name)
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
    
def addItem(lId:int,desc:str, due:str, comp:bool = False) -> str:    #add an item to a list
    if due == "":
        due = "No Due Date"
    item = Item(-1,lId,desc,due,comp)
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
                importedList[i].getItems()[-1].setItemId(len(getAllItems()))
            return f"Added item to {[i.getName() for i in importedList if i.getId() == item.getListId()][0]}"
    return f"Error: the list for this item doesn't exist."
    
    
def editItem(id:int, to: Item) -> str:    #Edit an item in a list
    x = 0
    y = 0
    tracker = 0
    found = False
    check4List = False
    for g in importedList:
        if g.getId() == to.getListId():
            check4List = True
            break
    if not check4List:
        return "Error: new item's list doesn't exist."
    
    for check in importedList:
        for item in check.getItems():
            if item.getItemId() == id:
                to.setItemId(id)
                found = True
                break
            else:
                x+=1
        if found:
            break
        else:
            tracker += 1
            x=0
    before = importedList[tracker].getItems()[x]
    if before.getListId() != to.getListId():
        for w in importedList:
            if w.getId() == to.getListId():
                break
            else:
                y+= 1
    else:
        y = tracker
    if hasdb:
        db.editItem(to)
    importedList[tracker].removeItem(before.getItemId())
    importedList[y].addItem(to)
    return "Item has been edited."

def getList(id: int) -> List:
    for l in importedList:
        if l.getId() == id:
            return l
    return List(-1,"")

def getItem(id: int) -> Item:
    for l in getAllItems():
        if l.getItemId() == id:
            return l
    return Item(-1,-1,"")

def editList(id: int, to: str) -> str:     #Edit a list
    for i in importedList:
        if i.getName() == to:
            return f"This list already exists."
    for i in importedList:
        if id == i.getId():
            i.setName(to)
            if hasdb:
                db.editList(i)
            return f"{getList(id).getName()} has been Modified."
    return f"Error: No such list with the ID \"{id}\"."

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

if __name__ == "__main__":
    inp = int(input(f"1:Add Item\n2:Add List\n3:Edit Item\n4:Edit List\n5:Remove Item\n6:Remove List\n7:Show All\n8:Quit\n"))
    while(inp != 8):
        match(inp):
            case(1):
                listAllLists()
                iName = str(input("Item Name?\n"))
                iList = int(input("List Id?\n"))
                iDue = str(input("Due Date? MM/DD/YYYY or just press enter if no due date.\n"))
                iComp = bool(input("Completed Already? True/False\n"))
                print(addItem(iList,iName,iDue,iComp))
            case(2):
                listAllLists()
                lName = str(input("List Name?\n"))
                print(addList(lName))
            case(3):
                listAllLists()
                id = int(input("ID of Item you want to edit?\n"))
                if getItem(id).getItemId() == -1:
                    print("No Such Item.\n")
                else:
                    orig = getItem(id)
                    iItem = Item(orig.getItemId(),orig.getListId(),orig.getDesc(),orig.getDue(),orig.getCompleted())
                    print(iItem)
                    print("What do you want to edit within this item?\n")
                    choice = int(input("1:Change List Its In\n2:Change Name\n3:Change Due Date\n4:Change Completion Status\n"))
                    match(choice):
                        case(1):
                            listAllLists()
                            iList = int(input("What List ID Would You Like To Put It Into?\n"))
                            iItem.setListId(iList)
                            print(editItem(iItem.getItemId(),iItem))
                                    
                        case(2):
                            iItem.setDesc(str(input("What Would You Like The Name To Be?")))
                            print(editItem(iItem.getItemId(),iItem))
                                    
                        case(3):
                            iItem.setDue(str(input("What Would You Like The Due Date To Be? MM/DD/YYYY")))
                            print(editItem(iItem.getItemId(), iItem))
                        case(4):
                            iItem.setCompleted(bool(input("Completed? True/False")))
                            print(editItem(iItem.getItemId(),iItem))
            case(4):
                listAllLists()
                ichoice = int(input("Which List ID Would You Like To Edit?\n"))
                print(editList(ichoice,(str(input("What Would You Like To Set The Name To?\n")))))
            case(5):
                listAllLists()
                print(removeItem(int(input("What Item ID Would You Like To Remove?\n"))))
            case(6):
                listAllLists()
                print(removeList(int(input("What List ID Would You Like To Remove?\n"))))
            case(7):
                listAllLists()
            case(8):
                print("Quitting...")
            case _:
                print("Invalid option. Try Again.")
        try:
            inp = int(input(f"1:Add Item\n2:Add List\n3:Edit Item\n4:Edit List\n5:Remove Item\n6:Remove List\n7:Show All\n8:Quit\n"))
        except:
            inp = ""
            print("Wrong Input. Please Try Again.")
            while not inp in [1,2,3,4,5,6,7,8]:
                try:
                    inp = int(input(f"1:Add Item\n2:Add List\n3:Edit Item\n4:Edit List\n5:Remove Item\n6:Remove List\n7:Show All\n8:Quit\n"))
                except:
                    inp = ""
                    print("Wrong Input. Please Try Again.")
            
        