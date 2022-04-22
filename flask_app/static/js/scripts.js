var gitUrl = 'https://api.github.com/users/'
var jokeUrl = 'https://v2.jokeapi.dev/joke/Programming'
var user = document.getElementById('gitUsername').value;
console.log("The username: ", user);

// console.log(gitUrl)

async function getGitHub() {
    var response = await fetch(`${gitUrl}${user}/followers`)
    var data = await response.json()
    console.log("github url json res: ", data)
    console.log("1st index: ", data[0])
    console.log('1st index login id: ', data[0].login)
        // var node = document.createElement('div')  // Create a div section
        // var h2 = document.createElement('h2') // Create a h2
        // var login = document.createTextNode(data[0].login) // set var login to equal data by telling it that it is text
        // h2.appendChild(login) // Add data to the h2
        // node.appendChild(h2)  // put h2 inside the div
        // document.getElementById('gitHub').appendChild(node) // Add div to page
    for (var i = 0; i < data.length; i++) {
        var node = document.createElement('div')  // Create a div section
        var h2 = document.createElement('h2') // Create a h2
        var login = document.createTextNode(data[i].login) // set var login to equal data by telling it that it is text
        h2.appendChild(login) // Add data to the h2
        node.appendChild(h2)  // put h2 inside the div
        document.getElementById('gitHub').appendChild(node) // Add div to page
    }
}

// getGitHub()

async function jokeApi() {
    var res = await fetch (`${jokeUrl}`)
    var data = await res.json()
    console.log("joke api response: ", data)
    console.log("joke type: ", data.type)
    var t = data.type
    if (t === 'single') {
        console.log("The type was single")
        var node = document.createElement('div') //Creates outer div
        var h2 = document.createElement('h2') //Creates h2 line
        var joke = document.createElement('h3') // Creates h3 line
        var form = document.createElement('form') // Created the form tags
        var inpType = document.createElement('input') // Creates the input field
        var inpJoke = document.createElement('input')
        var button = document.createElement('button')
        var buttonText = document.createTextNode('Save to DataBase')
        button.appendChild(buttonText)
        inpType.setAttribute('type', 'hidden') // inside input tag add type='hidden'
        inpJoke.setAttribute('type', 'hidden')
        inpType.setAttribute('name', 'jokeType') // set the name to = the column name of jokeType
        inpJoke.setAttribute('name', 'jokeText') // sets the name to = the column name of jokeText
        inpType.setAttribute('value', t) // set the values to their corresponding info
        inpJoke.setAttribute('value', data.joke)
        form.setAttribute('method', 'post') // inside opening form tag adds the method='post'
        form.setAttribute('action', '/joke/createSingle/') // inside opening form tag adds action='/joke/createSingle/
        var style = document.createTextNode(`This is a ${t} joke`) // create text
        h2.appendChild(style) // add style text to h2
        var jokeText = document.createTextNode(data.joke) //creates text
        form.appendChild(inpType)
        form.appendChild(inpJoke)
        form.appendChild(button)
        joke.appendChild(jokeText) // adds jokeText to h3
        node.appendChild(h2) // adds h2 to div
        node.appendChild(joke) //add h3 to div
        node.appendChild(form)
        document.getElementById('joke').appendChild(node) // prints div to page
    }
    else {
        console.log("Nope this was a two part joke")
        var node = document.createElement('div')
        var h2 = document.createElement('h2')
        var setup = document.createElement('h3')
        var delivery = document.createElement('h3')
        var form = document.createElement('form')
        var inpType = document.createElement('input')
        var inpSetup = document.createElement('input')
        var inpDelivery = document.createElement('input')
        var style = document.createTextNode(`This is a ${t} joke`)
        var setupText = document.createTextNode(data.setup)
        var deliveryText = document.createTextNode(data.delivery)
        var button = document.createElement('button')
        var buttonText = document.createTextNode('Save to DataBase')
        button.appendChild(buttonText)
        form.setAttribute('method', 'post') // inside opening form tag adds the method='post'
        form.setAttribute('action', '/joke/createTwopart/') 
        inpType.setAttribute('type', 'hidden')
        inpType.setAttribute('name', 'jokeType')
        inpType.setAttribute('value', t)
        inpSetup.setAttribute('type', 'hidden')
        inpDelivery.setAttribute('type', 'hidden')
        inpSetup.setAttribute('name', 'jokeSetup')
        inpDelivery.setAttribute('name', 'jokeDeleiver')
        inpSetup.setAttribute('value', data.setup)
        inpDelivery.setAttribute('value', data.delivery)
        setup.appendChild(setupText)
        delivery.appendChild(deliveryText)
        h2.appendChild(style)
        form.appendChild(inpType)
        form.appendChild(inpSetup)
        form.appendChild(inpDelivery)
        form.appendChild(button)
        node.appendChild(h2)
        node.appendChild(setup)
        node.appendChild(delivery)
        node.appendChild(form)
        document.getElementById('joke').appendChild(node)
    }
}
// jokeApi()