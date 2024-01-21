$(".draggable").draggable();

function addItem(draggableId) {
    var inputField = $("#" + draggableId + " input");
    var actualItem = inputField.val();

    if (actualItem.length !== 0) {
        var createAnHTMLList = `<li>${actualItem} <button onclick="removeItem(this, '${draggableId}')">Remove</button></li>`;
        var itemList = $("#" + draggableId + " ul");
        itemList.append(createAnHTMLList);
        inputField.val('');
    }
}

function removeItem(button, draggableId) {
    $(button).closest("li").remove();
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

