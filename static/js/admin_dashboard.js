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

