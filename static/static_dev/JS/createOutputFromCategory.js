document.addEventListener("DOMContentLoaded", () => {
  const categoriesSelect = document.querySelector("#id_categories");

  const redirectToView = (value) => {
    if (!value) {
      // noinspection JSAnnotator
        return;
    }
    if (value == "monitors") {
      window.location.replace("/devices/create_monitor");
    } else if (value == "headsets") {
      window.location.replace("/devices/create_headset");
    } else if (value == "speakers") {
      window.location.replace("/devices/create_speaker");
    } else if(value == "printers"){
      window.location.replace("/printer/create");
    } else if(value == "catriges"){
      window.location.replace("/catrige/create");
    }
  };

  categoriesSelect.addEventListener("change", (event) => {
    redirectToView(event.target.value);
});
});
