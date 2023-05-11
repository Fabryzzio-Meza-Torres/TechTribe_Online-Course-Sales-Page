// Obtener elementos del DOM
const menu = document.querySelector('.menu');
const logo = document.querySelector('img');
const cursosLink = document.querySelector('a[href="#cursos"]');
const asesoriasLink = document.querySelector('a[href="#asesorias"]');
const cursoPython = document.querySelector('.curso_python');
const cursoCplusplus = document.querySelector('.curso_cplusplus');
const cursoHtml = document.querySelector('.curso_html');
const asesoriaPython = document.querySelector('.asesoria_python');

// Función para agregar margen entre el logo y el menú
function ajustarMenu() {
  const logoWidth = logo.offsetWidth;
  menu.style.marginLeft = `${logoWidth}px`;
}

// Ajustar margen del menú al cargar la página
window.addEventListener('load', ajustarMenu);

// Ajustar margen del menú al redimensionar la ventana
window.addEventListener('resize', ajustarMenu);

// Animación del enlace a Cursos
cursosLink.addEventListener('click', (event) => {
  event.preventDefault();
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

window.addEventListener('scroll', animateElements);