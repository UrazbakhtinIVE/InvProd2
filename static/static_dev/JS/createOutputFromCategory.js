document.addEventListener("DOMContentLoaded", () => {
  const categoriesSelect = document.querySelector("#id_categories");

  const redirectToView = (value) => {
    if (!value) {
      // noinspection JSAnnotator
        return;
    }
    if (value == "monitors") {
      window.location.replace("/devices/monitor/create");
    } else if (value == "headsets") {
      window.location.replace("/devices/headset/create");
    } else if (value == "speakers") {
      window.location.replace("/devices/speakers/create");
    } else if(value == "printers"){
      window.location.replace("/printer/create");
    } else if(value == "cartridges"){
      window.location.replace("/cartridges/create");
    }
  };

  categoriesSelect.addEventListener("change", (event) => {
    redirectToView(event.target.value);
});
});
