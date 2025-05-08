// Header Fixed
$(window).scroll(function(){
    if ( $(this).scrollTop() > 50) {
        $(".header").addClass("fixed");
    } else {
        $(".header").removeClass("fixed");
    }
});
// Header Burgir
$(".header__burgir").click(function() {
    $(this).toggleClass("active");
    $(".header").toggleClass("active");
    $("body").toggleClass("hide");
});
$(".header__navbar li a").click(function() {
    $(".header__burgir").removeClass("active");
    $(".header").removeClass("active");
    $("body").removeClass("hide");
});
// Accordeon
$(".asked__btn").click(function() {
    $(this).toggleClass("active");
});
// Modal
$(".open-modal").click(function() {
    $(".modal").addClass("active");
    setTimeout(function() {
        $(".modal").addClass("opacity");
    },100);
    $("body").addClass("hide");
});
$(".modal__close").click(function() {
    $(".modal").removeClass("opacity");
    setTimeout(function() {
        $(".modal").removeClass("active");
    },300);
    $("body").removeClass("hide");
});
// Header Link Smooth Scrolll Down
$('.header__navbar li a, .header__logo').click(function(e){
    e.preventDefault(); // предотвращает переход по ссылке
    var target = $(this).attr('href');

    if (target && $(target).length) {
        $('html, body').animate({
            scrollTop: $(target).offset().top
        }, 800);
    }
});
// Checkbox Product
$(".services__block").click(function () {
    $(this).toggleClass("active");
});
$(".addmore__block").click(function () {
    $(this).toggleClass("active");
});
// Plus Minus
document.querySelectorAll('.counter').forEach(counter => {
    const input = counter.querySelector('input');
    const plus = counter.querySelector('.plus');
    const minus = counter.querySelector('.minus');

    plus.addEventListener('click', () => {
        input.value = parseInt(input.value) + 1;
    });

    minus.addEventListener('click', () => {
        if (parseInt(input.value) > 0) {
        input.value = parseInt(input.value) - 1;
        }
    });
});