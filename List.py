from Item import Item


class List:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.items: list = [Item]
        
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
        
    def removeItem(self, item: Item):
        ind = 0
        for i in self.items:
            if item.getItemId == i.getItemId:
                ind = i
                break
        self.items.remove(ind)