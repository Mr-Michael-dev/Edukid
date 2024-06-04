$(document).ready(function() {
    $("#regform").submit(function(e) {
      e.preventDefault();
      return validateReg() ? this.submit() : false;
    });

    $("#loginform").submit(function(e) {
      e.preventDefault();
      return validateLogin() ? this.submit() : false;
    });
  
    function setError(element, message) {
      element.parent().addClass("error").removeClass("success").find(".error").text(message);
    }
  
    function setSuccess(element) {
      element.parent().addClass("success").removeClass("error").find(".error").text("");
    }
  
    function validateReg() {
      const fullnameValue = $("#fullname").val().trim();
      const usernameValue = $("#username").val().trim();
      const passwordValue = $("#password").val().trim();
      const confirmPasswordValue = $("#confirmPassword").val().trim();
  
      if (fullnameValue === "") {
        setError($("#fullname"), "Fullname is required");
        return false;
      } else {
        setSuccess($("#fullname"));
      }
  
      if (usernameValue === "") {
        setError($("#username"), "Username is required");
        return false;
      } else {
        setSuccess($("#username"));
      }
  
      if (passwordValue === "") {
        setError($("#password"), "Please enter your password");
        return false;
      } else {
        setSuccess($("#password"));
      }
  
      if (confirmPasswordValue === "") {
        setError($("#confirmPassword"), "Please confirm your password");
        return false;
      } else if (confirmPasswordValue !== passwordValue) {
        setError($("#confirmPassword"), "Passwords do not match");
        return false;
      } else {
        setSuccess($("#confirmPassword"));
      }

      return true;
    }

    function validateLogin() {
      const usernameValue = $("#username").val().trim();
      const passwordValue = $("#password").val().trim();

      if (usernameValue === "") {
        setError($("#username"), "Username is required");
        return false;
      } else {
        setSuccess($("#username"));
      }
  
      if (passwordValue === "") {
        setError($("#password"), "Please enter your password");
        return false;
      } else {
        setSuccess($("#password"));
      }
      return true;
    }
  });
  