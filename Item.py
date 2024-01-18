from datetime import datetime
class Item:
    def __init__(self,itemId: int,listId: int,desc: str,due:datetime,completed: bool):
        if itemId is None:
            self.itemId = -1
        else:    
            self.itemId = itemId
        self.listId = listId
        self.desc = desc
        self.due = due
        if completed is None:
            self.completed = False
        else:
            self.completed = completed
        
    def getItemId(self) -> int:
        return self.itemId
    
    def getListId(self) -> int:
        return self.listId
    
    def getDesc(self) -> str:
        return self.desc
    
    def getDue(self) -> datetime:
        return self.due
            
    def getCompleted(self):
        return self.completed
    
    def setItemId(self,itemid):
        self.itemId = itemid
    
    def setListId(self, listid):
        self.listId = listid
    
    def setDesc(self, desc):
        self.desc = desc
    
    def setDue(self, due):
        self.due = due
            
    def setCompleted(self, comp):
        self.completed = comp