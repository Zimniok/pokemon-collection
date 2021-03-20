function setCard(id, status){
  const url='http://localhost:5000/card/set/'+id+'/'+(status?1:0);
  fetch(url)
  .then(data=>{return data.json()})
}

function showCardInfo(id){
  const url='http://localhost:5000/card/id/'+id;
  fetch(url)
  .then(data=>{return data.json()})
  .then(res=>{
    var cardInfoDiv = document.getElementById("cardInfoDiv");

    if(cardInfoDiv.childNodes[0])
      cardInfoDiv.removeChild(cardInfoDiv.childNodes[0]);

    var image = document.createElement("img");
    image.src = res.images.large;
    cardInfoDiv.appendChild(image);
  })
}

function showList(res){
  var t = document.createElement("table");
  var tb = document.createElement("tbody");

  var headderRow = document.createElement("tr");
  var idCell = document.createElement("td");
  var nameCell = document.createElement("td");
  var ownCell = document.createElement("td");

  var idText = document.createTextNode("ID");
  var nameText = document.createTextNode("Name");
  var ownText = document.createTextNode("Owned");

  idCell.appendChild(idText);
  nameCell.appendChild(nameText);
  ownCell.appendChild(ownText);

  headderRow.appendChild(idCell);
  headderRow.appendChild(nameCell);
  headderRow.appendChild(ownCell);

  tb.appendChild(headderRow);

  for (var i = 0;i < res.data.length;i++){
    var id = res.data[i].id;
    var row = document.createElement("tr");

    var cell1 = document.createElement("td");
    var cell2 = document.createElement("td");
    var cell3 = document.createElement("td");

    var text = document.createTextNode(id);
    var text2 = document.createTextNode(res.data[i].name);
    var x = document.createElement("INPUT");
    x.setAttribute("type", "checkbox");
    x.checked = res.data[i].owned == 1;
    x.onclick = function() { setCard(this.parentNode.parentNode.firstChild.innerText, this.checked) };

    cell1.appendChild(text);
    cell2.appendChild(text2);
    cell3.appendChild(x);

    row.appendChild(cell1);
    row.appendChild(cell2);
    row.appendChild(cell3);
    row.onclick = function() { showCardInfo(this.childNodes[0].innerText) };

    tb.appendChild(row);
  }

  t.appendChild(tb);
  var mainTableDiv = document.getElementById("mainTableDiv");
  mainTableDiv.appendChild(t);

}
function generate_table(){
  var body = document.getElementsByTagName("body")[0];
  // creates a <table> element and a <tbody> element
   var tbl = document.createElement("table");
   var tblBody = document.createElement("tbody");


   for (var i = 0; i < 2; i++) {
     // creates a table row
     var row = document.createElement("tr");

     for (var j = 0; j < 2; j++) {
       // Create a <td> element and a text node, make the text
       // node the contents of the <td>, and put the <td> at
       // the end of the table row
       var cell = document.createElement("td");
       var cellText = document.createTextNode("cell in row "+i+", column "+j);
       cell.appendChild(cellText);
       row.appendChild(cell);
     }

     // add the row to the end of the table body
     tblBody.appendChild(row);
   }

   // put the <tbody> in the <table>
   tbl.appendChild(tblBody);
   // appends <table> into <body>
   body.appendChild(tbl);
   // sets the border attribute of tbl to 2;
   tbl.setAttribute("border", "2");
   var xD = document.getElementById("div2");
   xD.appendChild(tbl);
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
