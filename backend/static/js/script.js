$('body').ready( () => {
	$('.datepicker').datepicker({
			calendarWeeks: true,
			todayHighlight: true
	})
	// let d = new Date();
	// let h = d.getHours() -4;
	// h = (h <= 0)?h+24:h;
	$('#event_timer').timepicker();
});
