// Event Listeners

document.getElementById("user-btn").addEventListener("click", loadUsers);

function loadUsers(){
  fetch("http://127.0.0.1:8080/admin/users").then(response => response.json()).then(data => renderUsers(data));
}

function renderUsers(users){
  let content = document.getElementById("main-content");
  
  // Build template
  let html = `
  <div id="user-control-panel">
  <h1 style="color : white"> USERS </h1>
  <table id="drives"  class='table'>
  <tr class="head-table">
  <th> Name </th>
  <th> Role </th>
  <th> Status </th>
  </tr>
  `;

  users.forEach(user =>{
    
    if (user.status == "deactivated"){
      status = "activate"
    }
    if (user.status === "activated"){
      status = "deactivate"
    }

    html += `
    <tr class='table_element'>
    <td class="name"> ${user.name} </td>
    <td> ${user.role} </td>
    <td> <button class="control-btn" onclick="AlterStatus(this)" id="${user.name}" style='color:black;'>${status}</button> </td>
    </tr>
`
  });

  html += `</div> </table>`;

  content.innerHTML = html;
}


async function AlterStatus(element){
  console.log(element.id); // fetching information about the element
  let current_status = element.textContent;

  const data = {
    name : element.id,
    st : current_status,
    work : "alter" // delete for deleting :)
  }

  console.log(`Sending status for the given elemnt : ${data.st}`)

  const response = await fetch("http://127.0.0.1:8080/admin/alter-status",
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
  element.textContent = result.st;
  }

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
      <table id="drives" class='table'>
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
  <h1 style='color:white;'> Graphs </h1>
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

document.getElementById('data-btn').addEventListener('click',loadgraph);

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
