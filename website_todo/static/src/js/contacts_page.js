
// Second section

let currentSlide = 0;
const totalSlides = document.querySelectorAll('.carousel-slide').length - 3;

function updateSlides() {

    const carouselWrapper = document.querySelector('.carousel-wrapper');
    const slideWidth = document.querySelector('.carousel-slide').clientWidth;
    const offset = -slideWidth * currentSlide + (carouselWrapper.clientWidth - (slideWidth * 4)) / 2;

    carouselWrapper.style.transform = `translateX(${offset}px)`;
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % totalSlides;
    updateSlides();
}

function prevSlide() {
    currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    updateSlides();
}


// Fifth section

let currentAccordionItem = 0;
const items = document.querySelectorAll('.fifth_section_accordion_item');
const headers = document.querySelectorAll('.fifth_section_accordion_header');

headers.forEach(header => {
    header.addEventListener('click', function() {
        changeAccordionItem(header);
    });
});

function changeAccordionItem(element) {
    const parentElement = element.parentElement;
    const isOpen = parentElement.classList.contains('open');
    
    document.querySelectorAll('.fifth_section_accordion_item').forEach(c => {
        c.classList.remove('open');
    });
    
    if (!isOpen) {
        parentElement.classList.add('open');
    }
}





document.addEventListener('DOMContentLoaded', function() {
    updateSlides();
    changeAccordionItem(headers[0]);
});