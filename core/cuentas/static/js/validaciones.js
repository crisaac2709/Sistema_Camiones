
const username = document.getElementById('username')
const first_name = document.getElementById('first_name')
const last_name = document.getElementById('last_name')
const email = document.getElementById('email')
const password = document.getElementById('password1')
const password2 = document.getElementById('password2')
const telefono = document.getElementById('telefono')
const cedula = document.getElementById('cedula')
const fecha_nacimiento = document.getElementById('fecha_nacimiento')


let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
let passRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,20}$/;
let patron = /^\d{10}$/;


function validar(campo, longitud, mensaje_valido, mensaje_invalido) {
    const msg = campo.closest('.field').querySelector('.mensaje')
    console.log(msg);
    campo.addEventListener('input', () => {
        if (!campo.value.trim()) {
            msg.textContent = ''
            return
        }
        if (campo.value.length >= longitud) {
            msg.textContent = mensaje_valido
            msg.className = 'mensaje valido'
        } else {
            msg.textContent = mensaje_invalido
            msg.className = 'mensaje invalido'
        }
    })
}

function otra_validacion(campo, regex, mensaje_valido, mensaje_invalido) {
    const msg = campo.closest('.field').querySelector('.mensaje')
    campo.addEventListener('input', () => {
        if (!campo.value.trim()) {
            msg.textContent = ''
            return
        }
        if (regex.test(campo.value)) {
            msg.textContent = mensaje_valido
            msg.className = 'mensaje valido'
        } else {
            msg.textContent = mensaje_invalido
            msg.className = 'mensaje invalido'
        }
    })
}

function comparar(campo, password1, password2, mensaje_valido, mensaje_invalido) {
    const msg = campo.closest('.field').querySelector('.mensaje')
    campo.addEventListener('input', () => {
        if (!password2.value.trim()) {
            msg.textContent = ''
            return
        }
        if (password1.value.trim() === password2.value.trim()) {
            msg.textContent = mensaje_valido
            msg.className = 'mensaje valido'
        } else {
            msg.textContent = mensaje_invalido
            msg.className = 'mensaje invalido'
        }
    })
}

validar(first_name, 3, 'Nombre valido', 'Nombre Invalido. Minimo 3 caracteres')
validar(last_name, 3, 'Apellido valido', 'Apellido Invalido. Minimo 3 caracteres')
validar(username, 8, 'Usuario valido', 'Usuario Invalido. Minimo 8 caracteres')
otra_validacion(email, emailRegex, 'Correo valido', 'Correo invalido')
otra_validacion(password, passRegex, 'Contraseña valida', 'Min 8 caracteres, Max 20 caracteres, una mayuscula, minusculas y un numero.')
comparar(password2, password, password2, "Coinciden", "No coinciden")
otra_validacion(telefono, patron, 'Telefono valido', 'Se necesita exactamente 10 digitos')
otra_validacion(cedula, patron, 'Cedula valida', 'Se necesita exactamente 10 digitos')


fecha_nacimiento.addEventListener('input', () => {
    const hoy = new Date()
    const msg = fecha_nacimiento.closest('.field').querySelector('.mensaje')
    const fechaNacimientoDate = new Date(fecha_nacimiento.value)
    if (fechaNacimientoDate > hoy) {
        msg.textContent = 'La fecha de nacimiento no puede ser mayor a la fecha actual'
        msg.className = 'mensaje invalido'
    } else {
        msg.textContent = 'Fecha valida'
        msg.className = 'mensaje valido'
    }
})

const inputFoto = document.getElementById('foto');
const preview   = document.getElementById('preview');
inputFoto?.addEventListener('change', (e) => {
    const file = e.target.files?.[0];
    if (!file) { preview.innerHTML = ''; return; }
    const url = URL.createObjectURL(file);
    preview.innerHTML = `<img src="${url}" alt="Vista previa">`;
});


