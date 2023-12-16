
document.addEventListener('DOMContentLoaded', function() {
    var btn = document.getElementById("searchBtn");
    // onClick's logic below:
    btn.addEventListener('click', function() {
        fetchData();
    });
});


function fetchData() {
    
    var seachText = document.getElementById("searchText").value;
    if (seachText.length < 1)
    {
        window.alert("Field is blank");
        return false;
    }
    
    runPyScript(seachText);
    
}

async function runPyScript(query) {
    
    let url = 'http://127.0.0.1:5000/jsPythonCall';
    let response = await fetch(url, {
        method: "POST",
        body: JSON.stringify(query),
        headers: {"Content-type": "application/json; charset=UTF-8"}});

    let allURLs = await response.text(); // read response body and parse as JSON
    
    //document.getElementById("courseraLinks1").innerHTML= courseraURLs;

    var courseraURLsArray = allURLs.split("|~|")[0].split("|");
    var campuswireURLsArray = allURLs.split("|~|")[1].split("|");

    document.getElementById("courseraLinks1").innerHTML= '<a href="' + courseraURLsArray[0] + '">' + courseraURLsArray[0] + '</a>';
    document.getElementById("courseraLinks2").innerHTML= '<a href="' + courseraURLsArray[1] + '">' + courseraURLsArray[1] + '</a>';
    document.getElementById("courseraLinks3").innerHTML= '<a href="' + courseraURLsArray[2] + '">' + courseraURLsArray[2] + '</a>';

    document.getElementById("campuswireLinks1").innerHTML= '<a href="' + campuswireURLsArray[0] + '">' + campuswireURLsArray[0] + '</a>';
    document.getElementById("campuswireLinks2").innerHTML= '<a href="' + campuswireURLsArray[1] + '">' + campuswireURLsArray[1] + '</a>';
    document.getElementById("campuswireLinks3").innerHTML= '<a href="' + campuswireURLsArray[2] + '">' + campuswireURLsArray[2] + '</a>';

}