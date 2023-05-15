
//Mostrar Secciones
function mostrarDefault() {
  const secciones = {
    "textdefault": "flex",
    "textcurso": "none",
    "Tpython": "none",
    "textasesoria": "none",
    "atrascursos": "none",
    "botonmenuin": "flex",
    "cursos": "none",
    "asesorias": "none",
    "inicio": "none",
    "Python": "none",
    "Cplusplus": "none",
    "htmlcss": "none",
    "TCp": "none",
    "THC": "none"
  };

  for (const id in secciones) {
    document.getElementById(id).style.display = secciones[id];
  }

}

function mostrarCurso() {
  const secciones = {
    "textdefault": "none",
    "textcurso": "flex",
    "Tpython": "none",
    "botonmenuin": "none",
    "textasesoria": "none",
    "atrascursos": "none",
    "cursos": "block",
    "asesorias": "none",
    "inicio": "none",
    "Python": "none",
    "Cplusplus": "none",
    "htmlcss": "none",
    "TCp": "none",
    "THC": "none"
  };

  for (const id in secciones) {
    document.getElementById(id).style.display = secciones[id];
  }
}


function mostrarAsesoria() {
  const secciones = {
    "textdefault": "none",
    "textcurso": "none",
    "textasesoria": "flex",
    "botonmenuin": "none",
    "Tpython": "none",
    "atrascursos": "none",
    "cursos": "none",
    "asesorias": "block",
    "inicio": "none",
    "Python": "none",
    "Cplusplus": "none",
    "htmlcss": "none",
    "TCp": "none",
    "THC": "none"
  };

  for (const id in secciones) {
    document.getElementById(id).style.display = secciones[id];
  }

}

function mostrarProfesores() {

  document.getElementById("cursos").style.display = "none";
  document.getElementById("asesorias").style.display = "none";
  //document.getElementById("profesores").style.display = "block";
  document.getElementById("inicio").style.display = "none";
  //document.getElementById("registro").style.display = "none";
}

function mostrarInicio() {
  const secciones = {
    "textdefault": "none",
    "textcurso": "none",
    "textasesoria": "none",
    "botonmenuin": "none",
    "Tpython": "none",
    "atrascursos": "none",
    "cursos": "none",
    "asesorias": "none",
    "inicio": "block",
    "Python": "none",
    "Cplusplus": "none",
    "htmlcss": "none",
    "TCp": "none",
    "THC": "none"
  };

  for (const id in secciones) {
    document.getElementById(id).style.display = secciones[id];
  }
}

function MPython() {
  const secciones = {
    "textdefault": "none",
    "textcurso": "none",
    "textasesoria": "none",
    "botonmenuin": "none",
    "Tpython": "flex",
    "atrascursos": "flex",
    "cursos": "none",
    "asesorias": "none",
    "inicio": "none",
    "Python": "block",
    "Cplusplus": "none",
    "htmlcss": "none",
    "TCp": "none",
    "THC": "none"
  };

  for (const id in secciones) {
    document.getElementById(id).style.display = secciones[id];
  }
}

function MCPP() {
  const secciones = {
    "textdefault": "none",
    "textcurso": "none",
    "textasesoria": "none",
    "textasesoria": "none",
    "atrascursos": "flex",
    "botonmenuin": "none",
    "cursos": "none",
    "asesorias": "none",
    "inicio": "none",
    "Python": "none",
    "Cplusplus": "block",
    "htmlcss": "none",
    "TCp": "flex",
    "THC": "none"
  };

  for (const id in secciones) {
    document.getElementById(id).style.display = secciones[id];
  }
}

function MHTMLCSS() {
  const secciones = {
    "textdefault": "none",
    "textcurso": "none",
    "textasesoria": "none",
    "botonmenuin": "none",
    "cursos": "none",
    "textasesoria": "none",
    "atrascursos": "flex",
    "asesorias": "none",
    "inicio": "none",
    "Python": "none",
    "Cplusplus": "none",
    "htmlcss": "block",
    "TCp": "flex",
    "THC": "none"
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
    "THC": "none"
  };

  for (const id in secciones) {
    document.getElementById(id).style.display = secciones[id];
  }
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
      }
      else {
        const succesCreateClient = document.getElementById('succesCreateClient');
        succesCreateClient.style.display = 'block';
        succesCreateClient.innerHTML = responseJson.message;
        setTimeout(() => {
          formre.reset()
          successEmployeeMessage.style.display = 'none'
        }, 15000)
      }
    })

}