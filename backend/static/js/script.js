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
	let ut = $('#user_time').val()
	console.log(ut);
	if(ut){
		ut=parseInt(ut)*1000;
		let dt = new Date(ut);
		console.log(ut);
		dt = dt.setHours(dt.getHours()+tz)
		dt = new Date(dt).toLocaleString();
		console.log('dt',dt);
		let date = dt.substr(0,9);
		let time = dt.substr(-11)
		console.log(time);
		console.log(date);
		console.log(dt);
		$('#event_timer').val(time)
		$('#start_date').val(date)
	}
	$('#schedule').submit( () => {
		let date = $('#start_date').val()
		let time = $('#event_timer').val()
		if(date.length <= 1){
			return false;
		}
		let ts = new Date(`${date} ${time}`).getTime();
		$('#user_time').val(ts);
		return true;
	});
});
