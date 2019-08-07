window.onload = function() {
  var req_inp = document.querySelectorAll(".is-invalid");
  var drawer = document.querySelector("div.mdl-layout__drawer");
  var drawerShadow = document.querySelector("div.mdl-layout__obfuscator");
  var login_tab = document.querySelector("#teacher-login");
  var reg_tab = document.querySelector("#teacher-reg");

  req_inp.forEach((el, i) => {
    el.firstElementChild.onblur = function(e) {
      if (e.target.value == "" && e.target.required) {
        el.classList.add("is-invalid");
      }
    };
    el.classList.remove("is-invalid");
  });

  var hammertime = new Hammer(document.querySelector("main"));
  hammertime.on("swiperight", function(ev) {
    drawerShadow.classList.add("is-visible");
    drawer.classList.add("is-visible");
    drawer.setAttribute("aria-hidden", "false");
  });
  hammertime.on("swipeleft", function(ev) {
    drawerShadow.classList.remove("is-visible");
    drawer.classList.remove("is-visible");
    drawer.setAttribute("aria-hidden", "true");
  });
  var login_ham = new Hammer(login_tab);
  var reg_ham = new Hammer(reg_tab);
  login_ham.on("swipeleft", function(e) {
    login_tab.classList.remove("is-active");
    reg_tab.classList.add("is-active");
    document.querySelector("#tlogin-tab").classList.remove("is-active");
    document.querySelector("#treg-tab").classList.add("is-active");
  });
  reg_ham.on("swiperight", function(e) {
    drawerShadow.classList.remove("is-visible");
    drawer.classList.remove("is-visible");
    document.querySelector("#treg-tab").classList.remove("is-active");
    document.querySelector("#tlogin-tab").classList.add("is-active");
    drawer.setAttribute("aria-hidden", "true");
    login_tab.classList.add("is-active");
    reg_tab.classList.remove("is-active");
  });
};
