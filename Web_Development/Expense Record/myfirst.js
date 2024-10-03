const but = document.querySelector('button');
const bod = document.querySelector('body');
let count = 0;
but.addEventListener('click',function ()
{
    event.preventDefault()
    const inr = document.querySelector('#amount').value;
    const type = document.querySelector('#type').value;
    const desc = document.querySelector('#decription').value;
    let dat = document.querySelector('#date').value
    if(inr>=0 && type.length>0)
    {
        const newElement = `<div>Amount = ${inr}, Date = ${dat}, Type: ${type}, Description: ${desc}</div>`;
        if(count == 0)
        {
            document.querySelector('#container').innerHTML = newElement;
            count++;
        }
        else
        {
            document.querySelector('#container').innerHTML += newElement;
            count++;
        }
        const formm = document.querySelector('form');
        formm.reset();
    }
    else
    {
        alert('Invalid Number or empty type');
    }
});

