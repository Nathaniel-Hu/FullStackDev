document.getElementById("myButton").onclick = function(){
    var myProductName = document.getElementById("myProductName").value;
    var myProductDesc = document.getElementById("myProductDesc").value;
    console.log("Product Name:", myProductName);
    console.log("Product Description:", myProductDesc);
}

function sendUserInfo() {
    let userInfo = {
        'name': 'apple',
        'type': 'fruit',
    }
    const request = new XMLHttpRequest()
    request.open('POST', '/processUserInfo/${JSON.stringify(userInfo)}')
    request.onload = () => {
        const flaskMessage = request.responseText
        console.log(flaskMessage)
    }
    request.send()
}