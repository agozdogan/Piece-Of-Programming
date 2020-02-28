var number  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16];

for (var index = 1; index < number.length; index++) {
    if(index % 5 === 0 && index % 3 === 0){
        console.log("FizzBuzz");
    }else if(index % 5 === 0){
        console.log("Buzz");
    }else if(index % 3 === 0){
        console.log("Fizz");
    }
    else{
        console.log(index);
    }
}
