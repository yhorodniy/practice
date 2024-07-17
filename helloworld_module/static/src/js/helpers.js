// Modal open / close

document.addEventListener('DOMContentLoaded', () => {
    const getDemoBtn = document.querySelectorAll('#get-demo-btn');
    const getPresentation = document.querySelectorAll('#get-presentation-btn');
    
    const closeDemoBtn = document.querySelectorAll('#close-btn');
    const modalDialogMenu = document.querySelector('#dialog_form')
    const contactUsModalMenu = document.querySelector('#contact_modal_form');
    
    const openCloseModalGetDemo = (event) => {
        if(event.target.id === 'get-demo-btn') {
            modalDialogMenu.className = 'dialog_bg';
        } else if(event.target.id === 'get-presentation-btn') {
            contactUsModalMenu.className = 'dialog_bg';
        } else {
            modalDialogMenu.className = 'dialog_bg d-none';
            contactUsModalMenu.className = 'dialog_bg d-none';
        }
    };
    
    getDemoBtn.forEach(button => button.addEventListener('click', openCloseModalGetDemo));
    getPresentation.forEach(button => button.addEventListener('click', openCloseModalGetDemo));
    closeDemoBtn.forEach(button => button.addEventListener('click', openCloseModalGetDemo));
})
