console.log("main.js 가 제대로 연결 되었습니다.")

const thisYear = document.querySelector('.this-year');
thisYear.textContent = new Date().getFullYear();


const searchEl = document.querySelector('.search');
const searchInputEl = searchEl.querySelector('input');

searchEl.addEventListener('click', function () {
    // Logic
    searchInputEl.focus();
})

searchInputEl.addEventListener('focus', function () {
    searchEl.classList.add('focused');
    searchInputEl.setAttribute('placeholder', '통합검색');
});

searchInputEl.addEventListener('blur', function () {
    searchEl.classList.remove('focused');
    searchInputEl.setAttribute('placeholder', '');
});

const fadeEls = document.querySelectorAll('.visual .fade-in');
console.log(fadeEls)
const aa = document.querySelector('.visual .k')
console.log(aa)
fadeEls.forEach(function (fadeEl, index) {
    // gsap.to(요소, 지속시간, 옵션);
    gsap.to(fadeEl, 1, {
        delay: (index + 1) * .7,  // 0.7, 1.4, 2.1, 2.7
        opacity: 1
    });
});

// 범위 랜덤 함수(소수점 2자리까지)
function random(min, max) {
    // `.toFixed()`를 통해 반환된 문자 데이터를,
    // `parseFloat()`을 통해 소수점을 가지는 숫자 데이터로 변환
    return parseFloat((Math.random() * (max - min) + min).toFixed(2))
}
function floatingObject (selector, delay, size) {
    // gsap.to(요소, 시간, 옵션);
    gsap.to(
        selector,  // 선택자
        delay,
        // random(1.5, 2.5),  // 애니메이션 동작 시간
        {  // 옵션
        y: size,
        repeat: -1,  // 무한반복
        yoyo: true,  // 애니메이션이 진행이 되고 다시 돌아오는
        ease: Power1.easeInOut,  // gsap Easing
        delay: delay
    });
}
floatingObject('.floating', 1, 20);
floatingObject('.floating2', 2, 200);
