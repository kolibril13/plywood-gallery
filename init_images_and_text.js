// @ts-check

var version_number =  "v0.0.1"
var whole_string = "version ".concat(version_number)

document.getElementById('version_number').innerHTML = whole_string;


var request1 = new XMLHttpRequest();
request1.open("GET", "imgs/plot_gallery.json", false);
request1.send(null);
var jsonData1 = JSON.parse(request1.responseText);
document.writeln(' <h1>My Plots</h1>')
for (let key of Object.keys(jsonData1)) {
    document.write(`<img src='imgs/${key}' alt= '${jsonData1[key][0]}' onclick='myFunction(this);' class='image' style= '${jsonData1[key][1]}'>  `);
}




// var request2 = new XMLHttpRequest();
// request2.open("GET", "imgs/structuring_elements.json", false);
// request2.send(null);
// var jsonData4 = JSON.parse(request2.responseText);
// document.writeln(' <h1>3D Structuring Elements</h1>')
// for (let key of Object.keys(jsonData4)) {
//     document.write(`<img src='imgs/${key}' alt= '${jsonData4[key]}' onclick='myFunction(this);' class='imagebig'> `);
// }


// add copy button to images
function myFunction(imgs) {
    var name = imgs.alt;
    // navigator.clipboard.writeText(name); # copying is disabled for now
    document.getElementById("info_field").innerHTML = name + " \n<b>is the corresponding code</b>"
}