// restart game button
var restart = document.querySelector("#b");

//Grab all the squares
var squares = document.querySelectorAll('td');


//clear all the squares
function clearBoard(){
    for(var i=0; i < squares.length; i++){
        squares[i].textContent = '';
    }
}
restart.addEventListener('click', clearBoard);

//check the square marker


//For loop to add event listener to all the squares