// Capturamos los elementos del formulario
const nombre = document.getElementById("nombre");
const correo = document.getElementById("correo");
const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");
const edad = document.getElementById("edad");
const btnEnviar = document.getElementById("btnEnviar");

// Expresión regular para validar correo
const regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// Expresión regular para contraseña
// Al menos 8 caracteres, un número y un carácter especial
const regexPassword = /^(?=.*[0-9])(?=.*[!@#$%^&*])/;

// Función para validar todo el formulario
function validarFormulario() {
    if (
        validarNombre() &&
        validarCorreo() &&
        validarPassword() &&
        validarConfirmPassword() &&
        validarEdad()
    ) {
        btnEnviar.disabled = false; // Habilita el botón
    } else {
        btnEnviar.disabled = true; // Deshabilita el botón
    }
}

// Validación del nombre
function validarNombre() {
    if (nombre.value.length >= 3) {
        nombre.className = "valido";
        errorNombre.textContent = "";
        return true;
    } else {
        nombre.className = "invalido";
        errorNombre.textContent = "Debe tener al menos 3 caracteres";
        return false;
    }
}

// Validación del correo
function validarCorreo() {
    if (regexCorreo.test(correo.value)) {
        correo.className = "valido";
        errorCorreo.textContent = "";
        return true;
    } else {
        correo.className = "invalido";
        errorCorreo.textContent = "Correo electrónico no válido";
        return false;
    }
}

// Validación de la contraseña
function validarPassword() {
    if (password.value.length >= 8 && regexPassword.test(password.value)) {
        password.className = "valido";
        errorPassword.textContent = "";
        return true;
    } else {
        password.className = "invalido";
        errorPassword.textContent =
            "Mínimo 8 caracteres, un número y un carácter especial";
        return false;
    }
}

// Validación de confirmación de contraseña
function validarConfirmPassword() {
    if (confirmPassword.value === password.value && confirmPassword.value !== "") {
        confirmPassword.className = "valido";
        errorConfirmPassword.textContent = "";
        return true;
    } else {
        confirmPassword.className = "invalido";
        errorConfirmPassword.textContent = "Las contraseñas no coinciden";
        return false;
    }
}

// Validación de edad
function validarEdad() {
    if (edad.value >= 18) {
        edad.className = "valido";
        errorEdad.textContent = "";
        return true;
    } else {
        edad.className = "invalido";
        errorEdad.textContent = "Debe ser mayor o igual a 18 años";
        return false;
    }
}

// Eventos para validaciones dinámicas (tiempo real)
nombre.addEventListener("input", validarFormulario);
correo.addEventListener("input", validarFormulario);
password.addEventListener("input", validarFormulario);
confirmPassword.addEventListener("input", validarFormulario);
edad.addEventListener("input", validarFormulario);

// Evento al enviar el formulario
document.getElementById("formulario").addEventListener("submit", function (e) {
    e.preventDefault(); // Evita el envío real
    alert("Formulario validado correctamente ✔️");
});
