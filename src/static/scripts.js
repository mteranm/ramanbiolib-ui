function openTab(evt, tabName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";

    updateResult("")
} 
document.getElementById("slk_tab").click();

var tableExpanded = false

function showMore() {
    showMoreBtn = document.getElementById("show_more_btn")
    if (tableExpanded) {
      showMoreBtn.innerHTML = "Show more";
      tableExpanded = false
      $(".short_results").show();
      $(".full_results").hide();
    } else {
      showMoreBtn.innerHTML = "Show less";
      tableExpanded = true
      $(".short_results").hide();
      $(".full_results").show();
    }
}

function updateResult(html_content) {
    console.log("Updating result with: ", html_content);
    const plotDiv = document.getElementById('results')
    document.getElementById('results').innerHTML = html_content;

    // Find and execute all scripts inside the injected HTML
    var scripts = plotDiv.getElementsByTagName("script");
    for (var i = 0; i < scripts.length; i++) {
        var newScript = document.createElement("script");
        newScript.text = scripts[i].text;  // Copy script content
        document.body.appendChild(newScript).parentNode.removeChild(newScript); // Execute & remove
    }
    $(".loader_container").removeClass("active");
}

function onSearchClick() {
    // Get the values of the form inputs
    var file = document.getElementById('spectra').files[0]; // Get the file input (first file selected)
    var windowSize = document.getElementById('window').value; // Get window size value
    var tableN = document.getElementById('table_n').value; // Get Top N table value
    var plotN = document.getElementById('plot_n').value; // Get Top N plot value

    $(".loader_container").addClass("active");

    if (file) {
        // Get file information
        var fileName = file.name;
        var fileSize = file.size;
        var fileType = file.type;
        var lastModified = new Date(file.lastModified).toLocaleString();  // Convert lastModified timestamp to a readable date
        
        console.log('File Name:', fileName);
        console.log('File Size:', fileSize, 'bytes');
        console.log('File Type:', fileType);
        console.log('Last Modified:', lastModified);


        // You can read the file content if needed
        var reader = new FileReader();
        reader.onload = function(e) {
            var fileContent = e.target.result;  // The content of the file (as a string or binary)
            // Do something with file content (e.g., send to server)
            pyHandler.slk_search(fileContent, fileName, windowSize, tableN, plotN);
        };

        // Read the file (e.g., as text)
        reader.readAsText(file);
    } else {
        console.log('No file selected');
    }
}

function onPMSearchClick() {
    // Get the values of the form inputs
    var file = document.getElementById('pm_spectra').files[0]; // Get the file input (first file selected)
    var sourceType = document.getElementById('input_selection').value; 
    var sortCol = document.getElementById('sort_metric').value; 
    var tolerance = document.getElementById('tolerance').value; 
    var penalty = document.getElementById('penalty').value; 
    var resultsN = document.getElementById('pm_table_n').value;
    var plotN = document.getElementById('pm_plot_n').value;
    var prominence = document.getElementById('prominence').value;
    var peaks = document.getElementById('peaks').value;
    console.log('File:', file);
    console.log('Source:', sourceType);
    console.log('sortCol:', sortCol);
    console.log('tolerance:', tolerance);
    console.log('penalty:', penalty);
    console.log('resultsN:', resultsN);
    console.log('plotN:', plotN);

    $(".loader_container").addClass("active");

    if (sourceType == 'spectrum') {
        if (file) {
            // Get file information
            var fileName = file.name;
            var fileSize = file.size;
            var fileType = file.type;
            var lastModified = new Date(file.lastModified).toLocaleString();  // Convert lastModified timestamp to a readable date
            
            console.log('File Name:', fileName);
            console.log('File Size:', fileSize, 'bytes');
            console.log('File Type:', fileType);
            console.log('Last Modified:', lastModified);

            // You can read the file content if needed
            var reader = new FileReader();
            reader.onload = function(e) {
                var fileContent = e.target.result;  // The content of the file (as a string or binary)
                // Do something with file content (e.g., send to server)
                var inputDict = {
                    csv_data: fileContent,
                    prominence: prominence,
                    filename: fileName
                }
                pyHandler.pm_search(sourceType, sortCol, tolerance, penalty, resultsN, plotN, inputDict)
            };

            // Read the file (e.g., as text)
            reader.readAsText(file);
        } else {
            console.log('No file selected');
        }
    }
    else {
        var inputDict = {
            peaks: peaks,
        }
        pyHandler.pm_search(sourceType, sortCol, tolerance, penalty, resultsN, plotN, inputDict)
    }
}

function tableToCSV() {
    pyHandler.save_csv();
}

$(document).ready(function(){
    document.getElementById('input_selection').onchange = function () { 
        var status = this.value;
        if(status=="spectrum") {
            $("#peaks_input").hide();
            $("#specturm_input").show();
        } else {
            $("#peaks_input").show();
            $("#specturm_input").hide();
        }        
     }

    document.getElementById("input_selection").dispatchEvent(new Event('change', { bubbles: true }));

});