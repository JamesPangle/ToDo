from datetime import date


class Item:
    def __init__(self,itemId: int,listId: int,desc: str,due: str = "No Due Date",completed:bool = False):
        if itemId is None:
            self.itemId = -1
        else:    
            self.itemId = itemId
        self.listId = listId
        self.desc = desc
        self.due = due
        self.completed = completed
        
    def getItemId(self) -> int:
        return self.itemId
    
    def getListId(self) -> int:
        return self.listId
    
    def getDesc(self) -> str:
        return self.desc
    
    def getDue(self) -> str:
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
        
    def toJson(self):
        return {
            "itemId":self.itemId,
            "listId":self.listId,
            "desc": self.desc,
            "due": self.due,
            "completed": self.completed
        }
        
    def __str__(self) -> str:
        if self.due == "No Due Date" or self.completed:
            return f"{self.itemId}: {self.desc} | {self.completed}"
        else:
            return f"{self.itemId}: {self.desc} | {self.completed} | Due: {self.due}"