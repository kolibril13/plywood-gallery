// @ts-check

var version_number = "v0.0.1"
var whole_string = "version ".concat(version_number)

document.getElementById('version_number').innerHTML = whole_string;


var request1 = new XMLHttpRequest();
request1.open("GET", "imgs/gallery_parameters.json", false);
request1.send(null);
var chapter_of_html = "NAME_OF_CHAPTER";
var chapter_of_example
var jsonData1 = JSON.parse(request1.responseText);
for (let key of Object.keys(jsonData1)) {
    // json: key: imagepath, values: 0 -> chapter, 1 -> code, 2-> style
    var path_of_example = key
    var chapter_of_example = jsonData1[key][0]
    var codeblock_of_example = jsonData1[key][1]
    var css_of_example = jsonData1[key][2]

    if (chapter_of_html != chapter_of_example) {
        chapter_of_html = chapter_of_example
        document.writeln(`<h1> ${chapter_of_html} </h1>`)
    }
    document.write(`<img src='imgs/${path_of_example}' alt= '${codeblock_of_example}' onclick='myFunction(this);' class='gallery_entry' style= '${css_of_example}'>  `);
}


// add code field
function myFunction(imgs) {
    var name = imgs.alt;
    document.getElementById("info_field").innerHTML = name 
}