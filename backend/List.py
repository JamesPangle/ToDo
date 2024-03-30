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
        
    def removeItem(self, item: Item):
        ind = -1
        for i in range(len(self.items)):
            if item.getItemId() == self.items[i].getItemId() or item.getDesc() == self.items[i].getDesc():
                ind = i
                break
        if ind != -1:
            self.items.pop(ind)
    
    def setItem(self, items: list[Item]):
        self.items = items
        
    def toJson(self):
        return {
            "id": self.id,
            "name": self.name,
            "items": [i.toJson() for i in self.items]
        }
        
    def __str__(self) -> str:
        string = f"({self.id}){self.name}:"
        for i in self.items:
            string += f"\n\t|-> {str(i)}"
        return string
            