$('#formulario1').validate({ 
    "rules": {
        "txtNombre": {
            required: true,
            
        },
        "txtEmail": {
            required: true,
            email: true
        },
        "txtMensaje": {
            required: true,
            
        }
    }, // --> Fin de reglas
    messages: {
        "txtNombre": {
            required: 'El nombre es un campo requerido',
            
        },
        "txtUsuario": {
            required: 'El usuario es requerido',
            
        },
        "txtEmail": {
            required: 'El email es un campo requerido',
            email: 'El email no cumple el formato de un correo'
        },
        "txtMensaje": {
            required: 'Debe ingresar un mensaje',
            
        }
    },
});