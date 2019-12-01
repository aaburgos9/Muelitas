/**
 * funcion para el uso de ventanas modales
 */
function abrir_modal(url) {
$('#ventana_modal').load(url, function () {
    $(this).modal({
        backdrop: 'static',
        keyboard: false
    })
    $(this).modal('show');
});
return false;
}
function cerrar_modal() {
$('#ventana_modal').modal('hide');
return false;
}


// Scrolling Effect navbar
$(window).on("scroll", function() {
    if($(window).scrollTop()) {
          $('nav').addClass('black');
    }

    else {
          $('nav').removeClass('black');
    }
});







//validaciones
$(document).ready(function(){
    $('#documento').on('input', function () { 
        this.value = this.value.replace(/[^0-9]/g,'');
    });
    
});


function validar() {
    var document, nombre, password, correo;
    Documento = document.getElementById("Documento").value;
    Nombre = document.getElementById("Nombre").value;
    Password = document.getElementById("Password").value;
    Correo = document.getElementById("Correo").value;

    if (Documento === "") {
        alert("el campo documento esta vacio");
        return false;
        
    }
    
    
    
}


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
