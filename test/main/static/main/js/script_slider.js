$('.slider').slick({
    infinite: true,
    arrows: true,
    dots: true,
	centerMode: true,
	centerPadding: '12%',
	slidesToShow: 1,
	speed: 900,
    autoplay: true,
    autoplaySpeed: 4500,
    
    responsive: [
        {
            breakpoint: 1000,
            settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '6%',
                slidesToShow: 1
            }
        },
        {
            breakpoint: 480,
            settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '40px',
                slidesToShow: 1
            }
        }
    ]
});

$('.slider_card').slick({
    dots: true,
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    responsive: [
        {
            breakpoint: 1100,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 1,
                infinite: true,
                arrows: false
                //  dots: false
            }
        },
        {
            breakpoint: 900,
            settings: {
                slidesToShow: 2,
                arrows: false,
                infinite: true,
                slidesToScroll: 1
            }
        },
        {
            breakpoint: 620,
            settings: {
                slidesToShow: 1,
                arrows: false,
                infinite: true,
                slidesToScroll: 1
            }
        }
        // You can unslick at a given breakpoint now by adding:
        // settings: "unslick"
        // instead of a settings object
    ]
});

