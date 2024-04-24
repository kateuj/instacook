// Materialize CSS initialization
document.addEventListener("DOMContentLoaded", function () {
  // Sidenav initialization
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);

  // Select initialization
  let selects = document.querySelectorAll("select");
  M.FormSelect.init(selects);

  // Collapsible initialization
  let collapsibles = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapsibles);

  // Modal initialization
  let modals = document.querySelectorAll('.modal');
  M.Modal.init(modals);

  // Hero Slider initialization
  let slider = document.querySelectorAll('.slider');
  M.Slider.init(slider);

});

// Update query params for dropdown filters on search page.
function updateQueryParams(key, value) {
  const url = new URL(window.location);
  if (value === 'All') {
    url.searchParams.delete(key);
  } else {
    url.searchParams.set(key, value);
  }
  window.location = url.toString();
}