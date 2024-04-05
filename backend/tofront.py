from flask import Flask, Request, request, jsonify
from flask_cors import CORS
import back
from List import List
from Item import Item

app = Flask(__name__)
CORS(app)

@app.get("/lists")
def getLists():
    listoLists: list[List] = []
    for l in back.getAllLists():
        listoLists.append(l.toJson()) # type: ignore
    return jsonify(listoLists)
    
@app.get("/items")
def getItems():
    listoItems = []
    for i in back.getAllItems():
        listoItems.append(i.toJson())
    return jsonify(listoItems)
    
@app.route("/lists/<int:listId>", methods=["GET", "POST", "DELETE"])
def maniList(listId):                         #Need to finish
    match request.method:
        case "GET":
            for l in back.getAllLists():
                if l.getId == listId:
                    return jsonify(l.toJson())
            return []
        case "POST":
            return []
        case "DELETE":
            return []
        case _:
            return []
        
@app.route("/items/<int:itemId>", methods=["GET", "POST", "DELETE"])
def maniItem():                         #Need to finish
    match request.method:
        case "GET":
            return []
        case "POST":
            data = request.form
            return []
        case "DELETE":
            return []
        case _:
            return []
    
    
        


if __name__ == "__main__":
    app.run(debug=True)
    
    