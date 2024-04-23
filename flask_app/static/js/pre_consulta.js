

$(document).ready(function(){
    
    var current_fs, next_fs, previous_fs; //fieldsets
    var opacity;
    
    $(".next").click(function(){
        
        current_fs = $(this).parent();
        next_fs = $(this).parent().next();
        
        //Add Class Active
        $("#progressbar li").eq($("fieldset").index(next_fs)).addClass("active");
        
        //show the next fieldset
        next_fs.show(); 
        //hide the current fieldset with style
        current_fs.animate({opacity: 0}, {
            step: function(now) {
                // for making fielset appear animation
                opacity = 1 - now;
    
                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                next_fs.css({'opacity': opacity});
            }, 
            duration: 600
        });
    });
    
    $(".previous").click(function(){
        
        current_fs = $(this).parent();
        previous_fs = $(this).parent().prev();
        
        //Remove class active
        $("#progressbar li").eq($("fieldset").index(current_fs)).removeClass("active");
        
        //show the previous fieldset
        previous_fs.show();
    
        //hide the current fieldset with style
        current_fs.animate({opacity: 0}, {
            step: function(now) {
                // for making fielset appear animation
                opacity = 1 - now;
    
                current_fs.css({
                    'display': 'none',
                    'position': 'relative'
                });
                previous_fs.css({'opacity': opacity});
            }, 
            duration: 600
        });
    });
    
    $('.radio-group .radio').click(function(){
        $(this).parent().find('.radio').removeClass('selected');
        $(this).addClass('selected');
    });
    
    $(".submit").click(function(){
        return false;
    })
        
    });





$(document).ready(function(){
    $('#msform').validate({
        //console.log("empieza la validacion")
        errorPlacement: function(error, element) {
        element.before(error);
        },
        rules: {
            nombre_mas : {
                required: true,
                minlength: 3
            },
            dog_or_cat : {
                required: true
            },
            raza : {
                required: true,
                minlength: 3
            }, 
            fecha_nac: {
                required: true
            },
            edad : {
                required: true,
                minlength:3
            },
            peso : {
                required: true,
                minlength: 3
            },
            sexo : {
                required: true
            },
            edad_adopcion: {
                required: true
            }, 
            donde_adquisicion: {
                required: true
            }, 
            tiempo_con_madre_hrnos: {
                required: true
            }, 
            momento_salida_a_calle: {
                required: true
            }
        },
        messages: {
            nombre_mas: {
                minlength: "El nombre de la mascota debería tener al menos 3 caracteres"
            },
            dog_or_cat: {
                required: "Seleccione una opción"
            },
            raza: {
                required: "Ingrese la raza de su mascota"
            },
            fecha_nac: {
                required: "Ingrese la fecha de nacimiento de su mascota"
            },
            edad: {
                required: "Ingrese la edad de su mascota"
            },
            peso: {
                required: "Ingrese el peso de su mascota"
            },
            sexo: {
                required: "Seleccione una opción"
            },
            edad_adopcion: {
                required: "Ingrese la edad de adopción de su mascota"
            },
            donde_adquisicion: {
                required: "Ingrese donde adquirió a su mascota "
            },
            tiempo_con_madre_hrnos: {
                required: "Ingrese hasta qué edad su mascota estuvo con su madre/hermanos"
            },
            momento_salida_a_calle: {
                required: "Ingrese a qué edad su mascota salió a la calle"
            }
        },
        submitHandler: function(form) {
        form.submit();
        }
    });

    $('#msform input').keyup(function(){
        $(this).valid();
    });
    
    $('.next').click(function(){
        var form = $('#msform') //$(this).closest('form');
        console.log("siguiente")
        if (form.valid()) {
            console.log("valido!")
            $(this).closest('fieldset').removeClass('active').next().addClass('active');
        }
    });
    
    $('.previous').click(function(){
        $(this).closest('fieldset').removeClass('active').prev().addClass('active');
    });
});




/* Prueba de validacion 
$(document).click(function() {
    if($("#msform".valid) == false) {
        return;
    }
    let nombre_mas = $("#nombre_mas").val()
    let dog_or_cat = $("#dog_or_cat").is(":checked")
    let raza = $("#raza").val()
    let fecha_nac = $("#fecha_nac").val()
    let edad = $("#edad").val()
    let peso = $("#peso").val()
    let sexo = $("#sexo").val()
    let edad_adopcion = $("#edad_adopcion").val()
    let donde_adquisicion = $("#donde_adquisicion").val()
    let tiempo_con_madre_hrnos = $("#tiempo_con_madre_hrnos").val()
    let momento_salida_a_calle = $("#momento_salida_a_calle").val()   

})

/*
$(document).ready(function() {
    $("msform").validate({
        rules: {
            
        messages: {
            nombre_mas: {
                required: "Introduce el nombre"
            },
            dog_or_cat: {
                required: "Perro o gato"
            }
        }
    });
});
*/

/*

$(document).ready(function() {
    $("#basic-form").validate({
    rules: {
    name : {
        required: true,
        minlength: 3
    },
    age: {
        required: true,
        number: true,
        min: 18
    },
    email: {
        required: true,
        email: true
    },
    weight: {
        required: {
        depends: function(elem) {
            return $("#age").val() > 50
        }
        },
        number: true,
        min: 0
    }
    },
    messages : {
    name: {
        minlength: "Name should be at least 3 characters"
    },
    age: {
        required: "Please enter your age",
        number: "Please enter your age as a numerical value",
        min: "You must be at least 18 years old"
    },
    email: {
        email: "The email should be in the format: abc@domain.tld"
    },
    weight: {
        required: "People with age over 50 have to enter their weight",
        number: "Please enter your weight as a numerical value"
    }
    }
});
});


$( document ).ready(function() {
    $(‘pre_consulta’).submit(function(e) {
        e.preventDefault();
    }).validate({
    debug: false,
    rules: {
    “nombre_mas”: {
    required: true
    },
    “dog_or_cat”: {
    required: true
    },
    “surname2”: {
    required: true
    },
    “email”: {
    required: true,
    email: true
    },
    “cpostal”: {
    required: true,
    number:true,
    minlength: 5,
    maxlength: 5
    }
    },
    messages: {
    “name”: {
    required: “Introduce tu nombre.”
    },
    “surname”: {
    required: “Apellido obligatorio.”
    },
    “surname2”: {
    required: “Apellido obligatorio.”
    },
    “email”: {
    required: “Introduce tu correo.”,
    email: “”
    },
    “cpostal”: {
    required: “Introduce tu código postal.”,
    number: “Introduce un código postal válido.”,
    maxlength: “Debe contener 5 dígitos.”,
    minlength: “Debe contener 5 dígitos.”
    }
    }
    
    });
    });
    
    */