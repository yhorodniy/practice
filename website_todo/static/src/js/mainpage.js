const showMoreBtn = document.querySelector('#sixth_section_show_more_btn');

showMoreBtn.addEventListener('click', () => {
    const showMoreContent = document.querySelector('#sixth_section_hiden_content');

    if(showMoreContent.className.includes('hiden_content')) {
        showMoreContent.className = 'row sixth_section_items_wrapper';
        showMoreBtn.textContent = 'ПРИХОВАТИ КЕЙСИ...';
    } else {
        showMoreContent.className = 'row sixth_section_items_wrapper hiden_content';
        showMoreBtn.textContent = 'ПОКАЗАТИ ВСІ КЕЙСИ...';
    };
});


// Carousel seventh section

let currentSlide = 2;
const totalSlides = document.querySelectorAll('.carousel-slide').length;

function updateSlides() {
    document.querySelectorAll('.carousel-slide').forEach((slide, index) => {
        if (index === currentSlide) {
            slide.classList.add('active');
        } else {
            slide.classList.remove('active');
        }
    });

    document.querySelectorAll('.carousel-description').forEach((descr, index) => {
        if (index === currentSlide) {
            descr.classList.add('active');
        } else {
            descr.classList.remove('active');
        }
    })

    const carouselWrapper = document.querySelector('.carousel-wrapper');
    const slideWidth = document.querySelector('.carousel-slide').clientWidth;
    // const offset = -slideWidth * currentSlide + (window.innerWidth - slideWidth) / 2;
    const offset = -slideWidth * currentSlide + (carouselWrapper.clientWidth - slideWidth) / 2;

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

updateSlides();



// Carousel eighth section

let currentImg = 0;
const laptopSlideslength = document.querySelectorAll('.carousel_image').length;
const laptopSlidesBtns = document.querySelectorAll('.carousel_indicator');

laptopSlidesBtns.forEach((button, index) => {
    button.addEventListener('click', () => {
        currentImg = index;
        updateLaptopSlides();
    });
});

function updateLaptopSlides() {
    document.querySelectorAll('.carousel_image').forEach((slide, index) => {
        if (index === currentImg) {
            slide.classList.add('active');
        } else {
            slide.classList.remove('active');
        }
    });

    document.querySelectorAll('.carousel_name_wrapper').forEach((descr, index) => {
        if (index === currentImg) {
            descr.classList.add('active');
        } else {
            descr.classList.remove('active');
        };
    });

    document.querySelectorAll('.carousel_indicator').forEach((indicator, index) => {
        if (index === currentImg) {
            indicator.classList.add('active');
        } else {
            indicator.classList.remove('active');
        };
    });

};

setInterval(() => {
    if(currentImg === laptopSlideslength - 1) {
        currentImg = 0;
    } else {
        currentImg += 1;
    }
    updateLaptopSlides();
}, 5000)
