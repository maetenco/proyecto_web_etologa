const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
	nombre_mas: /^.{2,255}$/, // todo tipo de caracteres
	raza: /^.{3,255}$/, 
	edad: /^.{4,255}$/, 
	peso: /^.{2,255}$/, 
	edad_adopcion: /^.{2,255}$/, 
	donde_adquisicion: /^.{4,255}$/, 
	tiempo_con_madre_hrnos: /^.{2,255}$/, 
	momento_salida_a_calle: /^.{2,255}$/, 

	nom_fecha_ultima_vac: /^.{6,255}$/, 
	nom_fecha_antiparasitario: /^.{6,255}$/, 
	fecha_castracion: /^.{2,255}$/, 
	motivo_castracion: /^.{2,255}$/, 

	tipo_alimentacion: /^.{6,255}$/, 
	motivo_entrenamiento: /^.{6,255}$/, 

	diagnostico: /^.{2,255}$/, 
	problema_fisico: /^.{2,255}$/, 
	medicamentos: /^.{2,255}$/, 

	motivo_consulta: /^.{6,255}$/, 
	otra_mascota: /^.{2,255}$/ 
}

const campos = {
	nombre_mas: false,
	raza: false,
	edad: false,
	peso: false,
	edad_adopcion: false,
	donde_adquisicion: false,
	tiempo_con_madre_hrnos: false,
	momento_salida_a_calle: false,

	nom_fecha_ultima_vac: false,
	nom_fecha_antiparasitario: false,
	fecha_castracion: false,
	motivo_castracion: false,

	tipo_alimentacion: false,
	motivo_entrenamiento: false,

	diagnostico: false,
	problema_fisico: false,
	medicamentos: false,

	motivo_consulta: false,
	otra_mascota: false,
}

const validarFormulario = (e) => {
	switch (e.target.name) {
		case "nombre_mas":
			console.log('se ejecuto nombre_mas');
			validarCampo(expresiones.nombre_mas, e.target, 'nombre_mas');
		break;
		case "raza":
			console.log('se ejecutp raza');
			validarCampo(expresiones.raza, e.target, 'raza');
		break;
		case "edad":
			console.log('se ejecutp edad');
			validarCampo(expresiones.edad, e.target, 'edad');
		break;
		case "peso":
			console.log('se ejecutp peso');
			validarCampo(expresiones.peso, e.target, 'peso');
		break;
		case "edad_adopcion":
			console.log('se ejecuto edad_adopcion');
			validarCampo(expresiones.edad_adopcion, e.target, 'edad_adopcion');
		break;
		case "donde_adquisicion":
			console.log('se ejecuto donde_adquisicion');
			validarCampo(expresiones.donde_adquisicion, e.target, 'donde_adquisicion');
		break;
		case "tiempo_con_madre_hrnos":
			console.log('se ejecuto tiempo_con_madre_hrnos');
			validarCampo(expresiones.tiempo_con_madre_hrnos, e.target, 'tiempo_con_madre_hrnos');
		break;
		case "momento_salida_a_calle":
			console.log('se ejecuto momento_salida_a_calle');
			validarCampo(expresiones.momento_salida_a_calle, e.target, 'momento_salida_a_calle');
		break;
		case "nom_fecha_ultima_vac":
			console.log('se ejecuto nom_fecha_ultima_vac');
			validarCampo(expresiones.nom_fecha_ultima_vac, e.target, 'nom_fecha_ultima_vac');
		break;
		case "nom_fecha_antiparasitario":
			console.log('se ejecuto nom_fecha_antiparasitario');
			validarCampo(expresiones.nom_fecha_antiparasitario, e.target, 'nom_fecha_antiparasitario');
		break;
		case "fecha_castracion":
			console.log('se ejecuto fecha_castracion');
			validarCampo(expresiones.fecha_castracion, e.target, 'fecha_castracion');
		break;
		case "motivo_castracion":
			console.log('se ejecuto motivo_castracion');
			validarCampo(expresiones.motivo_castracion, e.target, 'motivo_castracion');
		break;
		case "tipo_alimentacion":
			console.log('se ejecuto tipo_alimentacion');
			validarCampo(expresiones.tipo_alimentacion, e.target, 'tipo_alimentacion');
		break;
		case "motivo_entrenamiento":
			console.log('se ejecuto motivo_entrenamiento');
			validarCampo(expresiones.motivo_entrenamiento, e.target, 'motivo_entrenamiento');
		break;
		case "diagnostico":
			console.log('se ejecuto diagnostico');
			validarCampo(expresiones.diagnostico, e.target, 'diagnostico');
		break;
		case "problema_fisico":
			console.log('se ejecuto problema_fisico');
			validarCampo(expresiones.problema_fisico, e.target, 'problema_fisico');
		break;
		case "medicamentos":
			console.log('se ejecuto medicamentos');
			validarCampo(expresiones.medicamentos, e.target, 'medicamentos');
		break;
		case "motivo_consulta":
			console.log('se ejecuto motivo_consulta');
			validarCampo(expresiones.motivo_consulta, e.target, 'motivo_consulta');
		break;
		case "otra_mascota":
			console.log('se ejecuto otra_mascota');
			validarCampo(expresiones.otra_mascota, e.target, 'otra_mascota');
		break;
	}

	console.log('se ejecuto validar formulario');
	console.log(e.target);
}

const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
		campos[campo] = false;
	}
}



inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});




const prevBtns = document.querySelectorAll('.btn-pre')
const nextBtn1 = document.getElementById('btn-next1')
const nextBtn2 = document.getElementById('btn-next2')
const nextBtn3 = document.getElementById('btn-next3')
const nextBtn4 = document.getElementById('btn-next4')
const submitBtn = document.getElementById('btn-submit')
const progress = document.getElementById('progress')
const formSteps = document.querySelectorAll('.form-step')
const progressSteps = document.querySelectorAll('.progress-step')

