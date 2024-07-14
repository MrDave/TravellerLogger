// get the elements
const editButton = document.getElementById('edit-button');
const wareList = document.getElementById('ware-list');
const wareForm = document.getElementById('ware-form');
const cancelButton = document.getElementById('cancel-button');

// add event listener to edit button
editButton.addEventListener('click', () => {
  // hide initial element and show swap element
  editButton.style.display = 'none';
  wareList.style.display = 'none';
  wareForm.style.display = 'block';
  cancelButton.style.display = 'block';
});

// add event listener to cancel button
cancelButton.addEventListener('click', () => {
  // hide swap element and show initial element
  wareForm.style.display = 'none';
  wareList.style.display = 'block';
  cancelButton.style.display = 'none';
  editButton.style.display = 'block';
});