//JS function for counter string

//Fetch date
var counterText = document.getElementById("counter-text");
// Set the date we're counting down to
var countDownDate = new Date(counterText.innerHTML).getTime();

function update(){
 // Get todays date and time
  var now = new Date().getTime();

  // Find the distance between now an the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in counter"
  counterText.innerHTML = "Next Live Stream<hr>"+days + "d " + hours + "h "
  + minutes + "m " + seconds + "s ";

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    counterText.innerHTML = "Currently Live";
  }
}
//Counter Load
update();
counterText.style.visibility = "visible";

// Update the count down every 1 second
var x = setInterval(function() {
    update();
}, 1000);
