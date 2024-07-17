// Third section

const showMoreBtn = document.querySelector('#advantages_show_more_btn');

showMoreBtn.addEventListener('click', () => {
    const showMoreContent = document.querySelector('#advantages_hiden_content');

    if(showMoreContent.className.includes('d-none')) {
        showMoreContent.className = 'odoo_advantages_list mt-5';
        showMoreBtn.textContent = 'ПОКАЗАТИ ВСІ ПУНКТИ...';
    } else {
        showMoreContent.className = 'odoo_advantages_list mt-5 d-none';
        showMoreBtn.textContent = 'ПРИХОВАТИ ПУНКТИ...';
    };
});


// Sixth section

let currentSlide = 0;
const totalSlides = document.querySelectorAll('.carousel-slide').length;

function updateSlides() {

    const carouselWrapper = document.querySelector('.carousel-wrapper');
    const slideWidth = document.querySelector('.carousel-slide').clientWidth;
    // const offset = -slideWidth * currentSlide + (window.innerWidth - slideWidth) / 2;
    const offset = -slideWidth * currentSlide + (carouselWrapper.clientWidth - (slideWidth * 4)) / 2;

    carouselWrapper.style.transform = `translateX(${offset}px)`;

    console.log(slideWidth);
    console.log(currentSlide);
    console.log(offset);
}

function nextSlide() {
    currentSlide = (currentSlide + 4) % totalSlides;
    updateSlides();
}

function prevSlide() {
    currentSlide = (currentSlide - 4 + totalSlides) % totalSlides;
    updateSlides();
}

document.addEventListener('DOMContentLoaded', function() {
    updateSlides();
});

