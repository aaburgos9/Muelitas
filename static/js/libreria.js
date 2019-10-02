// Scrolling Effect
$(window).on("scroll", function() {
    if($(window).scrollTop()) {
          $('nav').addClass('black');
    }

    else {
          $('nav').removeClass('black');
    }
});

$(document).ready(function(){
    $('#documento').on('input', function () { 
        this.value = this.value.replace(/[^0-9]/g,'');
    });
    
});


/*$('#form-login').bootstrapValidator({
 
    
    fields: {

        documento: {

            validators: {

                notEmpty: {

                    message: 'El documento es requerido, no puede estar vacio'

                },
                
                regexp: {
 
                    regexp: /^[0-9]+$/,

                    message: 'El documento solo puede contener números'

                }

            }

        },

       

     

        password: {

            validators: {

                notEmpty: {

                    message: 'El password es requerido y no puede ser vacio'

                },

                /*stringLength: {

                    min: 8,

                    message: 'El password debe contener al menos 8 caracteres'

                }

            }

        },
    }

       

});*/
