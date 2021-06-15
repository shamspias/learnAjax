console.log('hello my post')

const helloWorldBox = document.getElementById('hello-world')
const postBox = document.getElementById('posts-box')


$.ajax({
    type: 'GET',
    url: '/hello-world/',
    success: function (response) {
        console.log('success', response.text)
        helloWorldBox.textContent = response.text
    },
    error: function (error) {
        console.log('error', error)
    }
})

$.ajax({
    type: 'GET',
    url: '/data/',
    success: function (response) {
        console.log('success', response)
        const data = response.data
        data.forEach(el => {
            postBox.innerHTML += `
                <div class="card" style="width: 18rem;">
                  
                  <div class="card-body">
                    <h5 class="card-title">${el.title}</h5>
                    <p class="card-text">${el.body}</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                  </div>
                </div>
            `

        });
    },
    error: function (error) {
        console.log('error', error)
    }
})