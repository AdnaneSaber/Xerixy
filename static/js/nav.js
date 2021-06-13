let collapseButton = document.getElementById("navCollapse");
let closeNav = document.getElementById("closeNav");
collapseButton.addEventListener("click", function () {
  toggleNav(true);
});
closeNav.addEventListener("click", function () {
  toggleNav(false);
});
function toggleNav(open) {
  let navLinks = document.getElementById("navLinks");
  let closeNav = document.getElementById("closeNav");
  if (open) {
    navLinks.style.left = 0;
    navLinks.style.display = "flex";
    closeNav.style.display = "block";
  } else {
    navLinks.style.left = "100%";
    navLinks.style.display = "none";
    closeNav.style.display = "none";
  }
}

$(document).ready(function () {
  $(window).bind("scroll", function () {
    if ($(document).scrollTop() > 0 && $(window).width() > 800) {
      $(".logoContainer").css("height", "0");
      $(".language").css("top", "50%");
      $(".scrollLogo").css("width", "85px");
      $(".scrollLogo").css("margin-left", "40px");
      $("nav").addClass("fixed");
    } else {
      $("nav").removeClass("fixed");

      $(".language").css("top", "67%");
      $(".logoContainer").css("height", "70px");
      $(".scrollLogo").css("width", "0%");
      $(".scrollLogo").css("margin", "0");
    }
  });
});
let fqw = $("#seoL").height();
if (fqw >= 200) {
  $("#seoL").css("overflow-y", "scroll");
}
$("#languageToggler").click(() => {
  let languages = $("#hiddenLanguages");
  let len = $("#hiddenLanguages button").length;
  if (languages.css("height") === "0px") {
    languages.css("height", len * 25 + "px");
  } else {
    languages.css("height", "0px");
  }
});
let cookies_tooltip = false;
const cookieOptions = () => {
  // $("#mask").css("display", "block");
  // $(".cookieOptions").css("display", "block");
  // cookies_tooltip = true;

  $("#mask").toggleClass("dn");
  // $(".cookieStatus").toggleClass("dn");
  $(".cookieOptions").toggleClass("dn");
  $("body").toggleClass("dn");
};

$("#cookieManBtn, #closeCookies").on("click", cookieOptions);
