// @ts-check

let version_number = "v0.0.1"
let whole_string = "version ".concat(version_number)

document.getElementById('version_number').innerHTML = whole_string;


let request1 = new XMLHttpRequest();
request1.open("GET", "imgs/gallery_parameters.json", false);
request1.send(null);
let chapter_of_html = "NAME_OF_CHAPTER_XYZ";
let chapter_of_example
let jsonData1 = JSON.parse(request1.responseText);
for (let key of Object.keys(jsonData1)) {
    // json: key: imagepath, values: 0 -> chapter, 1 -> code, 2-> style
    let path_of_example = key
    let chapter_of_example = jsonData1[key][0]
    let codeblock_of_example = jsonData1[key][1]
    let css_of_example = jsonData1[key][2]

    if (chapter_of_html != chapter_of_example) {
        chapter_of_html = chapter_of_example
        document.writeln(`<h1> ${chapter_of_html} </h1>`)
    }
    document.write(`<img src='imgs/${path_of_example}' data-code= '${codeblock_of_example}' onclick='display_code_from_gallery_cell(this);' class='gallery_entry' style= '${css_of_example}'>  `);
}


// add code field
// function myFunction(imgs) {
//     let name = imgs.dataset.code;
//     hljs.initHighlighting.called = false;

//     hljs.initHighlighting();
//     document.getElementById("info_field").innerHTML = name
// }