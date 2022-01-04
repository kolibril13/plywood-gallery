// @ts-check

let version_number = "v0.0.1"
let whole_string = "version ".concat(version_number)

document.getElementById('version_number').innerHTML = whole_string;


let request1 = new XMLHttpRequest();
request1.open("GET", "imgs/gallery_parametersX.json", false);
request1.send(null);

let jsonData1 = JSON.parse(request1.responseText);

// json: key: imagepath, values: 0 -> chapter, 1 -> code, 2-> style
// let path_of_example = key
// // let chapter_of_example = jsonData1[key][0]
// let codeblock_of_example = jsonData1[key][1]
// let css_of_example = jsonData1[key][2]


for (let key of Object.keys(jsonData1)) {
    let chapter_of_html = key
    document.writeln(`<h1> ${chapter_of_html} </h1>`)

    let chapter_content = jsonData1[key]
    for (const entery of chapter_content) {
        let element_dict= entery[0]
        let path_of_example = element_dict["image"]
        let codeblock_of_example = element_dict["code"]
        let css_of_example = element_dict["css"]
        document.write(`<img src='imgs/${path_of_example}' data-code= '${codeblock_of_example}' onclick='display_code_from_gallery_cell(this);' class='gallery_entry' style= '${css_of_example}'>  `);

    }

}



// 
// }


// add code field
// function myFunction(imgs) {
//     let name = imgs.dataset.code;
//     hljs.initHighlighting.called = false;

//     hljs.initHighlighting();
//     document.getElementById("info_field").innerHTML = name
// }