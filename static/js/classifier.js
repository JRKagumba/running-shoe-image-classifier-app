var elemnt = x => document.getElementById(x);

function showPicker(inputId) { 
    elemnt('file-input').click(); 
    document.getElementById("dashed-box").style.display="none";
    document.getElementById("no-dashed-box").style.display="block";
}

function showPicked(input) {
    elemnt('upload-label').innerHTML = input.files[0].name;
    var reader = new FileReader();
    reader.onload = function (e) {
        elemnt('image-picked').src = e.target.result;
        elemnt('image-picked').className = '';
    }
    reader.readAsDataURL(input.files[0]);
}

function analyze() {
    var uploadFiles = elemnt('file-input').files;
    if (uploadFiles.length != 1) alert('Please select 1 file to analyze!');

    elemnt('analyze-button').innerHTML = 'Analyzing...';

    elemnt("loading-image").style.display ='block';
    // var xhr = new XMLHttpRequest();
    // var loc = window.location
    // xhr.open('POST', '${loc.protocol}//${loc.hostname}:${loc.port}/analyze', true);
    // xhr.onerror = function() {alert (xhr.responseText);}
    // xhr.onload = function(e) {
    //     if (this.readyState === 4) {
    //         var response = JSON.parse(e.target.responseText);
    //         elemnt('result-label').innerHTML = "Result = ${response['result']}";
    //     }
    //     elemnt('analyze-button').innerHTML = 'Analyze';
    // }

    // var fileData = new FormData();
    // fileData.append('file', uploadFiles[0]);
    // xhr.send(fileData);
}