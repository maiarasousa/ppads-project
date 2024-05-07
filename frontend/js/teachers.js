async function createTeacher(body) {
    var url = 'https://q0jzawwz35.execute-api.us-east-1.amazonaws.com/system-presence-deploy/postTeacher'
    var options = { method: 'POST', data: body };
    
    var response = await axios(url, options);
    return response;
}

function getTeacherDataForm() {
    document.getElementById('create-teacher-id').addEventListener('submit', async function (event) {
        event.preventDefault();

        const loader = document.getElementById('loader-id');
        loader.removeAttribute('hidden')

        const idClass = document.getElementById('class-list').value;
        const teacherName = document.getElementById('teacher-name').value;
        const teacherEmail = document.getElementById('teacher-email').value;

        const data = {
            idClass: idClass,
            teacherName: teacherName,
            teacherEmail: teacherEmail
        };

        try{
            await createTeacher(JSON.stringify(data));
            const alert = document.getElementById('message-success');
            alert.removeAttribute('hidden')
        } catch(error){
            const alert = document.getElementById('message-failed');
            alert.removeAttribute('hidden')
        }

        document.getElementById('class-list').value = '';
        document.getElementById('teacher-name').value = '';
        document.getElementById('teacher-email').value = '';

        loader.setAttribute('hidden', 'true');
    });
}
