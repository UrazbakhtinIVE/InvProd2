document.addEventListener("DOMContentLoaded", () => {
  const categoriesSelect = document.querySelector("#id_categories");

  const redirectToView = (value) => {
    if (!value) {
      return;
    }
    if (value == "monitors") {
      window.location.replace("/outputs/create_monitor");
    } else if (value == "headsets") {
      window.location.replace("/outputs/create_headset");
    } else if (value == "speakers") {
      window.location.replace("/outputs/create_speaker");
    }
  };

  categoriesSelect.addEventListener("change", (event) => {
    redirectToView(event.target.value);
  });
});
