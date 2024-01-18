from Item import Item


class List:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.items: list[Item] = []
        
    def getId(self) -> int:
        return self.id
            
    def getName(self) -> str:
        return self.name
    
    def getItems(self):
        return self.items
    
    def setId(self, id):
        self.id = id
        
    def setName(self, name):
        self.name = name
        
    def addItem(self, item: Item):
        self.items.append(item)
        print(f"Added an item to {self.getName}.\n")
        
    def removeItem(self, item: Item):
        ind = -1
        for i in range(len(self.items)):
            if item.getItemId() == self.items[i].getItemId():
                ind = i
                break
        if ind != -1:
            self.items.pop(ind)
            print(f"Removed an item from {self.getName}.\n")
    
    def setItem(self, items: list[Item]):
        self.items = items
            