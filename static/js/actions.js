// Obtener elementos del DOM
/*
const menu = document.querySelector('.header');
const logo = document.querySelector('img');
const cursosLink = document.querySelector('#cursos');
const asesoriasLink = document.querySelector('#asesorias"]');
const cursoPython = document.querySelector('.curso_python');
const cursoCplusplus = document.querySelector('.curso_cplusplus');
const cursoHtml = document.querySelector('.curso_html');
const asesoriaPython = document.querySelector('.asesoria_python');
*/
//Contenido
/*
function showContent(index) {
  const sections = document.querySelectorAll('.body__item')
  for (let i = 0; i < sections.length; i++) {
    const section = sections[i]
    if (i === index) {
      section.classList.add('body__item__active')

      if (i == 0) {
        //handle display employees
        fetchCursos()
      } else if (i == 1) {
        //handle create new employee
        populateSelectDepartment()
        createEmployee()
      } else if (i == 2) {
        //List of departments
        fetchDepartments()
      } else if (i == 3) {
        //create new department
        createDepartment()
      }
    } else {
      section.classList.remove('body__item__active')
    }
  }
}

function fetchCursos(){
  fetch('/cursos')
    .then(function(cursos){
      const cursos = document.getElementById('cursos')
    })
}

function fetchAsesorias(){
  fetch('/asesorias')
    .then(function(asesoria){
      const asesoria = document.getElementById('asesorias')
    })
}

// Función para agregar margen entre el logo y el menú

function ajustarMenu() {
  const logoWidth = logo.offsetWidth;
  menu.style.marginLeft = `${logoWidth}px`;
}

// Ajustar margen del menú al cargar la página
window.addEventListener('load', ajustarMenu);

// Ajustar margen del menú al redimensionar la ventana
window.addEventListener('resize', ajustarMenu);
*/



//Mostrar Secciones
function mostrarDefault() {
  //Texto
  document.getElementById("textdefault").style.display = "flex";
  document.getElementById("textcurso").style.display = "none";
  document.getElementById("textasesoria").style.display = "none";
  //Boton
document.getElementById("botonmenuin").style.display = "flex";
  //Secciones
  document.getElementById("cursos").style.display = "none";
  document.getElementById("asesorias").style.display = "none";
  //document.getElementById("profesores").style.display = "none";
  document.getElementById("inicio").style.display = "none";
  //document.getElementById("registro").style.display = "none";


}

function mostrarCurso() {
//Texto
document.getElementById("textdefault").style.display = "none";
document.getElementById("textcurso").style.display = "flex";
document.getElementById("textasesoria").style.display = "none";

//Boton
document.getElementById("botonmenuin").style.display = "none";
//Secciones
document.getElementById("cursos").style.display = "block";
document.getElementById("asesorias").style.display = "none";
//document.getElementById("profesores").style.display = "none";
document.getElementById("inicio").style.display = "none";
//document.getElementById("registro").style.display = "none";

}

function mostrarAsesoria() {
//Texto
document.getElementById("textdefault").style.display = "none";
document.getElementById("textcurso").style.display = "none";
document.getElementById("textasesoria").style.display = "flex";
//Boton
document.getElementById("botonmenuin").style.display = "none";
//Secciones
document.getElementById("cursos").style.display = "none";
document.getElementById("asesorias").style.display = "block";
//document.getElementById("profesores").style.display = "none";
document.getElementById("inicio").style.display = "none";
//document.getElementById("registro").style.display = "none";
}

function mostrarProfesores() {
  document.getElementById("cursos").style.display = "none";
  document.getElementById("asesorias").style.display = "none";
  //document.getElementById("profesores").style.display = "block";
  document.getElementById("inicio").style.display = "none";
  //document.getElementById("registro").style.display = "none";
}

function mostrarInicio() {
  document.getElementById("textdefault").style.display = "none";
  document.getElementById("textcurso").style.display = "none";
  document.getElementById("textasesoria").style.display = "none";
  
  //Boton
  document.getElementById("botonmenuin").style.display = "none";
  //Secciones
  document.getElementById("cursos").style.display = "none";
  document.getElementById("asesorias").style.display = "none";
  //document.getElementById("profesores").style.display = "none";
  document.getElementById("inicio").style.display = "block";
  //document.getElementById("registro").style.display = "none";
  
}

function mostrarRegistro() {
  document.getElementById("cursos").style.display = "none";
  document.getElementById("asesorias").style.display = "none";
  //document.getElementById("profesores").style.display = "none";
  document.getElementById("inicio").style.display = "none";
  //document.getElementById("registro").style.display = "block";
}


/*
// Animación del enlace a Cursos
cursosLink.addEventListener('click', () => {
  cursoPython.classList.add('animate__fadeInLeft');
  cursoCplusplus.classList.add('animate__fadeInUp');
  cursoHtml.classList.add('animate__fadeInRight');
});

// Animación del enlace a Asesorías
asesoriasLink.addEventListener('click', (event) => {
  event.preventDefault();
  asesoriaPython.classList.add('animate__fadeInLeft');
});

// Animaciones en scroll
const elementsToAnimate = [cursoPython, cursoCplusplus, cursoHtml, asesoriaPython];

function animateElements() {
  for (const element of elementsToAnimate) {
    const elementTop = element.getBoundingClientRect().top;
    const windowHeight = window.innerHeight;

    if (elementTop < windowHeight) {
      element.classList.add('animate__fadeIn');
    }
  }
}

window.addEventListener('scroll', animateElements);*/