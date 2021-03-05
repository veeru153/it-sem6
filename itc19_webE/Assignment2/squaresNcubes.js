const list = document.querySelector('#list');


window.addEventListener('load', () => {
    for(let i = 1; i < 20; i++) {
        const row = document.createElement('tr');
    
        const numCell = document.createElement('td');
        numCell.innerText = i;
        row.appendChild(numCell);
        
        const sqCell = document.createElement('td');
        sqCell.innerText = i*i;
        row.appendChild(sqCell);
        
        const cuCell = document.createElement('td');
        cuCell.innerText = i*i*i;
        row.appendChild(cuCell);
    
        list.appendChild(row);
    }
})