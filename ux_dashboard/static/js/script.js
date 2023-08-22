document.addEventListener('DOMContentLoaded', function() {
    const loadEventsBtn = document.querySelector('#load-events-btn');
    const viewRecordsBtn = document.querySelector('#view-records-btn');
    const viewOtherDataBtn = document.querySelector('#view-other-data-btn');
    const loadEventsSection = document.querySelector('.load-events-section');
    const viewRecordsSection = document.querySelector('.view-records-section');
    const recordsTable = document.querySelector('#records-table');
    const ipMask = document.querySelector('#ip-mask');
    const infoMask = document.querySelector('#info-mask');

    loadEventsBtn.addEventListener('click', () => {
        loadEventsSection.style.display = 'block';
        viewRecordsSection.style.display = 'none';
        // loadEvents();
        console.log("loadEventsBtn clicked");
    });


    viewRecordsBtn.addEventListener('click', () => {
        loadEventsSection.style.display = 'none';
        viewRecordsSection.style.display = 'block';
        console.log("clicked");
        fetchRecords();
    });

    viewOtherDataBtn.addEventListener('click', () => {
        if(viewOtherDataBtn.textContent==="View Masked Data")
        {
            fetchRecords();
            viewOtherDataBtn.textContent = "View UnMasked Data";
            ipMask.textContent="IP (Masked)";
            infoMask.textContent="Info (Masked)";
        }
        else
        {
            fetchUnmaskedRecords();
            viewOtherDataBtn.textContent = "View Masked Data";
            ipMask.textContent="IP (UnMasked)";
            infoMask.textContent="Info (UnMasked)";

        }
    });

    async function loadEvents() {
        const d = {
            number_of_events: 1
        };
        
        let response = await fetch('/load-events', {
            method: 'POST', // Set the request method to 'POST'
            headers: {
                'Content-Type': 'application/json'  // Indicate that you're sending JSON data
            },
            body: JSON.stringify(d)  // Convert the data object to a JSON string
        });        
        // let data = await response.json();
        console.log("data: ",data);
        displayData(data);
    }

    async function fetchRecords() {
        let response = await fetch('/get-records');
        let data = await response.json();

        displayData(data);
    }

    async function fetchUnmaskedRecords() {
        let response = await fetch('/get-unmasked-records');
        let data = await response.json();

        displayData(data);
    }

    function displayData(data) {
        recordsTable.innerHTML = ''; // Clear previous data

        data.forEach(record => {
            console.log("record: ",record);
            let row = recordsTable.insertRow();

            record.forEach(cellValue => {
                let cell = row.insertCell();
                cell.textContent = cellValue;
            });
        });
    }
});
function toggleDivVisibility() {
    console.log("toggleDivVisibility");
    const div = document.getElementById("instructions");
    if (div.classList.contains("shrink")) {
        div.classList.remove("shrink");
    } else {
        div.classList.add("shrink");
    }
}

async function sendEventCount() {
    console.log("sendEventCount clicked");
    let eventCount = document.getElementById("number-of-events").value;
    console.log("numberOfEvents"+eventCount);
    const req = {
        number_of_events: eventCount
    };
    
    let response = await fetch('/load-events', {
        method: 'POST', // Set the request method to 'POST'
        headers: {
            'Content-Type': 'application/json'  // Indicate that you're sending JSON data
        },
        body: JSON.stringify(req)  // Convert the data object to a JSON string
    });     
    console.log("response: ",response);
    // if(response.status ==200)
    // {

    // }
    // Get the value from the input

    // Send eventCount... (here we're just going to print it)
    // You can modify this part to actually "send" the data wherever you need it

    // Display a success message after processing
    if(response.status==200)
    {

    setTimeout(() => {
        const element = document.getElementById("load-event-status");
        element.textContent = "Successfully Added "+eventCount+" records to the table";
    
        // Set another timeout to clear the textContent after 5 seconds
        setTimeout(() => {
            element.textContent = "";
        }, 5000);  // 5000 milliseconds = 5 seconds
    
    }, 0);  // display the success message after 1 second for demonstration
    
    }
    
}