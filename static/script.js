const toggleButtons = document.querySelectorAll('.toggle-attributes');
toggleButtons.forEach(button => {
button.addEventListener('click', () => {
    const attributes = button.nextElementSibling;
    attributes.classList.toggle('show-attributes');
});
});
