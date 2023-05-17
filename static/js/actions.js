
//Ocultar cursos
function ocultarCursos() {
  document.getElementById("textcurso").style.display = "none";
  document.getElementById("Tpython").style.display = "none";
  document.getElementById("cursos").style.display = "none";
  document.getElementById("Python").style.display = "none";
  document.getElementById("Cplusplus").style.display = "none";
  document.getElementById("htmlcss").style.display = "none";
  document.getElementById("TCp").style.display = "none";
  document.getElementById("THC").style.display = "none";
  document.getElementById("MAT").style.display = "none";
  document.getElementById("csMat").style.display = "none";

  console.log("Ocultar cursos");
}


function ocultarAsesorias() {
  document.getElementById("textasesoria").style.display = "none";
  document.getElementById("TAP").style.display = "none";
  document.getElementById("AS1").style.display = "none";
  document.getElementById("AS2").style.display = "none";
  document.getElementById("AS3").style.display = "none";
  document.getElementById("asesorias").style.display = "none";
  document.getElementById("asesoriapython").style.display = "none";
  document.getElementById("asesoriacpp").style.display = "none";
  document.getElementById("asesoriahtmlcss").style.display = "none";
  document.getElementById("asesoriamathcs").style.display = "none";

}


//Mostrar Secciones
function mostrarDefault() {
  ocultarAsesorias();
  ocultarCursos();
  document.getElementById("textdefault").style.display = "flex";
  document.getElementById("botonmenuin").style.display = "flex";


}

function mostrarCurso() {

  const secciones = {
    "textdefault": "none",
    "textcurso": "flex",
    "Tpython": "none",
    "botonmenuin": "none",
    "textasesoria": "none",
    "cursos": "block",
    "asesorias": "none",
    "inicio": "none",
    "Python": "none",
    "Cplusplus": "none",
    "htmlcss": "none",
    "TCp": "none",
    "THC": "none",
    "TAP": "none",
    "asesoriapython": "none",
    "csMat": "none",
    "MAT": "none",
    "profesores": "none",
    "AS1":"nome",
    "AS2":"nome",
    "AS3":"nome",
    "asesoriahtmlcss":"none",
    "asesoriamathcs":"none"
  };


}


function mostrarAsesoria() {
const secciones = {
  "textdefault": "none",
  "textcurso": "none",
  "textasesoria": "flex",
  "botonmenuin": "none",
  "Tpython": "none",
  "cursos": "none",
  "asesorias": "block",
  "inicio": "none",
  "Python": "none",
  "Cplusplus": "none",
  "htmlcss": "none",
  "TCp": "none",
  "THC": "none",
  "TAP": "none",
  "asesoriapython": "none",
  "csMat": "none",
  "MAT": "none",
  "profesores": "none",
  "AS1":"nome",
  "AS2":"nome",
  "AS3":"nome",
  "asesoriahtmlcss":"none",
  "asesoriamathcs":"none"
};


for (const id in secciones) {
  document.getElementById(id).style.display = secciones[id];
}

}



function mostrarInicio() {
  const secciones = {
    "textdefault": "none",
    "textcurso": "none",
    "textasesoria": "none",
    "botonmenuin": "none",
    "Tpython": "none",
    "cursos": "none",
    "asesorias": "none",
    "inicio": "block",
    "Python": "none",
    "Cplusplus": "none",
    "htmlcss": "none",
    "TCp": "none",
    "THC": "none",
    "TAP": "none",
    "asesoriapython": "none",
    "csMat": "none",
    "MAT": "none",
    "profesores": "none",
    "AS1":"nome",
    "AS2":"nome",
    "AS3":"nome",
    "asesoriahtmlcss":"none",
    "asesoriamathcs":"none"
  };


}

function mostrarRegistro() {
  document.getElementById("cursos").style.display = "none";
  document.getElementById("asesorias").style.display = "none";
  //document.getElementById("profesores").style.display = "none";
  document.getElementById("inicio").style.display = "none";
  //document.getElementById("registro").style.display = "block";
}

function MPython(){  
ocultarCursos();
document.getElementById("Tpython").style.display = "flex";
document.getElementById("Python").style.display = "block";

}

function MCPP(){  

  ocultarCursos();
  document.getElementById("TCp").style.display = "flex";
  document.getElementById("Cplusplus").style.display = "block";

}

