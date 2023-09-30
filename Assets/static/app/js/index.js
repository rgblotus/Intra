$(document).ready(function () {
  $("#loginForm").submit(function (event) {
    event.preventDefault();
    var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
    $.ajax({
      type: "POST",
      url: "/", // Replace with the actual URL for your login view
      data: $(this).serialize() + "&login_submit=login_submit",
      headers: {
        "X-CSRFToken": csrfToken,
      },
      success: function (response) {
        if (response.success) {
          // Redirect to home page
          window.location.href = "/"; // Replace with the actual URL for your home view
        } else {
          // Display form errors
          var errors = JSON.parse(response.errors);
          var errorlist = "";
          for (var field in errors) {
            if (errors.hasOwnProperty(field)) {
              errorlist += errors[field][0]["message"];
            }
          }
          $("#loginError").text(errorlist).show();
        }
      },
      error: function (xhr, status, error) {
        console.error(xhr.responseText);
      },
    });
  });
});

$(document).ready(function () {
  $("#registerForm").submit(function (event) {
    event.preventDefault();
    var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
    $.ajax({
      type: "POST",
      url: "/", // Replace with the actual URL for your login view
      data: $(this).serialize() + "&register_submit=register_submit",
      headers: {
        "X-CSRFToken": csrfToken,
      },
      success: function (response) {
        if (response.success) {
          // Redirect to home page
          window.location.href = "/"; // Replace with the actual URL for your home view
        } else {
          // Display form errors
          $("#contactError").text(response.error_message).show();
          var errors = JSON.parse(response.errors);
          var errorlist = "";
          for (var field in errors) {
            if (errors.hasOwnProperty(field)) {
              errorlist += errors[field][0]["message"];
            }
          }
          $("#registerError").text(errorlist).show();
        }
      },
      error: function (xhr, status, error) {
        console.error(xhr.responseText);
      },
    });
  });
});

$(document).ready(function () {
  $("#registerForm #id_email").on("input", function () {
    var emailValue = $(this).val();
    var usernameValue = emailValue.split("@")[0];
    $("#registerForm #id_username").val(usernameValue);
  });
});

document.addEventListener("DOMContentLoaded", function () {
  // Initialize the purecounter plugin
  var counters = document.querySelectorAll(".purecounter");
  counters.forEach(function (counter) {
    var options = {
      duration: counter.getAttribute("data-purecounter-duration") || 2, // Duration in seconds
      start: counter.getAttribute("data-purecounter-start") || 0, // Start value
      end: counter.getAttribute("data-purecounter-end") || 0, // End value
    };
    var purecounter = new PureCounter(counter, options);
    purecounter.start();
  });
});

// Get the button element
const scrollToTopBtn = document.getElementById("scrollToTopBtn");

// Show the button when user scrolls down
window.addEventListener("scroll", () => {
  if (window.scrollY > 300) {
    scrollToTopBtn.style.display = "block";
  } else {
    scrollToTopBtn.style.display = "none";
  }
});

// Scroll to the top when the button is clicked
scrollToTopBtn.addEventListener("click", () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
});
