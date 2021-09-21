function friend(list){
    var friend = []
    
    list.forEach(person => {
        if (person.length == 4){
            friend.push(person)
        }
    });

    return friend
}

console.log(friend(["Ryan", "Kieran", "Mark"]))