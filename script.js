const imageUrlInput = document.getElementById("imageUrl");
const addImageButton = document.getElementById("addImage");
const deleteImageButton = document.getElementById("deleteImage");
const gallery = document.getElementById("gallery");

let selectedImage = null;

// Agregar imagen
addImageButton.addEventListener("click", () => {
    const imageUrl = imageUrlInput.value.trim();

    if (imageUrl === "") {
        alert("Por favor ingrese una URL válida.");
        return;
    }

    const img = document.createElement("img");
    img.src = imageUrl;

    img.addEventListener("click", () => {
        selectImage(img);
    });

    // Manejo de error
    img.onerror = () => {
        alert("La URL ingresada no corresponde a una imagen válida.");
        img.remove();
    };

    gallery.appendChild(img);
    imageUrlInput.value = "";
});

// Seleccionar imagen
function selectImage(img) {
    if (selectedImage) {
        selectedImage.classList.remove("selected");
    }

    selectedImage = img;
    selectedImage.classList.add("selected");
}

// Eliminar imagen seleccionada
deleteImageButton.addEventListener("click", () => {
    if (!selectedImage) {
        alert("No hay ninguna imagen seleccionada.");
        return;
    }

    selectedImage.style.opacity = "0";
    setTimeout(() => {
        gallery.removeChild(selectedImage);
        selectedImage = null;
    }, 300);
});

// Atajo de teclado
document.addEventListener("keydown", (event) => {
    if (event.key === "Delete" && selectedImage) {
        gallery.removeChild(selectedImage);
        selectedImage = null;
    }
});

