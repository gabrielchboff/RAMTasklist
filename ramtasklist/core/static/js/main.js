
const activateSidebarItem = () => {

  var pathArray = window.location.pathname.split( '/' )[1];
  if (pathArray == '') {
    var iten = document.getElementById('home');
    iten.classList.add('active');
  } else {
    var iten = document.getElementById(pathArray);
    iten.classList.add('active');

  }
} 
