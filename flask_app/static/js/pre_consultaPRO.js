const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	raza: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	edad: /^.{4,12}$/, // 4 a 12 digitos.
	peso: /^.{4,12}$/, // 4 a 12 digitos.
	edad_adopcion: /^\d{7,14}$/, // 7 a 14 numeros.
	adquisicion: /^\d{7,14}$/, // 7 a 14 numeros.
	tiempo_madre: /^\d{7,14}$/, // 7 a 14 numeros.
	edad_calle: /^\d{7,14}$/ // 7 a 14 numeros.
}

const campos = {
	nombre: true,
	raza: true,
	edad: true,
	peso: true,
	edad_adopcion: true,
	adquisicion: true,
	tiempo_madre: true,
	edad_calle: true,
}

const validarFormulario = (e) => {
	switch (e.target.name) {
		case "nombre":
			console.log('se ejecuto nombre');
			validarCampo(expresiones.nombre, e.target, 'nombre');
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
		case "adquisicion":
			console.log('se ejecuto adquisicion');
			validarCampo(expresiones.adquisicion, e.target, 'adquisicion');
		break;
		case "tiempo_madre":
			console.log('se ejecuto tiempo_madre');
			validarCampo(expresiones.tiempo_madre, e.target, 'tiempo_madre');
		break;
		case "edad_calle":
			console.log('se ejecuto edad_calle');
			validarCampo(expresiones.edad_calle, e.target, 'edad_calle');
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

	// guarda el valor de la fecha de nacimiento para usarla en el if
	const fechaNacimiento = document.getElementById('nacimiento').value;

	// se le da valor de true or false para usar en el if
	const radioButtons = document.querySelectorAll('input[name="dog_or_cat"]');
    let dogOrCatSelected = false;
    radioButtons.forEach(button => {
        if (button.checked) {
            dogOrCatSelected = true;
        }
    });

	// se le da valor de true or false para usar en el if
	const radioButtons2 = document.querySelectorAll('input[name="sexo"]');
    let sexoSelected = false;
    radioButtons2.forEach(button => {
        if (button.checked) {
            sexoSelected = true;
        }
    });


    // Verifica si solo los campos sean verdaderos
    if (campos.nombre && 
		campos.raza && 
		campos.edad && 
		campos.peso && 
		campos.edad_adopcion && 
		campos.adquisicion && 
		campos.tiempo_madre && 
		campos.edad_calle && 
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

    // Verifica si solo los campos nombre y apellido son verdaderos
    if (campos.nombre && campos.raza) {
        // Incrementa el número de pasos del formulario
        formStepsNum++;
        
        // Actualiza los pasos del formulario y la barra de progreso
        updateFormSteps();
        updateProgressbar();
        
        // Loguea un mensaje
        console.log("boton escuchado 2  jaja");
    } else {
        console.log("boton2 escuchado hay false jaja");
    }
});


nextBtn3.addEventListener('click', (event) => {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    // Verifica si solo los campos nombre y apellido son verdaderos
    if (campos.nombre && campos.raza) {
        // Incrementa el número de pasos del formulario
        formStepsNum++;
        
        // Actualiza los pasos del formulario y la barra de progreso
        updateFormSteps();
        updateProgressbar();
        
        // Loguea un mensaje
        console.log("boton escuchado 3  jaja");
    } else {
        console.log("boton3 escuchado hay false jaja");
    }
});

nextBtn4.addEventListener('click', (event) => {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    // Verifica si solo los campos nombre y apellido son verdaderos
    if (campos.nombre && campos.raza) {
        // Incrementa el número de pasos del formulario
        formStepsNum++;
        
        // Actualiza los pasos del formulario y la barra de progreso
        updateFormSteps();
        updateProgressbar();
        
        // Loguea un mensaje
        console.log("boton escuchado 4  jaja");
    } else {
        console.log("boton4 escuchado hay false jaja");
    }
});

submitBtn.addEventListener('click', (event) => {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente

    // Verifica si solo los campos nombre y apellido son verdaderos
    if (campos.nombre && campos.raza) {
        // Incrementa el número de pasos del formulario
        formStepsNum++;
        
        // Actualiza los pasos del formulario y la barra de progreso
        updateFormSteps();
        updateProgressbar();
        
        // Loguea un mensaje
        console.log("boton escuchado 5  jaja");
    } else {
        console.log("boton5 escuchado hay false jaja");
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