let formStepsNum = 0;

nextBtn1.addEventListener('click', (event) => {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

	// guarda el valor de la fecha de fecha_nac para usarla en el if
	const fechaNacimiento = document.getElementById('fecha_nac').value;

	// se le da valor de true or false para usar en el if
	const radioButtons = document.querySelectorAll('input[name="dog_or_cat"]');
    let dogOrCatSelected = false;
    radioButtons.forEach(button => {
        if (button.checked) {
            dogOrCatSelected = true;
        }
    });

	// se le da valor de true or false al sexo para usar en el if
	const radioButtons2 = document.querySelectorAll('input[name="sexo"]');
    let sexoSelected = false;
    radioButtons2.forEach(button => {
        if (button.checked) {
            sexoSelected = true;
        }
    });


    // Verifica si solo los campos sean verdaderos
    if (campos.nombre_mas && 
		campos.raza && 
		campos.edad && 
		campos.peso && 
		campos.edad_adopcion && 
		campos.donde_adquisicion && 
		campos.tiempo_con_madre_hrnos && 
		campos.momento_salida_a_calle && 
		dogOrCatSelected && 
		fechaNacimiento !== "" && 
		sexoSelected) {
        // Incrementa el número de pasos del formulario
        formStepsNum++;
        
        // Actualiza los pasos del formulario y la barra de progreso
        updateFormSteps();
        updateProgressbar();
        
        // Loguea un mensaje
        console.log("boton escuchado 1  jaja");
    } else {
        console.log("boton1 escuchado hay false jaja");
		document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
    }
});

nextBtn2.addEventListener('click', (event) => {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    // se le da valor de true or false a castracion para usar en el if
	const radioButtons = document.querySelectorAll('input[name="castracion"]');
    let castracionSelected = false;
    radioButtons.forEach(button => {
        if (button.checked) {
            castracionSelected = true;
        }
    });


    // Verifica si solo los campos nombre_mas y apellido son verdaderos
    if (campos.nom_fecha_ultima_vac && campos.nom_fecha_antiparasitario && castracionSelected ) {
        // Incrementa el número de pasos del formulario
        formStepsNum++;
        
        // Actualiza los pasos del formulario y la barra de progreso
        updateFormSteps();
        updateProgressbar();
        
        // Loguea un mensaje
        console.log("boton escuchado 2  jaja");
    } else {
        console.log("boton2 escuchado hay false jaja");
        document.getElementById('formulario__mensaje2').classList.add('formulario__mensaje-activo');
    }
});


nextBtn3.addEventListener('click', (event) => {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    // se le da valor de true or false a tipo_alimentacion para usar en el if
	const radioButtons = document.querySelectorAll('input[name="tuvo_entrenamiento"]');
    let entrenamientoSelected = false;
    radioButtons.forEach(button => {
        if (button.checked) {
            entrenamientoSelected = true;
        }
    });




    // Verifica si solo los campos nombre_mas y apellido son verdaderos
    if (campos.tipo_alimentacion && entrenamientoSelected) {
        // Incrementa el número de pasos del formulario
        formStepsNum++;
        
        // Actualiza los pasos del formulario y la barra de progreso
        updateFormSteps();
        updateProgressbar();
        
        // Loguea un mensaje
        console.log("boton escuchado 3  jaja");
    } else {
        console.log("boton3 escuchado hay false jaja");
        document.getElementById('formulario__mensaje3').classList.add('formulario__mensaje-activo');
    }
});

nextBtn4.addEventListener('click', (event) => {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    // Verifica si solo los campos nombre_mas y apellido son verdaderos
    if (campos.diagnostico && campos.problema_fisico && campos.medicamentos) {
        // Incrementa el número de pasos del formulario
        formStepsNum++;
        
        // Actualiza los pasos del formulario y la barra de progreso
        updateFormSteps();
        updateProgressbar();
        
        // Loguea un mensaje
        console.log("boton escuchado 4  jaja");
    } else {
        console.log("boton4 escuchado hay false jaja");
        document.getElementById('formulario__mensaje4').classList.add('formulario__mensaje-activo');
    }
});

submitBtn.addEventListener('click', (event) => {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    // Verifica si solo los campos nombre_mas y apellido son verdaderos
    if (campos.motivo_consulta && campos.otra_mascota) {
        // Incrementa el número de pasos del formulario
        formStepsNum++;
        
        // Actualiza los pasos del formulario y la barra de progreso
        updateFormSteps();
        updateProgressbar();

		//ENVIAR formulario
		document.getElementById('formulario').submit();
        
        // Loguea un mensaje
        console.log("boton escuchado 5  jaja");
    } else {
        console.log("boton5 escuchado hay false jaja");
        document.getElementById('formulario__mensaje5').classList.add('formulario__mensaje-activo');
    }
});

    


prevBtns.forEach(btn =>{
    btn.addEventListener('click', ()=>{
        formStepsNum--;
        updateFormSteps();
        updateProgressbar();
    })
})


function updateFormSteps(){
    formSteps.forEach(formStep =>{
        formStep.classList.contains('active')&&
            formStep.classList.remove('active')
    })
    formSteps[formStepsNum].classList.add('active')
}

function updateProgressbar(){
    progressSteps.forEach((progressStep, idx) =>{
        if (idx < formStepsNum + 1){
            progressStep.classList.add('active')
        } else {
            progressStep.classList.remove('active')
        }
    })

    const progressActive = document.querySelectorAll('.progress-step.active')

    progress.style.width = (progressActive.length -1) / (progressSteps.length -1) * 100 + '%'
}
