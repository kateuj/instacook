document.addEventListener("DOMContentLoaded", function() {
  // Sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

  // Select initialization
  let selects = document.querySelectorAll("select");
  M.FormSelect.init(selects); 
    
  // Collaspsible initialization
  let collapsibles = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapsibles);

  // Modal initialization
  let modals = document.querySelectorAll('.modal');
  M.Modal.init(modals);

  // Hero Slider initialization
  let slider = document.querySelectorAll('.slider');
  M.Slider.init(slider);

});