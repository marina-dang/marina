const age = 20;
console.log('Age:', age);
if (age > 17) {console.log('You are an adult!');}
else {console.log('You are not an adult yet!');}

yourAge = 16;
console.log('Your age is', yourAge);
if (yourAge < 13) {console.log('You are a child.');}
else if (yourAge < 20) {console.log('You are a teenager.');}
else {console.log('You are an adult.');}

let myAge = parseInt(prompt('Enter  your age:'));
console.log('Your age is', myAge);
if (myAge < 13){
    console.log('You are a child.');
    if (myAge < 5) {
        console.log('You are a baby.');
    }
}
else if (myAge < 20) {
    console.log('You are a teenager.');
    if (myAge > 17) {
        console.log('You are an adult.');
    }
}
else if (myAge < 60) {
    console.log('You are an adult.');
    if (myAge < 50) {
        console.log('You are a middle-aged adult.');
        if (myAge < 36) {
            console.log('You are a young adult.');
        }
    }
}
else (
    console.log('You are an elderly adult.')
)
