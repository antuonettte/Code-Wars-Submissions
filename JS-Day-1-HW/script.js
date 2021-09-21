
var xml = new XMLHttpRequest();

xml.onreadystatechange = function(){
    if( this.readyState === 4 && this.status === 200){
        document.getElementById("Ajax").innerHTML = this.responseText;
    }
}
 
xml.open('GET','/data.json')

xml.send();

   console.log('Is Prime \n')
    console.log(is_prime(13))

    console.log('Friend or Foe \n')
    console.log(friend(["Ryan", "Kieran", "Mark"]))
    


// Is a number prime kata
function is_prime(num){
    if(num <= 1){
        return false
    }
    for(let i = 2; i < Math.floor(Math.sqrt(num)) + 1 ; i++){
        if(parseInt(num % i) === 0 ){
            return false
        }

    }
    return true
}


// for(var i = 1; i < 20; i++){
//     if(is_prime(i)){
//         console.log(i + ' is Prime')
//     }else{
//         console.log(i + ' is Non-Prime')
//     }
// }


// Friend or Foe Kata
function friend(list){
    var friend = []
    
    list.forEach(person => {
        if (person.length == 4){
            friend.push(person)
        }
    });

    return friend
}

