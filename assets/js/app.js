window.onload = evt => {
  // Testing link
  console.log('System Ready');

  // Execute code
  let options = {
    responsiveThreshold: 0
  }
  let elem = document.querySelector('.parallax');
  let instance = M.Parallax.init(elem, options);
}
