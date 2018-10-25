

// Retrieve update button and add an onclick function
document.getElementById("saveBtn").addEventListener("click", () => {
    const
        id = document.getElementById("id").value,
        name = document.getElementById("name").value,
        email = document.getElementById("email").value,
        password = document.getElementById("password").value,
        dob = document.getElementById("dob").value,
        bio = document.getElementById("bio").value;

    const data = {
        name: name,
        email: email,
        password: password,
        dob: dob,
        bio: bio
    };

    // fetch('http://localhost:8000/info/2/update', {
    //     method: 'POST',
    //     headers: {
    //         "Context-Type": "application/json"
    //     },
    //     body: JSON.stringify(data)
    // })
    //     .then(() => console.log('hello, request has been sent'));

    // fetch('http://localhost:8000/info/2/update')
    //     .then((res) => res.json())
    //     .then((data) => console.log(data));

    // POST request to update the database with new user information
    fetch(`http://localhost:8000/info/${id}/update`, {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": Cookies.get('csrftoken'),
            "Accept": "application/json",
            "Content-Type": "application/json"
         },
        body: JSON.stringify(data),
    })
        .then((res) => {
            if(res.status === 200){
                const alert = document.createElement('div');
                const text = document.createTextNode('Your profile has been successfully updated!');
                const container = document.querySelector('.container');
                alert.className = "alert alert-success";
                alert.id = "tempAlert";
                alert.appendChild(text);
                container.insertAdjacentElement('beforebegin', alert);

                setTimeout(() => {
                    alert.remove();
                }, 5000)
             }
        })
        .catch((err) => console.log("There is an error: ", err))
})