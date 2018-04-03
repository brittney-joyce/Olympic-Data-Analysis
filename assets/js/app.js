window.onload = evt => {
  // Testing link
  console.log('System Ready');
  console.log("Go Swiss Hockey! #77 Gustave, Allons-y!");

  // Execute code
  let options = {
    responsiveThreshold: 0
  }

  let elem = document.querySelector('.parallax');
  let instance = M.Parallax.init(elem, options);

  let scrollSpyElem = document.querySelector('.scrollspy')
  M.ScrollSpy.init(scrollSpyElem, {
    throttle: 3000
  })

  M.AutoInit();
}
// Materialize non jquery dependancy didn't work, soooo I got screwed using this code
// Used the following instead
// Was able to get materialize to work without jQuery dependency

// Working JQuery
// $(document).ready(function(){
//   console.log("Go Swiss Hockey! #77 Gustave, Allons-y!");
//   $('.parallax').parallax();
//   $('.materialboxed').materialbox();
//   $('.scrollspy').scrollSpy();
// });
