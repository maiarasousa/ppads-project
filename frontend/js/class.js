async function createClass(body) {
    var url = 'https://q0jzawwz35.execute-api.us-east-1.amazonaws.com/system-presence-deploy/postClass'
    var options = { method: 'POST', data: body };
    
    var response = await axios(url, options);
    return response;
}

function getClassDataForm() {
    document.getElementById('create-class-id').addEventListener('submit', async function (event) {
        event.preventDefault();

        const loader = document.getElementById('loader-id');
        loader.removeAttribute('hidden')

        const yearScholl = document.getElementById('year-scholl').value;
        const className = document.getElementById('class-name').value;

        const data = {
            yearScholl: yearScholl,
            className: className
        };

        try{
            await createClass(JSON.stringify(data));
            const alert = document.getElementById('message-success');
            alert.removeAttribute('hidden')
        } catch(error){
            const alert = document.getElementById('message-failed');
            alert.removeAttribute('hidden')
        }

        document.getElementById('year-scholl').value = '';
        document.getElementById('class-name').value = '';

        loader.setAttribute('hidden', 'true');
    });
}
