// window.onload = evt => {
//   // Testing link
//   console.log('System Ready');
//
//   // Execute code
//   // let options = {
//   //   responsiveThreshold: 0
//   // }
//   // let elem = document.querySelector('.parallax');
//   // let instance = M.Parallax.init(elem, options);
//   $('.parallax').parallax();
// Materialize non jquery dependancy didn't work, soooo I got screwed using this code
// Used the following instead

$(document).ready(function(){
  console.log("Go Swiss Hockey! #77 Gustave, Allons-y!");
  $('.parallax').parallax();
  $('.materialboxed').materialbox();
  $('.scrollspy').scrollSpy();
});
