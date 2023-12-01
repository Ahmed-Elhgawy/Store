$(document).ready(function(){
    // for mobile
    $('.bar-sec').on('click', () => {
        $('#side-bar').toggleClass('display');
        $('#bar').toggleClass('rotate')
    });
    
    
    // toggle theme
    $('.dark-mode').on('click', () => {
        $('*').toggleClass('dark-theme');
    });
    
    // Slide bar
    $('.slider').slick({
        autoplay: true,
        autoplaySpeed: 3000,
        centerMode: true,
        centerPadding: '60px',
        slidesToShow: 3,
        responsive: [
            {
            breakpoint: 850,
            settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '40px',
                slidesToShow: 1
            }
            },
            {
            breakpoint: 600,
            settings: {
                arrows: false,
                centerMode: true,
                centerPadding: '40px',
                slidesToShow: 1
            }
            }
        ]
    });

    // Login & Register
    $('#myTabs a').on('click', function (e) {
        e.preventDefault()
        $(this).tab('show')
        });

    // Add your login and register form submission logic here
    $('#loginForm').submit(function(e){
        e.preventDefault();
        // Add your login logic
        console.log('Login clicked');
    });

    $('#registerForm').submit(function(e){
        e.preventDefault();
        // Add your register logic
        console.log('Register clicked');
    });
    
});

