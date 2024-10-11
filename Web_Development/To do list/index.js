let btn=document.querySelector('button');
let input=document.querySelector('input');
let todos=document.querySelector('.list-tasks');
function addTodo(){
    let task=input.value;
    if(task){
        let todo=document.createElement('div');
        let text=document.createElement('span');
        text.innerHTML=task;
        todo.appendChild(text);
        let close=document.createElement('span');
        close.innerHTML='&times;';
        close.classList.add('delete');
        close.addEventListener('click',(e)=>{
            e.preventDefault();
            todos.removeChild(todo);
        });
        todo.appendChild(close);
        todo.classList.add('todo');
        if (todos.firstChild) {
            todos.insertBefore(todo, todos.firstChild);
        } else {
            todos.appendChild(todo);
        }
        input.value='';
    }
}
btn.addEventListener('click',(e)=>{
    e.preventDefault();
    addTodo();
})

input.addEventListener('keypress',(e)=>{
    if(e.key==='Enter'){
        e.preventDefault();
        addTodo();
    }
})