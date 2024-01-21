function allowDrop(event) {
  event.preventDefault();
}

function drop(event) {
  event.preventDefault();
  var data = event.dataTransfer.getData("text");
  var draggedElement = document.getElementById(data);
  event.target.appendChild(draggedElement);
}

function addList() {
  
  var listName = prompt("Enter list name:");
  if (listName) {
    var newList = document.createElement("div");
    newList.className = "list";
    newList.id = "list-" + Date.now(); // Assign a unique ID to the list
    newList.draggable = true;
    newList.ondragstart = function(event) {
      event.dataTransfer.setData("text", event.target.id);
    };

    var listTitle = document.createElement("h3");
    listTitle.textContent = listName;
    newList.appendChild(listTitle);

    var addItemButton = document.createElement("button");
    addItemButton.textContent = "Add Item";
    addItemButton.onclick = function() {
      var itemName = prompt("Enter item name:");
      if (itemName) {
        var newItem = document.createElement("div");
        newItem.textContent = itemName;
        newList.appendChild(newItem);
      }
    };

    newList.appendChild(addItemButton);

    document.getElementById("lists-container").appendChild(newList);
  }
}
var givenName = document.querySelector('#name')
var btnClass = document.querySelector('#addItem')
