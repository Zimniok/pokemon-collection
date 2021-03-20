var para = document.createElement("p");
var node = document.createTextNode("This is new.");
para.appendChild(node);

var element = document.getElementById("div1");
element.appendChild(para);



const url='http://localhost:5000/all_cards';
fetch(url)
.then(data=>{return data.json()})
.then(res=>{console.log(res)})
