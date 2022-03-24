var nasa = keys.NASAKEY
var toons = 'https://dojo.navyladyveteran.com/characters/'
var squish = 'https://dojo.navyladyveteran.com/squishies/'


$(document).ready(function(){
    nasaurl = `https://api.nasa.gov/planetary/apod?api_key=${nasa}`

    $.get(nasaurl, function(res) {
        console.log(res)
        var html_str = ""
        html_str +="<img src='" + res.url + "' alt='Nasa Photo'>"
        $(".photo").html(html_str)
        html_str +="<form action='/images/create/' method='post'> <input type='hidden' name='name' value='" + res.title +"'><input type='hidden' name='img' value='" + res.url +"'> <button>Save Img to Database</button></form>"
        $(".photo").html(html_str)
    }, 'json')
    $('button').click(function(){
        $('img').animate( {
            width: 'toggle'
        })
    })
    $.get(toons, function(res) {
        console.log(res)
    })
})

async function getToons() {
     var response = await fetch(`${toons}`)
     var data = await response.json()
     console.log("full toon api data:", data)
     for (var i = 0; i < data.length; i++) {
        // console.log(data[i])
        var node = document.createElement('div')
        var h2 = document.createElement('h2')
        var h3 = document.createElement('h3')
        var form = document.createElement('form')
        var nameInput = document.createElement('input')
        var imgInput = document.createElement('input')
        var button = document.createElement('button')
        var submit = document.createTextNode('Save Image to Database')
        button.appendChild(submit)
        var img = new Image()
        img.src = `${data[i].img}`
        img.alt = `${data[i].name}`
        var name = document.createTextNode(data[i].name)
        h2.appendChild(name)
        var birth = document.createTextNode(data[i].birthDay)
        form.setAttribute('method', 'post')
        form.setAttribute('action', '/images/create/')
        nameInput.setAttribute('type', 'hidden')
        imgInput.setAttribute('type', 'hidden')
        namesrc = `${data[i].name}`
        imgsrc = `${data[i].img}`
        nameInput.setAttribute('name', 'name')
        imgInput.setAttribute('name', 'img')
        nameInput.setAttribute('value', namesrc)
        imgInput.setAttribute('value', imgsrc)
        form.appendChild(nameInput)
        form.appendChild(imgInput)
        form.appendChild(button)
        // console.log("name and img only: ", namesrc, imgsrc)
        h3.appendChild(birth)
        node.appendChild(h2)
        node.appendChild(h3)
        node.appendChild(img)
        node.appendChild(form)
        document.getElementById('tune').appendChild(node)
    }
}