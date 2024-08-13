// The documnet should be fully loaded
$(document).ready(function() {
    // Attach a click event listener to the <div> with id='red_header'
    $('#red_header').click(function() {
        // When the <div> is clicked, update the text coloe of <header> to '#FF0000'
        $('header').css('color', '#FF0000');
    });
});