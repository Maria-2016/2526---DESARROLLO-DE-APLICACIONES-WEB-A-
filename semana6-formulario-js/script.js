// Captura de los elementos del formulario
const nombre = document.getElementById("nombre");
const correo = document.getElementById("correo");
const password = document.getElementById("password");
const confirmar = document.getElementById("confirmar");
const edad = document.getElementById("edad");
const enviar = document.getElementById("enviar");

// 🔹 Validación del nombre (mínimo 3 caracteres)
function validarNombre() {
    if (nombre.value.length >= 3) {
        nombre.className = "valido";
        document.getElementById("errorNombre").textContent = "";
        return true;
    } else {
        nombre.className = "invalido";
        document.getElementById("errorNombre").textContent =
            "El nombre debe tener al menos 3 caracteres";
        return false;
    }
}

// 🔹 Validación del correo usando expresión regular
function validarCorreo() {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (regex.test(correo.value)) {
        correo.className = "valido";
        document.getElementById("errorCorreo").textContent = "";
        return true;
    } else {
        correo.className = "invalido";
        document.getElementById("errorCorreo").textContent =
            "Formato de correo incorrecto";
        return false;
    }
}

// 🔹 Validación de la contraseña
function validarPassword() {
    const regex = /^(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}$/;
    if (regex.test(password.value)) {
        password.className = "valido";
        document.getElementById("errorPassword").textContent = "";
        return true;
    } else {
        password.className = "invalido";
        document.getElementById("errorPassword").textContent =
            "Debe tener 8 caracteres, un número y un carácter especial";
        return false;
    }
}

// 🔹 Confirmación de contraseña
function validarConfirmacion() {
    if (password.value === confirmar.value && confirmar.value !== "") {
        confirmar.className = "valido";
        document.getElementById("errorConfirmar").textContent = "";
        return true;
    } else {
        confirmar.className = "invalido";
        document.getElementById("errorConfirmar").textContent =
            "Las contraseñas no coinciden";
        return false;
    }
}

// 🔹 Validación de la edad
function validarEdad() {
    if (edad.value >= 18) {
        edad.className = "valido";
        document.getElementById("errorEdad").textContent = "";
        return true;
    } else {
        edad.className = "invalido";
        document.getElementById("errorEdad").textContent =
            "Debe ser mayor o igual a 18 años";
        return false;
    }
}

// 🔹 Validación general del formulario
function validarFormulario() {
    if (
        validarNombre() &&
        validarCorreo() &&
        validarPassword() &&
        validarConfirmacion() &&
        validarEdad()
    ) {
        // Si todo es válido, se habilita el botón enviar
        enviar.disabled = false;
    } else {
        enviar.disabled = true;
    }
}

// 🔹 Eventos en tiempo real (validaciones dinámicas)
nombre.addEventListener("input", validarFormulario);
correo.addEventListener("input", validarFormulario);
password.addEventListener("input", validarFormulario);
confirmar.addEventListener("input", validarFormulario);
edad.addEventListener("input", validarFormulario);

// 🔹 Evento al enviar el formulario
document.getElementById("formulario").addEventListener("submit", function (e) {
    e.preventDefault(); // Evita el envío real
    alert("Formulario enviado correctamente ✅");
});
