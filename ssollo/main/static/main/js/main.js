
//выезжающий мобильный фильтр
function diplay_hide(block_id) {
 if ($(block_id).css('display') == 'none') {
	$(block_id).animate({ height: 'show' }, 500);
	}
	else {
	$(block_id).animate({ height: 'hide' }, 500);
	}
}
//плагин для прокрутки вверх
jQuery(document).ready(function(){jQuery.goup();});

//lazy loading
let images = document.querySelectorAll("img");
    lazyload(images);