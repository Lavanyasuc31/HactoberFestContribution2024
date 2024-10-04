document.querySelector('button').addEventListener('click', function (event) {
    event.preventDefault(); 

    const amount = document.querySelector('#amount').value;
    const type = document.querySelector('#type').value;
    const desc = document.querySelector('#description').value.trim() || 'No Description'; 
    const date = document.querySelector('#date').value;
 
    if (amount > 0 && type.length > 0 && date) {
      const container = document.querySelector('#container');

      if (container.textContent.trim() === 'No content found') {
        container.innerHTML = ''; 
      }
  
      const expenseDiv = document.createElement('div');
      expenseDiv.classList.add('expense-item'); 
  
      expenseDiv.innerHTML = `
        <strong>Amount:</strong> INR ${amount}, 
        <strong>Date:</strong> ${date}, 
        <strong>Type:</strong> ${type}, 
        <strong>Description:</strong> ${desc}
      `;
  
      const deleteButton = document.createElement('button');
      deleteButton.textContent = 'Delete';
      deleteButton.style.marginLeft = '10px';
      deleteButton.addEventListener('click', function() {
        expenseDiv.remove();
        if (container.children.length === 0) {
          container.textContent = 'No content found';
        }
      });
  
      expenseDiv.appendChild(deleteButton);
  
      container.appendChild(expenseDiv);
  
      document.querySelector('form').reset();
    } else {
      alert('Please enter a valid amount, type, and date.');
    }
  });