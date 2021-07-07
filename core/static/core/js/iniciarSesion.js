$('#formulario3').validate({ 
    "rules": {
        "txtUsuario": {
            required: true,
            
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
        "txtPassword": {
            required: 'Debe ingresar una contraseña de minimo 5 caracteres',
            minlength: 'Mínimo 5 caracteres'
        },
        
            
        
    },
});