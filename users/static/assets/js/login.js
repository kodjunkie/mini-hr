const Login = (function ($) {
    // Process Login
    const postLogin = function () {
        $('form#login').submit(function (e) {
            e.preventDefault();
            e.stopPropagation();

            let form = document.login;
            $.ajax({
                url: '/login',
                method: 'POST',
                data: {
                    username: form.username.value,
                    password: form.password.value,
                    csrfmiddlewaretoken: $('meta[name="csrfmiddlewaretoken"]').attr('content')
                },
                beforeSend: function () {
                    $('span.loader').html("<img src='/static/assets/images/loader.gif'>");
                    $('button#login').attr('disabled', 'disabled');
                },
                success: function (res) {
                    $('span.loader').html("");
                    $('button#login').removeAttr('disabled');

                    if (res.error)
                        swal('Oops!', res.msg, 'error');
                    else {
                        swal('Congratulations', res.msg, 'success');
                        setTimeout(function () {
                            document.location.href = '/dashboard';
                        }, 1500);
                    }
                }
            });
        });
    };

    return {
        init: function () {
            postLogin();
        }
    }
})(jQuery);

$(document).ready(function () {
    Login.init();
});