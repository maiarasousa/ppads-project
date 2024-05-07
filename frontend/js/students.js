async function createStudent(body) {
    var url = 'https://q0jzawwz35.execute-api.us-east-1.amazonaws.com/system-presence-deploy/postStudent'
    var options = { method: 'POST', data: body };
    
    var response = await axios(url, options);
    return response;
}

function getStudentDataForm() {
    document.getElementById('create-student-id').addEventListener('submit', async function (event) {
        event.preventDefault();

        const loader = document.getElementById('loader-id');
        loader.removeAttribute('hidden')

        const idClass = document.getElementById('class-list').value;
        const nameStudent = document.getElementById('student-name').value;
        const responsableEmail = document.getElementById('responsable-email').value;

        const data = {
            idClass: idClass,
            nameStudent: nameStudent,
            responsableEmail: responsableEmail
        };

        try{
            await createStudent(JSON.stringify(data));
            const alert = document.getElementById('message-success');
            alert.removeAttribute('hidden')
        } catch(error){
            const alert = document.getElementById('message-failed');
            alert.removeAttribute('hidden')
        }

        document.getElementById('class-list').value = '';
        document.getElementById('student-name').value = '';
        document.getElementById('responsable-email').value = '';

        loader.setAttribute('hidden', 'true');
    });
}
