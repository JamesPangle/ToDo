let listCounter = 1;

function allowDrop(event) {
    event.preventDefault();
}

function drop(event) {
    event.preventDefault();
    const data = event.dataTransfer.getData("text");
    const draggedElement = document.getElementById(data);
    const listsContainer = document.getElementById('lists-container');
    listsContainer.appendChild(draggedElement);
}

function addList() {
    const listsContainer = document.getElementById('lists-container');
    const listContainer = document.createElement('div');
    listContainer.classList.add('list');
    listContainer.setAttribute('id', 'list-' + listCounter);
    listContainer.setAttribute('draggable', true);

    $(listContainer).draggable();

    listContainer.ondragstart = function (event) {
        event.dataTransfer.setData("text", event.target.id);
    };

    const listHeader = document.createElement('div');
    listHeader.classList.add('list-header');

    const listTitle = document.createElement('span');
    listTitle.textContent = 'List ' + listCounter;

    const renameButton = document.createElement('button');
    renameButton.textContent = 'Rename';
    renameButton.onclick = function () {
        renameList(listContainer);
    };

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.onclick = function () {
        listsContainer.removeChild(listContainer);
    };

    listHeader.appendChild(listTitle);
    listHeader.appendChild(renameButton);
    listHeader.appendChild(deleteButton);

    const listItems = document.createElement('ul');
    listItems.classList.add('list-items');

    const inputField = document.createElement('input');
    inputField.type = 'text';
    inputField.placeholder = 'Add item...';

    const addButton = document.createElement('button');
    addButton.textContent = 'Add';
    addButton.onclick = function () {
        addItem(listContainer.id, inputField.value);
        inputField.value = '';
    };

    listContainer.appendChild(listHeader);
    listContainer.appendChild(listItems);
    listContainer.appendChild(inputField);
    listContainer.appendChild(addButton);

    listsContainer.appendChild(listContainer);

    listCounter++;
}

function renameList(listContainer) {
    const listHeader = listContainer.querySelector('.list-header');
    const listTitle = listHeader.querySelector('span');
    const newName = prompt('Enter new name for the list:', listTitle.textContent);
    if (newName !== null) {
        listTitle.textContent = newName;
    }
}
function addItem(listId, itemText) {
    const listItems = document.getElementById(listId).getElementsByClassName('list-items')[0];

    const listItem = document.createElement('li');
    listItem.classList.add('list-item');
    listItem.setAttribute('draggable', true);
    listItem.ondragstart = function (event) {
        event.dataTransfer.setData("text", event.target.id);
    };

    const input = document.createElement('input');
    input.type = 'text';
    input.value = itemText;
    input.disabled = true;

    const editButton = document.createElement('button');
    editButton.textContent = 'Edit';
    editButton.onclick = function () {
        toggleEdit(itemText, input, editButton, listItem);
    };

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.onclick = function () {
        listItems.removeChild(listItem);
    };

    listItem.appendChild(input);
    listItem.appendChild(editButton);
    listItem.appendChild(deleteButton);

    listItems.appendChild(listItem);
}

function toggleEdit(itemText, input, editButton, listItem) {
    if (input.disabled) {
        input.disabled = false;
        input.focus();
        editButton.textContent = 'Save';
    } else {
        input.disabled = true;
        editButton.textContent = 'Edit';
        itemText.textContent = input.value;
        listItem.classList.toggle('completed');
    }
}

function markCompleted(listItem) {
    listItem.classList.toggle('completed');
}
