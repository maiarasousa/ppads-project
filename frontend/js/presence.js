//====================================================
//                      GETCLASS
//====================================================
async function getClass() {
  var url = 'https://q0jzawwz35.execute-api.us-east-1.amazonaws.com/system-presence-deploy/getClass'
  var options = { method: 'GET' };
  var response = await axios(url, options);
  return response.data;
}

//====================================================
//                 GET STUDENTS CLASS
//====================================================
async function getStudentsClass(idClass) {
  var url = 'https://q0jzawwz35.execute-api.us-east-1.amazonaws.com/system-presence-deploy/getStudentsClass?idClass=' + idClass
  var options = { method: 'GET' };
  var response = await axios(url, options);
  return response.data;
}

//====================================================
//                   POST FREQUENCY
//====================================================
async function postListPresence(body) {
  var url = 'https://q0jzawwz35.execute-api.us-east-1.amazonaws.com/system-presence-deploy/postListPresence'
  var options = { method: 'POST', data: body };
  var response = await axios(url, options);
  return response.data;
}

//====================================================
//                     POPULATES
//====================================================
async function populateList() {
  const select = document.getElementById('class-list');
  const previouslySelected = select.value;

  const loadingOption = document.createElement('option');
  loadingOption.value = '';
  loadingOption.text = 'Carregando turmas...';
  loadingOption.disabled = true;
  select.appendChild(loadingOption);

  const classes = await getClass();

  const optionsFragment = document.createDocumentFragment();

  classes.forEach((item) => {
    const opt = document.createElement('option');
    opt.value = item.idClass;
    opt.text = item.className;
    opt.id = 'option' + item.idClass;
    optionsFragment.appendChild(opt);
  });

  select.innerHTML = '';
  select.appendChild(optionsFragment);

  loadingOption.remove();

  select.value = previouslySelected;

  select.addEventListener('change', (event) => {
    const selectedValue = event.target.value;
    populateTable(selectedValue);
  });
}

async function populateTable(idClass) {
  const loader = document.getElementById('loader');
  loader.removeAttribute('hidden')

  var students = await getStudentsClass(idClass);
  const tableBody = document.getElementById('table-main');
  tableBody.innerHTML = '';

  students.forEach((student) => {
    const tableRow = document.createElement('tr');
    const nameCell = document.createElement('th');
    const presenceCell = document.createElement('td');
    presenceCell.scope = 'row';

    nameCell.textContent = student["nameStudent"];

    const presenceRadioOptions = document.createElement('div');
    presenceRadioOptions.classList.add('form-check', 'form-check-inline');

    const presenceYesRadio = document.createElement('input');
    presenceYesRadio.type = 'radio';
    presenceYesRadio.classList.add('form-check-input');
    presenceYesRadio.name = `${student["nameStudent"]}`;
    presenceYesRadio.value = 'Sim';
    presenceRadioOptions.appendChild(presenceYesRadio);
    presenceYesRadio.setAttribute('idClass', idClass);
    presenceYesRadio.setAttribute('idStudent', student["idStudent"]);

    const presenceYesLabel = document.createElement('label');
    presenceYesLabel.classList.add('form-check-label');
    presenceYesLabel.textContent = 'Sim';
    presenceYesLabel.htmlFor = `${student["nameStudent"]}`;
    presenceRadioOptions.appendChild(presenceYesLabel)

    const presenceNoRadio = document.createElement('input');
    presenceNoRadio.type = 'radio';
    presenceNoRadio.classList.add('form-check-input');
    presenceNoRadio.name = `${student["nameStudent"]}`;
    presenceNoRadio.id = `${student["idStudent"]}`;
    presenceNoRadio.value = 'Não';
    presenceRadioOptions.appendChild(presenceNoRadio);
    presenceNoRadio.setAttribute('idClass', idClass);
    presenceNoRadio.setAttribute('idStudent', student["idStudent"]);

    const presenceNoLabel = document.createElement('label');
    presenceNoLabel.classList.add('form-check-label');
    presenceNoLabel.textContent = 'Não';
    presenceNoLabel.htmlFor = `${student["nameStudent"]}`;
    presenceRadioOptions.appendChild(presenceNoLabel);

    tableRow.appendChild(nameCell);
    tableRow.appendChild(presenceCell);
    presenceCell.appendChild(presenceRadioOptions);
    tableBody.appendChild(tableRow);
  });

  loader.setAttribute('hidden', 'true');
}

async function sendListPresence() {
  var loader = document.getElementById('loader');
  loader.removeAttribute('hidden')

  var selectedStudents = getStudentsData();
  var allStudentsSelected = true;

  const tableBody = document.getElementById('table-main');
  const rows = tableBody.getElementsByTagName('tr');
  for (let i = 0; i < rows.length; i++) {
    const radioButtons = rows[i].getElementsByTagName('input');
    let studentSelected = false;

    for (let j = 0; j < radioButtons.length; j++) {
      const radioButton = radioButtons[j];
      if (radioButton.checked) {
        studentSelected = true;
        break;
      }
    }

    if (!studentSelected) {
      allStudentsSelected = false;
      break;
    }
  }

  const scheduleSelect = document.getElementById('typeCalled');
  if (!allStudentsSelected || scheduleSelect.selectedIndex === 0) {
    alert("Por favor, selecione a presença de cada aluno e escolha um horário antes de confirmar.");
    loader.setAttribute('hidden', 'true');
    return;
  }

  var result = await postListPresence(JSON.stringify(selectedStudents));

  loader.setAttribute('hidden', 'true');

  if(result["Message"] == 'Lista de presença salva com sucesso!'){
    alert(result["Message"])
    window.location.href = '../frontend/index.html';
  }
  else{
    alert('Falha ao salvar lista de presença, tente novamente em alguns minutos!')
    window.location.href = '../frontend/index.html';
  }
}

function getStudentsData() {
  const studentList = [];
  const tableBody = document.getElementById('table-main');
  const rows = tableBody.getElementsByTagName('tr');

  for (let i = 0; i < rows.length; i++) {
    const radioButtons = rows[i].getElementsByTagName('input');

    for (let j = 0; j < radioButtons.length; j++) {
      const radioButton = radioButtons[j];

      if (radioButton.checked) {
        const studentData = {
          idStudent: radioButton.getAttribute('idStudent'),
          idClass: radioButton.getAttribute('idClass'),
          presenceStatus: (radioButton.value == 'Sim') ? 1 : 0,
          typeCalled: document.getElementById('typeCalled').value
        };
        studentList.push(studentData);
        break;
      }
    }
  }

  return studentList;
}