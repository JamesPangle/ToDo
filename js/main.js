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
var listOfItems = document.querySelector('#listOfItems')

dragElement(document.getElementById("mydiv"));
dragElement(document.getElementById("mydiv2"));
dragElement(document.getElementById("mydiv3"));
dragElement(document.getElementById("mydiv4"));

   function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "header")) {
    /* if present, the header is where you move the DIV from:*/
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
  } else {
    /* otherwise, move the DIV from anywhere inside the DIV:*/
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    /* stop moving when mouse button is released:*/
    document.onmouseup = null;
    document.onmousemove = null;
  }
}

