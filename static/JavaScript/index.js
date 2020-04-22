trList = ['leftUp', 'moveRight', 'moveDown', 'centerBig', 'rightDownBig'];
            var swiper = new Swiper('.swiper-container', {
                speed: 500,
                autoplay: 4400,
                autoplayDisableOnInteraction: false,
                effect: 'fade',
                pagination: '.swiper-pagination',
                paginationClickable: true,
                onSlideChangeStart: function(swiper) {
                    nextSlide = swiper.slides.eq(swiper.activeIndex);
                    nextSlide.addClass(trList[Math.floor(Math.random() * 5)]);
                },
                onSlideChangeEnd: function(swiper) {
                    prevSlide = swiper.slides[swiper.previousIndex];
                    prevSlide.className = "swiper-slide";
                },
            });