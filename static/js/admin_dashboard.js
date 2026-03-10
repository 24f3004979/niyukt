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
    <td> <button id="control-btn"> ${user.status} </button> </td>
    </tr>
`
  });

  html += `</div> </table>`;

  content.innerHTML = html;
}


