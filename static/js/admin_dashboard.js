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
  <table>
  <tr class="head-table">
  <th> Name </th>
  <th> Role </th>
  <th> Status </th>
  </tr>
  `;

  users.forEach(user =>{
    html += `
    <tr class='table_element'>
    <td> ${user.name} </td>
    <td> ${user.role} </td>
    <td> <button class="control-btn" onclick="AlterStatus(this)" id="${user.name}"> ${user.status} </button> </td>
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
  console.log(element.id);
  let current_status = element.textContent;

  const data = {
    company_name : element.id,
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
  <div id="drives-control-panel">
    <h1 style="color : white"> DRIVES </h1>
      <table>
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
      <td> ${drive.company_name } </td>
      <td> ${drive.job_role} </td>
      <td> ${drive.discription} </td>  <!-- Making simple for now expanding thing in future -->
      <td> <button class="drive-ctrl-btn" id="${drive.companny_id}" onclick="AlterDriveStatus(this)" id="${drive.company_name}"> ${drive.status} </td>
    </tr>
    `
  });
  html += "</div> </table>"
  content.innerHTML = html;
}


