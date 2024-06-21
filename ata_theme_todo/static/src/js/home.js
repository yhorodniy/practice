initSwiper();
window.addEventListener("orientationchange", (event) => {
    initSwiper();
});

var swiperClient;

function initSwiper() {
    if ((navigator.userAgent.includes("Android") || navigator.userAgent.includes("iPhone")) && screen.orientation.type.includes("portrait")) {

        swiperClient = new Swiper('.swiper-container-client', {
            slidesPerView: 1,
            loop: true,
            centeredSlides: true
        });

    } else if ((navigator.userAgent.includes("Android") || navigator.userAgent.includes("iPhone")) && screen.orientation.type.includes("landscape")) {

        swiperClient = new Swiper('.swiper-container-client', {
            slidesPerView: 5,
            loop: true,
            centeredSlides: true
        });

    } else {

        swiperClient = new Swiper('.swiper-container-client', {
            slidesPerView: 5,
            loop: true,
            centeredSlides: true,
            navigation: {
                nextEl: '.swiper-button-next-client',
                prevEl: '.swiper-button-prev-client',
            }
        });
    }

    swiperClient.on('slideChange', (event) => {
        let children = Array.from(document.getElementById("clientDescription").children);
        children.map(x => {
            if (!x.classList.contains("hide")) {
                x.classList.add("hide");
            }
        })
        children[event.realIndex].classList.remove("hide");
    });

}