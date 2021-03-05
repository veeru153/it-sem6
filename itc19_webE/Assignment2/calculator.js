const aNode = document.querySelector("#a");
const bNode = document.querySelector("#b");
const res = document.querySelector("#result");
const opNode = document.querySelector("#op");

function calc(op) {
    const a = parseInt(aNode.value);
    const b = parseInt(bNode.value);
    
    switch(op) {
        case "add":
            opNode.innerText = "+"
            res.innerText = (a + b);
            break;
        case "sub":
            opNode.innerText = "-"
            res.innerText = (a - b);
            break;
        case "mul":
            opNode.innerText = "×"
            res.innerText = (a * b);
            break;
        case "div":
            opNode.innerText = "÷"
            res.innerText = (a / b);
            break;
    }
}
