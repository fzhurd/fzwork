var x = myFunction(4, 3);      

function myFunction(a, b) {
    return a * b; 
    }

function toCelsius(fahrenheit) {
    return (5/9) * (fahrenheit-32);
}
document.getElementById("demo").innerHTML = toCelsius(32);               