$('#formulario2').validate({ 
    "rules": {
        "txtUsuario": {
            required: true,
            
        },
        "txtEmail": {
            required: true,
            email: true
        },
        "txtPassword": {
            required: true,
            minlength: 5
            
        },
        "txtRepetirPassword": {
            required: true,
            equalTo: '#id_txtPassword'
        }
    }, // --> Fin de reglas
    messages: {
        "txtUsuario": {
            required: 'El usuario es requerido',
            
        },
        "txtEmail": {
            required: 'El email es un campo requerido',
            email: 'El email no cumple el formato de un correo'
        },
        "txtPassword": {
            required: 'Debe ingresar una contraseña de minimo 5 caracteres',
            minlength: 'Mínimo 5 caracteres'
        },
        "txtRepetirPassword": {
            required: 'Repita la contraseña anterior',
            equalTo: 'Debe ser igual al campo Password'
        }
            
        
    },
});