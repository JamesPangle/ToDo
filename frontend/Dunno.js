let listCounter = 1;

function addList() {
    const listsContainer = document.getElementById('lists-container');

    const listContainer = document.createElement('div');
    listContainer.classList.add('list');
    listContainer.setAttribute('id', 'list-' + listCounter);

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

    listContainer.appendChild(listHeader);
    listContainer.appendChild(listItems);

    listsContainer.appendChild(listContainer);

    listCounter++;
}