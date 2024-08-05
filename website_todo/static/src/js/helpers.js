// Modal open / close

document.addEventListener('DOMContentLoaded', () => {
    const getCallbackBtn = document.querySelectorAll('#get-callback-btn');
    const getDemoBtn = document.querySelectorAll('#get-demo-btn');
    const getPresentation = document.querySelectorAll('#get-presentation-btn');
    const showItemDescription = document.querySelectorAll('#show_item_description');
    
    const closeDemoBtn = document.querySelectorAll('#close-btn');
    const modalCallback = document.querySelector('#callback_modal_form');
    const modalDialogMenu = document.querySelector('#dialog_form');
    const contactUsModalMenu = document.querySelector('#contact_modal_form');
    const itemDescriptionModal = document.querySelectorAll('.dialog_item')
    
    const openCloseModalGetDemo = (event) => {
        if (event.target.id === 'get-callback-btn') {
            modalCallback.className = 'dialog_bg';
        } else if (event.target.id === 'get-demo-btn') {
            modalDialogMenu.className = 'dialog_bg';
        } else if (event.target.id === 'get-presentation-btn') {
            contactUsModalMenu.className = 'dialog_bg';
        } else if (event.target.id === 'show_item_description') {
            const currentId = event.target.parentElement.id;
            const currentDescriptionModal = Array.from(itemDescriptionModal).find(el => el.id === `${currentId}_modal`);
            
            currentDescriptionModal.parentElement.classList.remove('d-none');
            currentDescriptionModal.classList.add('content_active');
        } else {
            modalCallback.className = 'dialog_bg d-none';
            modalDialogMenu.className = 'dialog_bg d-none';
            contactUsModalMenu.className = 'dialog_bg d-none';
            itemDescriptionModal.forEach(el => {
                el.parentElement.className = 'dialog_bg d-none';
                el.className = 'dialog_item';
            });
        }
    };
    
    getCallbackBtn.forEach(button => button.addEventListener('click', openCloseModalGetDemo));
    getDemoBtn.forEach(button => button.addEventListener('click', openCloseModalGetDemo));
    getPresentation.forEach(button => button.addEventListener('click', openCloseModalGetDemo));
    showItemDescription.forEach(button => button.addEventListener('click', openCloseModalGetDemo));
    closeDemoBtn.forEach(button => button.addEventListener('click', openCloseModalGetDemo));


    const dropdownUserMenu = document.querySelectorAll('.js_usermenu i');
    dropdownUserMenu.forEach(el => el.classList.replace('text-primary', 'main-title-color'));
})
