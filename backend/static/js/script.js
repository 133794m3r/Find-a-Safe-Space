$('body').ready( () => {
	$('.datepicker').datepicker({
			calendarWeeks: true,
			todayHighlight: true
	})
	// let d = new Date();
	// let h = d.getHours() -4;
	// h = (h <= 0)?h+24:h;
	let tz = new Date().getTimezoneOffset()/60
	$('#event_timer').timepicker();
	$('#user_tz').val(tz);

});