function MHTMLCSS(){  
  ocultarCursos();
  document.getElementById("THC").style.display = "flex";
  document.getElementById("htmlcss").style.display = "block";
}


function MATECSs(){ 
  ocultarCursos();
  document.getElementById("MAT").style.display = "flex";
  document.getElementById("csMat").style.display = "block"; 
}




function python_asesory(){
  ocultarAsesorias();
  document.getElementById("TAP").style.display = "flex";
  document.getElementById("asesoriapython").style.display = "block";
}


function mostrarProfesores(){  const secciones = {
  "textdefault": "none",
  "textcurso": "none",
  "textasesoria": "none",
  "botonmenuin": "none",
  "cursos": "none",
  "textasesoria": "none",
  "asesorias": "none",
  "inicio": "none",
  "Python": "none",
  "Cplusplus": "none",
  "htmlcss": "none",
  "TCp": "none",
  "THC": "none",
  "TAP": "none",
  "asesoriapython": "none",
  "matecs": "none",
  "MAT": "none",
  "profesores": "block",
  "AS1":"nome",
  "AS2":"nome",
  "AS3":"nome",
  "asesoriahtmlcss":"none",
  "asesoriamathcs":"none"
};

  for (const id in secciones) {
    document.getElementById(id).style.display = secciones[id];
  }
}

function prueba() {
  const secciones = {
    "textdefault": "none",
    "textcurso": "none",
    "textasesoria": "none",
    "botonmenuin": "none",
    "cursos": "none",
    "textasesoria": "none",
    "atrascursos": "none",
    "asesorias": "none",
    "inicio": "none",
    "Python": "none",
    "Cplusplus": "none",
    "htmlcss": "block",
    "TCp": "none",
    "THC": "none",
    "asesoriacpp": "none",
    "AS1":"nome",
    "AS2":"nome",
    "AS3":"nome",
    "asesoriahtmlcss":"none",
    "asesoriamathcs":"none"
  };


}


function cplus_asesory(){  
  ocultarAsesorias();
  document.getElementById("AS1").style.display = "flex";
  document.getElementById("asesoriacpp").style.display = "block";

}

function html_asesory(){  
  ocultarAsesorias();
  document.getElementById("AS2").style.display = "flex";
  document.getElementById("asesoriahtmlcss").style.display = "block";


}

function mat_asesory(){  
  ocultarAsesorias();
  document.getElementById("AS3").style.display = "flex";
  document.getElementById("asesoriamathcs").style.display = "block";

}

//Enviar formulario
function createUser() {
  const form_register = document.getElementById('form_register');
  form_register.addEventListener('submit', SubmitForm)


}
const pendingsController = new WeakMap()

function SubmitForm(evento) {
  //para evitar que el formulario se envíe y se recargue la página.
  evento.preventDefault();
  //para evitar que el evento se propague hacia otros elementos.
  evento.stopPropagation();

  const formre = evento.currentTarget;
  const previusController = pendingsController.get(formre)
  if (previusController) {
    previusController.abort();
  }

  const controller = new AbortController()
  pendingsController.set(formre, controller)
  const formData = new FormData(formre)
  const myButton= document.getElementById('Rbutton')

  fetch('/register', {
    'method': 'POST',
    'body': formData,
    'signal': controller.signal,
  })
    .then(function (response) {
      console.log('response:', response)
      return response.json();
    })
    .then(function (responseJson) {
      if (!responseJson.success) {

        const errorCreateClient = document.getElementById('errorCreateClient');
        errorCreateClient.style.display = 'block';
        errorCreateClient.innerHTML = responseJson.message;
        myButton.addEventListener('click', function() {
          errorCreateClient.style.display = 'none';
        })
      }
      else {
        const succesCreateClient = document.getElementById('succesCreateClient');
        succesCreateClient.style.display = 'block';
        succesCreateClient.innerHTML = responseJson.message;
        setTimeout(() => {
          formre.reset()
          successEmployeeMessage.style.display = 'none'
        }, 1059)
      }
    })

}



//Enviar formulario
  setTimeout(() => {
  const form_login = document.getElementById('loginform');
  form_login.addEventListener('submit', SubmitLoginn)
  }, 1000)


