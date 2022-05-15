$(function () {
	var $entries = $("#entries");
	var counter = 0;
	var user_username = "JamesXMM123"
	$.ajax({
	  type: "Get",
	  url: "http://localhost:5009/booking/booking_by_username/" + user_username,
	  success: function (booking) {
		booking = booking.data;
		console.log(booking)
		$.each(booking, function (i, code) {
		  var $output = booking;
		  console.log(booking);
		  console.log(counter);
  
		  $entries.append(
			'<tr id="row' + $output[counter].booking_id +
			'" class="row100 body"> <td class="cell100 column1"> ' +
			  $output[counter].booking_id +
			  '</td> <td class="cell100 column2">' +
			  $output[counter].booking_date +
			  '</td> <td class="cell100 column4"> ' +
			  $output[counter].booking_time +
			  '</td> <td class="cell100 column5">Approved <br>' +
			  "<button class='delete_class' style='color: red'> Click to cancel booking </button>" +
			  '</td > </tr>'
		  );
		  console.log(counter);
  
		  counter += 1;
		});
	  },
	});

	// any time any element with the 'delete_class' on it is clicked, then
	$(document).on('click', '.delete_class', function(e) {
		var row = $(this).closest('tr');
	
		console.log(row[0].id.slice(3))
		
		to_delete = row[0].id.slice(3)

		$.ajax({

			type:'DELETE',
			url: "http://localhost:5009/booking/delete_booking/" + to_delete,
			success: function(result) {
				// Do something with the result
				window.alert("Booking Cancelled")
				location.reload();
				
			}

		});
	});



});
  