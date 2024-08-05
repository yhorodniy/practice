document.addEventListener('DOMContentLoaded', () => {
    const items = document.querySelectorAll('.fifth_section_accordion_item');
    const headers = document.querySelectorAll('.fifth_section_accordion_header');

    headers.forEach(header => {
        header.addEventListener('click', () => {
            const element = header.parentElement;
            const isOpen = element.classList.contains('open');

            document.querySelectorAll('.fifth_section_accordion_item').forEach(c => {
                c.classList.remove('open');
            });

            if (!isOpen) {
                element.classList.add('open');
            }
        });
    });
});