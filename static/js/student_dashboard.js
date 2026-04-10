// --- Event Handlers ---

async function ApplyDrive(element) {
  let current_status = element.textContent.trim();

  if (current_status === "selected") return;

  const data = {
    name: element.id,
    st: current_status,
    work: "alter"
  };

  const response = await fetch(`http://127.0.0.1:8080/student/apply/${element.id}`, {
    method: "POST",
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  if (response.ok) {
    const result = await response.json();
    element.textContent = result.st;
  } else {
    console.error("Failed to apply to drive");
  }
}

async function AlterDriveStatus(element) {
  let current_status = element.textContent.trim();
  if (current_status === 'selected') return;

  const data = {
    drive_id: element.id,
    st: current_status,
    work: "alter"
  };

  const response = await fetch("http://127.0.0.1:8080/admin/alter-drive-status", {
    method: "POST",
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });

  if (response.ok) {
    let new_status = await response.json();
    element.textContent = new_status.st;
  } else {
    console.error("Failed drive alteration");
  }
}

// --- Data Loading & Rendering ---

async function loaddrives() {
  const response = await fetch("http://127.0.0.1:8080/student/applications");
  if (response.ok) {
    const data = await response.json();
    renderDrive(data);
  }
}

async function loaddashboard() {
  const response = await fetch("http://127.0.0.1:8080/admin/dashboard");
  if (response.ok) {
    const data = await response.json();
    render_dashboard(data);
  }
}

function renderDrive(drives) {
  let content = document.getElementById("main-content");
  let html = `
  <div id="user-control-panel">
    <h1 style="color: white"> APPLICATIONS MADE </h1>
    <table id="drives" class="table">
      <tr class="head-table">
        <th> Company Name </th>
        <th> Job role </th>
        <th> Current stage </th>
      </tr>
  `;

  drives.forEach(drive => {
    html += `
    <tr class="table_element">
      <td> ${drive.company_name} </td>
      <td> ${drive.job_role} </td>
      <td> ${drive.status} </td>
    </tr>
    `;
  });

  html += `</table></div>`;
  content.innerHTML = html;
}

function render_dashboard(data) {
  document.getElementById("main-content").innerHTML = `
    <h1> Total Summary </h1><br>
    <p> Company: ${data.company} | Student: ${data.student} | Application: ${data.application} | Drive: ${data.drives} </p>
  `;
}

function filterUsers() {
  let query = document.getElementById("search-box").value.toLowerCase();
  let rows = document.querySelectorAll(".table_element");

  rows.forEach(row => {
    let name = row.children[0].textContent.toLowerCase();
    let role = row.children[1].textContent.toLowerCase();
    row.style.display = (name.includes(query) || role.includes(query)) ? "" : "none";
  });
}

// --- Event Listeners ---

// Use a single listener for data-btn to trigger both loads if needed
document.getElementById("data-btn")?.addEventListener('click', () => {
  loaddrives();
  loaddashboard();
});

document.getElementById("search-box")?.addEventListener('input', filterUsers);

// Binding apply buttons (if they exist on initial load)
document.querySelectorAll('.apply-btn').forEach(btn => {
  btn.addEventListener('click', () => ApplyDrive(btn));
});