// Side nav bar on mobile screens
document.addEventListener("DOMContentLoaded", function() {
  // sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

  var slider = document.getElementById('slider');
    noUiSlider.create(slider, {
    start: [0, 0],
    connect: true,
    step: 1,
    orientation: 'horizontal', // 'horizontal' or 'vertical'
    range: {
      'min': 0,
      'max': 5
    },
    format: wNumb({
      decimals: 0
    })
  });


});