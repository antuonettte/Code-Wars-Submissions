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


for(var i = 1; i < 20; i++){
    if(is_prime(i)){
        console.log(i + ' is Prime')
    }else{
        console.log(i + ' is Non-Prime')
    }
}