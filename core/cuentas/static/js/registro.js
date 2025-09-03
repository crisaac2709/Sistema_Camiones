(function registro() {
    const form = document.getElementById('form')
    const url = window.URLS?.api_registro

    if (!form || !url) {
        console.error('Falta url de la api o form')
    }
    
    form.addEventListener('submit', async (e) => {
        e.preventDefault()
        
        const fd = new FormData(form)

        const csrfFromInput = document.querySelector('[name=csrfmiddlewaretoken]')?.value;
        const csrf = csrfFromInput || getCookie('csrftoken');

        try {
            const response = await fetch(url, {
                method: 'POST',
                body: fd,
                headers: {
                    'X-CSRFToken': csrf,             
                    'X-Requested-With': 'XMLHttpRequest',
                },
                credentials: "same-origin"
            })

            const data = await response.json()

            if (data.ok) {
                window.location.href = data.url
            } else {
                console.log(data.errors);
                const errorsDiv = document.getElementById('form-errors')
                errorsDiv.innerHTML = ""

                for (const [field, messages] of Object.entries(data.errors)) {
                errorsDiv.innerHTML += `<p><b>${field}:</b> ${messages.join(", ")}</p>`;
                }
                console.log(errorsDiv)
            }

        } catch(err) {
            console.error(err)
        }
    })
    // Helpers
  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
  }

})()


