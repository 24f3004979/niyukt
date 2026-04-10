
// Binding apply button
let elements = document.querySelectorAll('.drive-btn')
elements.forEach(element => {
  element.addEventListener('click', (event) => {
    console.log("Applying into the given drive");
    loadapplications(element);
  });
});


function loadapplications(element){
  fetch(`http://127.0.0.1:8080/company/applications/${element.id}`).then(response => response.json()).then(data => renderUsers(data));
}
/*
function renderUsers(users){
  let content = document.getElementById("main-content");
  
  // Build template
  let html = `
  <div id="user-control-panel">
  <h1 style="color : white"> USERS </h1>
  <table id="users-box" class='table'>
  <tr class="head-table">
  <th> Name </th>
  <th> Resume </th>
  <th> Final Decission </th>
  <th> Control </th>
  </tr>
  `;

  users.forEach(user =>{
    html += `
    <tr class='table_element'>
    <td class="name"> ${user.name} </td>
    <td> ${user.resume} </td>
    <td> <button class="control-btn" onclick="AlterStatus(this)" id="${user.application_id}" style='background-color:green;'> ${user.status} </button> </td>
    <td> <button class='control-btn' onclick="RejectStatus(this)" id="${user.application_id}" style='background-color:red;'> reject </button> </td>
    </tr>
`
  });

  html += `</div> </table>`;

  content.innerHTML = html;
}
*/
// Resume rendering logic

function renderUsers(users) {
  let content = document.getElementById("main-content");

  // Header and Container
  let html = `
  <div id="user-control-panel">
    <h1 style="color: white; margin-bottom: 20px;">Applications</h1>
    <div class="cards-container">
  `;

  users.forEach(user => {
    // Convert raw resume text to Markdown HTML
    const resumeHTML = marked.parse(user.resume || "");

    html += `
    <div class="application-card">
      <div class="card-header">
        <span class="user-name">${user.name}</span>
        <div class="status-badge" style="background-color: ${user.status === 'selected' ? 'green' : '#ff0000'}; padding:1%; border-radius : 5px; color: white;">
          ${user.status}
        </div>
      </div>
      
      <div class="resume-content">
        ${resumeHTML}
      </div>

      <div class="card-actions">
        <button class="control-btn accept" onclick="AlterStatus(this)" id="${user.application_id}">
          ${user.status}
        </button>
        <button class="control-btn reject" onclick="RejectStatus(this)" id="${user.application_id}">
          Reject
        </button>
      </div>
    </div>
    `;
  });

  html += `</div></div>`; // Close container and panel
  content.innerHTML = html;
}

// Making resume rendering into the main form



// TODO : Make one alter application function
async function AlterStatus(element){
  console.log(element.id); // fetching information about the element
  let current_status = element.textContent;

  let target = "selected"
  if (current_status === "shortlist"){
    target = 'shortlisted';
  }
  if (current_status === "applied"){
    target='shortlisted';
  }
  if (current_status == 'shortlisted'){
    target = 'selected'; // No going back
  }
  if (current_status === "selected"){
    return;
  }
  if (current_status === "rejected"){
    return;
  }

  const data = {
    drive_id : element.id,
    status : current_status,
    target_status : target,
    work : "alter" // delete for deleting :)
  }

  console.log(`Sending status for the given elemnt : ${data.st}`)

  const response = await fetch(`http://127.0.0.1:8080/company/alter-application`,
    {
      method : "POST",
      headers : {
        'Content-Type' : 'application/json'  // such critical stuff :
      },
      body : JSON.stringify(data)
    })
  if (!response.ok){
    console.log("Failed with not ok");
    return;
  }

  const result = await response.json();
  element.textContent = target;
  }


// TODO : Make one alter application function
async function RejectStatus(element){
  console.log(element.id); // fetching information about the element
  let current_status = element.textContent;

  let target = "rejected"
  const data = {
    drive_id : element.id,
    status : current_status,
    target_status : target,
    work : "alter" // delete for deleting :)
  }

  console.log(`Sending status for the given elemnt : ${data.st}`)

  const response = await fetch(`http://127.0.0.1:8080/company/alter-application`,
    {
      method : "POST",
      headers : {
        'Content-Type' : 'application/json'  // such critical stuff :
      },
      body : JSON.stringify(data)
    })
  if (!response.ok){
    console.log("Failed with not ok");
  }

  const result = await response.json();
  console.log("Response for the rejection");
  console.log(result);
  if (result.st === "Failed"){
    element.innerText = "Finalized status";
  }
  element.innerText = result.st;
}




