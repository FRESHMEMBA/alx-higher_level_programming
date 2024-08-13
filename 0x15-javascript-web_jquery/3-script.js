// the document should be fully loaded
$(document).ready(function() {
    // Attach a click event listener to the <div> with id='red_header"
    $('#red_header').click(function() {
        // When the <div> is clicked, add the class 'red' to the <header> element
        $('header').addClass('red');
    });
});