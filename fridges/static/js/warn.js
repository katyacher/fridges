function warn () {
	var td =  document.getElementsByTagName("td"); //коллекция элементов таблицы
	 for (var i = 0; i < td.length; i++) {
   		var warn = td[i].innerHTML;
			if (warn == 'Warning') {
			td[i].style.background = '#ffb3b3';	//выделяем цветом ячеки со значением warning
		} else {
						//alert(warn);
			}; 
   }
}