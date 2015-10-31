"use strict";
function validEmail(mail){

    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;

    return re.test(mail);


}
function send_mail(){
	 var fname='', mail='';
	 
	  fname=$('#fname').val();
	  mail=$('#uemail').val();
	 
	 if((fname=='')) 		 $('#form-errors').text('Queremos saber seu nome !');
	 else if(mail=='')		 $('#form-errors').text('Precisamos do seu e-mail !');
	 else if(!(validEmail(mail)))	 $('#form-errors').text('Acho que o e-mail está incorreto !');
	 else{
		  $.ajax({
			url:'ajaxmail.php',
			type:'POST',
			data:{ 'fname':fname,
				   'uemail':mail
				  },
			dataType:'json',
			success:function(response){ 
						if(response.success){ 
							$('#form-errors').text('');
							$('#form-success').text('Your request is received, Thank You !'); 
							$('#fname').val('');
							$('#uemail').val('');
							}
						else{ $('#form-errors').text('Request failed.Please retry with all the required details !'); } 
					},
			error:function(){ }
		 });
		 
		 }
	  
	 }
 $(function() {
$('.scrollto, .gototop').on('click',function(event){
		 var $anchor = $(this);
		 $('html, body').stop().animate({
         scrollTop: $($anchor.attr('href')).offset().top
          }, 1500,'easeInOutExpo');
     event.preventDefault();
      });
});
