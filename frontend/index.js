function showList(res){
  for (var i = 0;i < res.data.length;i++){
    document.getElementById('div1').appendChild(document.createElement("div").appendChild(document.createTextNode('id: ' + res.data[i].id + ' name: '+ res.data[i].name+'\r\n')))
  } 
}
var para = document.createElement("p");
var node = document.createTextNode("This is new.");
para.appendChild(node);

var element = document.getElementById("div1");
element.appendChild(para);



const url='http://localhost:5000/all_cards';
fetch(url)
.then(data=>{return data.json()})
.then(res=>{showList(res)})

