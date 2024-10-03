const inputBox = document.getElementById("input-box") 
// Selects the input box where the user enters the task.

const listContainer = document.getElementById("list-container") 
// Selects the container where tasks will be listed (likely a <ul> or <ol>).

const totalTasks = document.querySelector('#total-tasks') 
// Selects the element that displays the total number of tasks.

const completedTasks = document.querySelector('#completed-tasks') 
// Selects the element that displays the number of completed tasks.

const remainingTasks = document.querySelector('#remaining-tasks') 
// Selects the element that displays the remaining tasks to complete.

function addTask(){
    if(inputBox.value === ''){
        alert("you must write something") 
        // If the input box is empty, an alert pops up to notify the user.
    }
    else{
        let li = document.createElement("li") 
        // Creates a new <li> element for the task.

        li.classList = 'unchecked' 
        // Adds the 'unchecked' class to the newly created task.

        li.innerHTML = inputBox.value; 
        // Sets the inner HTML of the <li> to the value entered in the input box.

        listContainer.appendChild(li) 
        // Appends the newly created <li> to the task list container.

        let span = document.createElement('span') 
        // Creates a <span> element for the delete (×) button.

        span.innerHTML = "\u00d7"; 
        // Sets the <span>'s content to the "×" character for deleting the task.

        li.appendChild(span); 
        // Appends the <span> (delete button) to the <li> (task).
    }

    inputBox.value = ""; 
    // Clears the input box after a task is added.

    saveData() 
    // Calls the function to save the current task list to localStorage.

    countTasks() 
    // Calls the function to update task counters (total, completed, remaining).
}

document.getElementById('input-box').addEventListener('keydown', (e) =>{
    if(e.key === 'Enter') {
        document.getElementById('addt').click(); 
        // If the "Enter" key is pressed, it triggers the "add" button.
    }
})

function countTasks(){
    const completedTasksArray = [] 
    // Creates an empty array (not really used, could be omitted).

    let liChecked = document.getElementsByClassName('checked') 
    // Selects all the tasks that are marked as checked (completed).

    let liUnchecked = document.getElementsByClassName('unchecked') 
    // Selects all the tasks that are not checked (incomplete).

    completedTasks.textContent = liChecked.length; 
    // Updates the displayed count of completed tasks.

    totalTasks.textContent = liUnchecked.length; 
    // Updates the displayed count of total tasks (seems incorrect as this counts only unchecked tasks).

    remainingTasks.textContent = liUnchecked.length - liChecked.length 
    // Calculates and updates the number of remaining tasks to complete.

    saveData() 
    // Saves the updated data to localStorage.
}

listContainer.addEventListener("click", (e) => {
    if(e.target.tagName === "LI"){
        e.target.classList.toggle("checked"); 
        // Toggles the 'checked' class on the clicked task (marks it as complete/incomplete).

        saveData() 
        // Saves the updated task status to localStorage.

        countTasks() 
        // Updates the task counters after a task is checked/unchecked.
    }
    else if(e.target.tagName === "SPAN"){
        e.target.parentElement.remove(); 
        // If the delete button (×) is clicked, it removes the corresponding task.

        saveData() 
        // Saves the updated task list after the task is deleted.

        countTasks() 
        // Updates the task counters after a task is deleted.
    }
}, false);

function saveData(){
    localStorage.setItem("data", listContainer.innerHTML); 
    // Saves the current state of the task list to localStorage by storing its innerHTML.
}

function showTask(){
    listContainer.innerHTML = localStorage.getItem("data") 
    // Retrieves the stored task list from localStorage and displays it in the list container.

    countTasks() 
    // Updates the task counters when the stored task list is loaded.
}

showTask() 
// Calls the showTask function when the page loads to display the previously saved tasks.
