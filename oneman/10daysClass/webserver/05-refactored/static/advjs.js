var div = document.createElement('div');
div.textContent = "Sup, y'all?";
div.setAttribute('class', 'note');
document.body.appendChild(div);


var span = document.createElement('span');
span.textContent = "Hello!";
div.appendChild(span);


var span = document.createElement('span');
if (span.textContent) {
    span.textContent = "Hello!";
} else if (span.innerText) {
    span.innerText = "Hello!";
}

div.parentNode.removeChild(div);


var div = $('<div/>').text("Sup, y'all?").appendTo(document.body);
$('<span/>').text('Hello!').appendTo(div);

//canvas
var canvas = document.querySelector('canvas'),
    ctx = canvas.getContext('2d');

<canvas></canvas>

<script>
    var canvas = document.querySelector('canvas'),
        ctx = canvas.getContext('2d');
    ctx.fillRect(10, 10, 10, 10);
</script>


localStorage.setItem('name', 'tom');
var name = localStorage.getItem('name');

// Object example

localStorage.setItem('user', JSON.stringify({
    username: 'htmldog',
    api_key: 'abc123xyz789'
}));

var user = JSON.parse(localStorage.getItem('user'));


//errors and exception
JSON.parse("a");
try {
    JSON.parse("a"); // Produces a SyntaxError
} catch (error) {
    // Handle the error
    alert(error.message);
}    


//regex
var regex = /^[a-z\s]+$/;
var lowerCaseString = 'some characters';

if (lowerCaseString.match(regex)) {
    alert('Yes, all lowercase');
}

var text = "There is everything and nothing.";

text = text.replace(/(every|no)thing/g, 'something');

var text = "Everything and nothing.";

text = text.replace(/(every|no)thing/gi, "something");


//A closure is a function that returns a function. 
var saver = function (value) {
    return function () {
        return value;
    };
};

var retriever = saver(10);

alert(retriever());


var add = function (a) {
    return function (b) {
        return a + b;
    };
};

var addFive = add(5);

alert(addFive(10));

var hello = add('Hello ');

alert(hello('tom'));
