// Wait for the document to be fully loaded
$(document).ready(function() {
    $('#add_item').click(function() {
        const newItem = $('<li>Item</li>');
        
        $('.my_list').append(newItem);
    });
});
