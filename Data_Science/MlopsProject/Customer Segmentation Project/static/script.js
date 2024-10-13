// Add a scroll event listener to the window
window.addEventListener('scroll', function() {
    // Get the position of the "About Us" section
    var about = document.getElementById('about');
    var aboutPosition = about.getBoundingClientRect();
  
    // Check if the "About Us" section is in view
    if (aboutPosition.top < window.innerHeight && aboutPosition.bottom >= 0) {
      // Add a class to the "person" elements to animate them
      var persons = document.getElementsByClassName('person');
      for (var i = 0; i < persons.length; i++) {
        persons[i].classList.add('animate');
      }
    }
  });