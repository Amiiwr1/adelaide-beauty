(function ($) {
  const SignUpForm = function (form) {
    this.form = form;
    this.fields = ['username', 'email', 'mobile_number', 'password', 'first_name', 'last_name'];
  };


  SignUpForm.prototype.init = function () {
    const forms = $('form');
    forms.submit(this.submit.bind(this));
    forms.find('.mdl-textfield__error').each(function () {
      const element = $(this);
      const handleText = function () {
        element.text(element.attr('data-text'));
      };

      $(this).siblings('input').keyup(handleText);
      $(this).siblings('select').change(handleText);
    });
  };

  SignUpForm.handleSuccess = function (data) {
    window.location.replace(origin)
  };
  SignUpForm.prototype.handleFieldError = function (name, errors) {
    if (errors !== undefined) {
      const group = this.form.find('#f-' + name);
      group.find('.mdl-textfield__error').html(errors.join('<br />'));
      group.addClass('is-invalid');
    }
  };
  SignUpForm.prototype.handleError = function (jqXHR) {
    if (jqXHR.status === 400 || jqXHR.status === 403) {

      var snackbarContainer = document.querySelector('#snack-toast');
      var showToastButton = document.querySelector('#signup-snack');
      var snackData = {message: 'Please fix form errors.'};
      snackbarContainer.MaterialSnackbar.showSnackbar(snackData);
      const data = jqXHR.responseJSON;
      var signUp = new SignUpForm(this.form);
      for (let i = 0; i < signUp.fields.length; i += 1) {
        const name = signUp.fields[i];
        this.handleFieldError(name, data[name]);
      }
    }
  };
  Object.defineProperty(SignUpForm.prototype, 'username', {
    get: function () {
      return $(this.form).find("input[name=username]").val().trim().toLowerCase();

    }
  });

  Object.defineProperty(SignUpForm.prototype, 'email', {
    get: function () {
      return $(this.form).find("input[name=email]").val().trim().toLowerCase();

    }
  });
  Object.defineProperty(SignUpForm.prototype, 'form', {
    get: function () {
      return $('#singUpForm');
    }
  });

  Object.defineProperty(SignUpForm.prototype, 'password', {
    get: function () {
      return $(this.form).find("input[name=password]").val();
    }
  });
  Object.defineProperty(SignUpForm.prototype, 'first_name', {
    get: function () {
      return $(this.form).find("input[name=first_name]").val().trim();

    }
  });
  Object.defineProperty(SignUpForm.prototype, 'last_name', {
    get: function () {
      return $(this.form).find("input[name=last_name]").val().trim();

    }
  });

  Object.defineProperty(SignUpForm.prototype, 'mobile_number', {
    get: function () {
      return $(this.form).find("input[name=mobile_number]").val().trim();

    }
  });


  Object.defineProperty(SignUpForm.prototype, 'action', {
    get: function () {
      return $(this.form).attr('data-action');
    }
  });

  Object.defineProperty(SignUpForm.prototype, 'method', {
    get: function () {
      return $(this.form).attr('method');
    }
  });

  SignUpForm.prototype.isValid = function () {
    var signUp = new SignUpForm(this.form);
    for (let i = 0; i < signUp.fields; i += 1) {
      const name = signUp.fields[i];
      if (this.form.find('#f-' + name).hasClass('is-invalid')) {
        return false;
      }
    }
    return true;
  };

  SignUpForm.prototype.handleComplete = function () {
    $(this.form).find("button").removeAttr("disabled");
  };

  SignUpForm.prototype.submit = function () {
    const data = {
        username: this.username,
        email: this.email,
        password: this.password,
        first_name: this.first_name,
        last_name: this.last_name,
        mobile_number: this.mobile_number,
      }
    ;

    $.ajax({
      url: this.action, type: this.method, data: JSON.stringify(data),
      cache: false, contentType: "application/json", dataType: "json",
      success: SignUpForm.handleSuccess, error: this.handleError.bind(this),
      complete: this.handleComplete.bind(this),
      headers: {'X-CSRFToken': csrftoken}
    });
  };

  $(document).ready(function () {
    $("#singUpForm").submit(function (event) {
      event.preventDefault();
      const form = new SignUpForm(this);
      if (form.isValid()) {
        form.submit();
      }
    });
  });
})(jQuery);