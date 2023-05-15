//Mostrar Secciones
function mostrarDefault() {
  const secciones = {
    "textdefault": "flex",
    "textcurso": "none",
    "Tpython": "none",
    "textasesoria": "none",
    "botonmenuin": "flex",
    "cursos": "none",
    "asesorias": "none",
    "inicio": "none",
    "Python": "none",
    "Cplusplus": "none",
    "htmlcss": "none",
    "TCp": "none",
    "THC": "none",
    "TAP": "none",
    "asesoriapython": "none"
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
    "cursos": "block",
    "asesorias": "none",
    "inicio": "none",
    "Python": "none",
    "Cplusplus": "none",
    "htmlcss": "none",
    "TCp": "none",
    "THC": "none",
    "TAP": "none",
    "asesoriapython": "none"
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
  "cursos": "none",
  "asesorias": "block",
  "inicio": "none",
  "Python": "none",
  "Cplusplus": "none",
  "htmlcss": "none",
  "TCp": "none",
  "THC": "none",
  "TAP": "none",
  "asesoriapython": "none"
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
    "cursos": "none",
    "asesorias": "none",
    "inicio": "block",
    "Python": "none",
    "Cplusplus": "none",
    "htmlcss": "none",
    "TCp": "none",
    "THC": "none",
    "TAP": "none",
    "asesoriapython": "none"
  };

  for (const id in secciones) {
    document.getElementById(id).style.display = secciones[id];
  }
}

function mostrarRegistro() {
  document.getElementById("cursos").style.display = "none";
  document.getElementById("asesorias").style.display = "none";
  //document.getElementById("profesores").style.display = "none";
  document.getElementById("inicio").style.display = "none";
  //document.getElementById("registro").style.display = "block";
}

function MPython(){  const secciones = {
  "textdefault": "none",
  "textcurso": "none",
  "textasesoria": "none",
  "botonmenuin": "none",
  "Tpython": "flex",
  "cursos": "none",
  "asesorias": "none",
  "inicio": "none",
  "Python": "block",
  "Cplusplus": "none",
  "htmlcss": "none",
  "TCp": "none",
  "THC": "none",
  "TAP": "none",
  "asesoriapython": "none"
};

for (const id in secciones) {
  document.getElementById(id).style.display = secciones[id];
}
}

function MCPP(){  const secciones = {
  "textdefault": "none",
  "textcurso": "none",
  "textasesoria": "none",
  "textasesoria": "none",
  "botonmenuin": "none",
  "cursos": "none",
  "asesorias": "none",
  "inicio": "none",
  "Python": "none",
  "Cplusplus": "block",
  "htmlcss": "none",
  "TCp": "flex",
  "THC": "none",
  "TAP": "none",
  "asesoriapython": "none"
};

for (const id in secciones) {
  document.getElementById(id).style.display = secciones[id];
}
}

function MHTMLCSS(){  const secciones = {
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
  "htmlcss": "block",
  "TCp": "flex",
  "THC": "none",
  "TAP": "none",
  "asesoriapython": "none"
};


for (const id in secciones) {
  document.getElementById(id).style.display = secciones[id];
}
}

function python_asesory(){  const secciones = {
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
  "TAP": "flex",
  "asesoriapython": "block"
};


for (const id in secciones) {
  document.getElementById(id).style.display = secciones[id];
}
}

function mate(){  const secciones = {
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
  "matecs": "block",
  "MAT": "flex"
};

for (const id in secciones) {
  document.getElementById(id).style.display = secciones[id];
}
}