/*
// Binding apply button
let elements = document.querySelectorAll('.apply-btn')
elements.forEach(element => {
  element.addEventListener('click', (event) => {
    console.log("Applying into the given drive");
    ApplyDrive(element);
  });
});

/*
// Alteration Status for the placement drive
async function AlterDriveStatus(element){
  console.log(`Element id with element.id as : ${element.id}`);
  let current_status = element.textContent;

  const data = {
    drive_id : element.id,
    st : current_status,
    work : "alter" // TODO : making delete option with this
  }

  const response = await fetch("http://127.0.0.1:8080/admin/alter-drive-status",  // TODO Making alteration for the status
    {
      method : "POST",
      headers : {
        'Content-Type' : 'application/json'
      },
      body: JSON.stringify(data)
    })
  if (!response.ok){
    console.log("Failed response for drive alterations");
  }
  let new_status = await response.json();
  console.log(`New status update : ${new_status.st}`)

  element.textContent = new_status.st;
}


document.getElementById("requests-btn").addEventListener('click', loaddrives);

async function loaddrives(){
  const response = await fetch("http://127.0.0.1:8080/admin/requests");

  if (!response.ok){
    console.log("Failed for drivers fetch")
  }

  const data = await response.json();
  console.log(data);
  renderDrive(data);
}

function renderDrive(drives){
  console.log(drives);
  let content = document.getElementById("main-content");
  let html = `
  <div id="user-control-panel">
    <h1 style="color : white"> DRIVES </h1>
      <table id="drives">
        <tr class="head-table">
          <th> Company Name </th>
          <th> Job role </th>
          <th> Discription </th>
          <th> current stage </th>
        </tr>
  `;

  drives.forEach(drive =>{
    // TODO : With same pattern make alteration sequence for controlling drives in college
    html += `
    <tr class="table_element">
      <td id="name"> ${drive.company_name } </td>
      <td> ${drive.job_role} </td>
      <td> ${drive.discription} </td>  <!-- Making simple for now expanding thing in future -->
      <td> <button class="drive-ctrl-btn" id="${drive.drive_id}" onclick="AlterDriveStatus(this)" > ${drive.status} </td>
    </tr>
    `
  });
  html += "</div> </table>"
  content.innerHTML = html;
}

function render_dashboard(data){
  let content = document.getElementById("main-content");
  let html = `
  <h1> Total Summary </h1><br>
  <p> Company : ${data.company} | Student : ${data.student} | application : ${data.application} | drive : ${data.drives}

  `
  content.innerHTML = html;
}

function renderGraph(images){
  console.log("Loading Images for the admin panel");
  console.log(images);

  let content = document.getElementById("main-content");
  let html = `
  <h1> Graphs </h1>
  `
  // Making image and their heding with this format
  images.forEach(image =>{
    html += `<img src="/static/${image}" alt="Not Loading">`
    console.log('Loading image');
    // TODO  Load image with loading into the image directory of the given code base
    console.log(image);
  });
  content.innerHTML = html;
}

// Loading Graphs
document.getElementById("data-btn").addEventListener('click', loaddashboard);

async function loaddashboard(){
  const response = await fetch("http://127.0.0.1:8080/admin/dashboard")

  if (!response.ok){
    console.log("Failed with loading information");
  }
  const data = await response.json();
  console.log("Data loading");
  // Loading information into the Panel
  render_dashboard(data);
}

async function loadgraph(){
  const response = await fetch("http://127.0.0.1:8080/admin/graphs")

  if (!response.ok){
    console.log("Failed for loading Graphs");
  }
  const data = await response.json();
  console.log("Making Data loading for graphs");
  console.log(data.image);
  renderGraph(data.image);
}

*/

// Search Box functionality Making simple searching way for filtering the given changes
document.getElementById("search-box").addEventListener('input', filterUsers);

// Simple filter function for checking user existense with simpel frontend filter
function filterUsers(){
  let query = document.getElementById("search-box").value.toLowerCase();

  let rows = document.querySelectorAll(".table_element");

  rows.forEach(row => {
    let name = row.children[0].textContent.toLowerCase();
    let role = row.children[1].textContent.toLowerCase();

    if(name.includes(query) || role.includes(query)){
      row.style.display = "";
    } else {
      row.style.display = "none";
    }
  });
}

// Final commit for admin dashboard build
