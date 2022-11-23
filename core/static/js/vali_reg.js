$(document).ready(function () {

    $("#formRegi").submit(function (e) {

        var rut = $("#rut").val();
        var dv = $("#dv").val();
        var uname = $("#uname").val();
        var name = $("#name").val();
        var apat = $("#apat").val();
        var amat = $("#amat").val();
        var corre = $("#corre").val();
        var pass = $("#pass").val();
        var cpass = $("#cpass").val();
      

        let mensajeMostrar = "";
        let entrar = true;

        if ((rut.toString().length > 8 || rut.toString().length < 7)) {
            mensajeMostrar += "El rut debe tener una longitud de entre 7 y 8<br>";
            entrar = false; 
        }
        if ((dv == 1 || dv == 2 || dv == 3 || dv == 4 || dv == 5 || dv == 6 || dv == 7 || dv == 8 || dv == 9 || lower(dv) == "k")) {
            mensajeMostrar += "El rut debe tener una longitud de entre 7 y 8<br>";
            entrar = false; 
        }
        
        if (!esMayuscula(name.charAt(0))) {
            mensajeMostrar += "<br>La primera letra del nombre debe ser mayúscula<br>";
            entrar = false;
        }

        if (name.length > 50) {
            mensajeMostrar += "El nombre puede contener un máximo de 50 caracteres<br>";
            entrar = false;
        }


        if (!apat == "") {

            if (!esMayuscula(apat.charAt(0))) {
                mensajeMostrar += "La primera letra del apellido paterno debe ser mayúscula<br>";
                entrar = false;
            }
            if (apat.length > 50) {
                mensajeMostrar += "El apellido paterno puede contener un máximo de 50 caracteres<br>";
                entrar = false;
            }
        }
        if (!amat == "") {

            if (!esMayuscula(amat.charAt(0))) {
                mensajeMostrar += "La primera letra del apellido materno debe ser mayúscula<br>";
                entrar = false;
            }
            if (amat.length > 50) {
                mensajeMostrar += "El apellido materno puede contener un máximo de 50 caracteres<br>";
                entrar = false;
            }
        }

        

        if (uname.length < 4 || uname.length > 60) {
            mensajeMostrar += "El nombre de usuario debe tener entre 4 y 60 caracteres<br>";
            entrar = false;
        }

        if (corre.length > 30) {
            mensajeMostrar += "El correo no puede contener mas de 30 dígitos<br>";
            entrar = false;
        }

        if ((pass.length > 60 || pass.length < 4) || (cpass.length > 60 || cpass.length < 4)) {
            mensajeMostrar += "La contraseñas deben tener entre 4 y 60 caracteres<br>";
            entrar = false; 
        }

        if (!(isUpper(pass) || isUpper(cpass))) {
            mensajeMostrar += "Una letra de las contraseñas debe ser mayúscula<br>";
            entrar = false;
        }

        if (!tieneNumero(pass) || !tieneNumero(cpass)) {
            mensajeMostrar += "Un dígito de las contraseñas debe ser un número<br>";
            entrar = false;
        }


        if (pass != cpass) {
            mensajeMostrar += "Las contraseñas no coinciden<br>";
            entrar = false;
        }
        if (entrar) {
        }
        else {
            $("#mensajeReg").html(mensajeMostrar);
            e.preventDefault();
        }
    });
})

function esMayuscula(letra) {
    return letra == letra.toUpperCase();
};

function isUpper(str) {
    return /[A-Z]/.test(str);
}

function tieneNumero(numero) {
    return /\d/.test(numero);
}