const pendingsControl = new WeakMap()

function SubmitLoginn(evento) {
  //para evitar que el formulario se envíe y se recargue la página.
  evento.preventDefault();
  //para evitar que el evento se propague hacia otros elementos.
  evento.stopPropagation();

  const formrLo = evento.currentTarget;
  const previusController = pendingsControl.get(formrLo)
  if (previusController) {
    previusController.abort();
  }

  const controller = new AbortController()
  pendingsControl.set(formrLo, controller)
  const formData = new FormData(formrLo)
  const Button= document.getElementById('InicioButon')

  fetch('/login', {
    'method': 'POST',
    'body': formData,
    'signal': controller.signal,
  })
    .then(function (response) {
      console.log('response:', response)
      return response.json();
    })
    .then(function (responseJson) {
      if (!responseJson.success) {
        const errorCreateClient = document.getElementById('errorLogin');
        errorCreateClient.style.display = 'block';
        errorCreateClient.innerHTML = responseJson.message;
        Button.addEventListener('click', function() {
          errorCreateClient.style.display = 'none';
        });
        
      }
      else {
        const succesCreateClient = document.getElementById('succesLogin');
        succesCreateClient.style.display = 'block';
        succesCreateClient.innerHTML = responseJson.message;
        setTimeout(() => {
          formrLo.reset()
          successEmployeeMessage.style.display = 'none'
        }, 2000)
        window.location.href = '/'
      }
    })
}


function Compra_1(){document.getElementById("comprar_Python").addEventListener("click", function() {
  var button = document.getElementById("comprar_Python");
  var curso_name = button.getAttribute("curso_name");

  // Construir la URL con el valor de curso_name
  var url = "/compra/" + curso_name;

  // Redirigir a la URL
  window.location.href = url;
});}

function Compra_2(){document.getElementById("comprar_Cplusplus").addEventListener("click", function() {
  var button = document.getElementById("comprar_Cplusplus");
  var curso_name = button.getAttribute("curso_name");

  // Construir la URL con el valor de curso_name
  var url = "/compra/" + curso_name;

  // Redirigir a la URL
  window.location.href = url;
});}

function Compra_3(){document.getElementById("comprar_htmlcss").addEventListener("click", function() {
  var button = document.getElementById("comprar_htmlcss");
  var curso_name = button.getAttribute("curso_name");

  // Construir la URL con el valor de curso_name
  var url = "/compra/" + curso_name;

  // Redirigir a la URL
  window.location.href = url;
});}

function Compra_4(){document.getElementById("comprar_csMat").addEventListener("click", function() {
  var button = document.getElementById("comprar_csMat");
  var curso_name = button.getAttribute("curso_name");

  // Construir la URL con el valor de curso_name
  var url = "/compra/" + curso_name;

  // Redirigir a la URL
  window.location.href = url;
});}

function Compra_5(){document.getElementById("comprar_asesoriapython").addEventListener("click", function() {
  var button = document.getElementById("comprar_asesoriapython");
  var curso_name = button.getAttribute("curso_name");

  // Construir la URL con el valor de curso_name
  var url = "/compra/" + curso_name;

  // Redirigir a la URL
  window.location.href = url;
});}

function Compra_6(){document.getElementById("comprar_asesoriacpp").addEventListener("click", function() {
  var button = document.getElementById("comprar_asesoriacpp");
  var curso_name = button.getAttribute("curso_name");

  // Construir la URL con el valor de curso_name
  var url = "/compra/" + curso_name;

  // Redirigir a la URL
  window.location.href = url;
});}

function Compra_7(){document.getElementById("comprar_asesoriahtmlcss").addEventListener("click", function() {
  var button = document.getElementById("comprar_asesoriahtmlcss");
  var curso_name = button.getAttribute("curso_name");

  // Construir la URL con el valor de curso_name
  var url = "/compra/" + curso_name;

  // Redirigir a la URL
  window.location.href = url;
});}

function Compra_8(){document.getElementById("comprar_asesoriamathcs").addEventListener("click", function() {
  var button = document.getElementById("comprar_asesoriamathcs");
  var curso_name = button.getAttribute("curso_name");

  // Construir la URL con el valor de curso_name
  var url = "/compra/" + curso_name;

  // Redirigir a la URL
  window.location.href = url;
});}