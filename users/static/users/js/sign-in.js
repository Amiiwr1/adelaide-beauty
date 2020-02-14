(function ($) {
  const SignInForm = function (form) {
    this.form = form;
  };

  SignInForm.handleSuccess = function () {
    window.location.replace(origin)
  };

  SignInForm.handleError = function (jqXHR) {
    if (jqXHR.status === 400 || jqXHR.status === 401) {

      var snackbarContainer = document.querySelector('#snack-toast');
      var showToastButton = document.querySelector('#signin-snack');
      var snackData = {message: 'Username and Password does not match.'};
      snackbarContainer.MaterialSnackbar.showSnackbar(snackData);

    }
  };
  Object.defineProperty(SignInForm.prototype, 'username', {
    get: function () {
      return $(this.form).find("input[name=username]").val().trim().toLowerCase();

    }
  });

  Object.defineProperty(SignInForm.prototype, 'password', {
    get: function () {
      return $(this.form).find("input[name=password]").val();
    }
  });

  Object.defineProperty(SignInForm.prototype, 'action', {
    get: function () {
      return $(this.form).attr('data-action');
    }
  });

  Object.defineProperty(SignInForm.prototype, 'method', {
    get: function () {
      return $(this.form).attr('method');
    }
  });


  SignInForm.prototype.isValid = function () {
    return Boolean(this.username) && Boolean(this.password);
  };

  SignInForm.prototype.handleComplete = function () {
    $(this.form).find("button").removeAttr("disabled");
  };

  SignInForm.prototype.submit = function () {
    const data = {
      username: this.username,
      password: this.password,
    };

    $.ajax({
      url: this.action, type: this.method, data: JSON.stringify(data),
      cache: false, contentType: "application/json", dataType: "json",
      success: SignInForm.handleSuccess, error: SignInForm.handleError.bind(this),
      complete: this.handleComplete.bind(this), headers: {'X-CSRFToken': csrftoken}
    });
  };

  $(document).ready(function () {
    const signIn = $("#singInForm");
    const form = new SignInForm(signIn);
    window.signInForm = form;

    signIn.submit(function (event) {
      event.preventDefault();
      if (form.isValid()) {
        $(this).find("button").attr("disabled", "disabled");
        form.submit();
      }
    });
  });
})(jQuery);