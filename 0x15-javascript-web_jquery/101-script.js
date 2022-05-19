document.addEventListener('DOMContentLoaded', function () {
    $('#add_item').click(addElement);
    $('#remove_item').click(removeElement);
    $('#clear_list').click(removeList);
});

function addElement() {
    $('UL.my_list').append('<li>Item</li>');
}

function removeElement() {
    $('UL.my_list').children().last().remove();
}

function removeList() {
    $('UL.my_list').empty();
}
