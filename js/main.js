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
        listContainer.ondragstart = function (event) {
            event.dataTransfer.setData("text", event.target.id);
        };

        const listHeader = document.createElement('div');
        listHeader.classList.add('list-header');

        const listTitle = document.createElement('span');
        listTitle.textContent = 'List ' + listCounter;

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = function () {
            listsContainer.removeChild(listContainer);
        };

        listHeader.appendChild(listTitle);
        listHeader.appendChild(deleteButton);

        const listItems = document.createElement('ul');
        listItems.classList.add('list-items');

        const addItemContainer = document.createElement('div');
        addItemContainer.classList.add('add-item-container');

        const addItemInput = document.createElement('input');
        addItemInput.type = 'text';

        const addItemButton = document.createElement('button');
        addItemButton.textContent = 'Add Item';
        addItemButton.onclick = function () {
            addItem('list-' + listCounter);
        };

        addItemContainer.appendChild(addItemInput);
        addItemContainer.appendChild(addItemButton);

        listContainer.appendChild(listHeader);
        listContainer.appendChild(listItems);
        listContainer.appendChild(addItemContainer);

        listsContainer.appendChild(listContainer);

        listCounter++;
    }

    function addItem(listId) {
        const listItems = document.getElementById(listId).getElementsByClassName('list-items')[0];

        const listItem = document.createElement('li');
        listItem.classList.add('list-item');

        const input = document.createElement('input');
        input.type = 'text';

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