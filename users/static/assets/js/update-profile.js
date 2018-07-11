const UpdateProfile = (function ($) {

    const AjaxRequest = function (formData) {
        $.ajax({
            url: '/update-profile',
            method: 'POST',
            data: formData,
            cache: false,
            processData: false,
            contentType: false,
            beforeSend: function () {
                $('span.loader').html("<img src='/static/assets/images/loader.gif'>");
                $('button#update').attr('disabled', 'disabled');
            },
            success: function (res) {
                $('span.loader').html("");
                $('button#update').removeAttr('disabled');

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
    };

    const postDetails = function () {
        $("form[name='updateProfile']").submit(function (e) {
            e.preventDefault();
            e.stopPropagation();

            let avatar = $('input#avatar').get(0).files[0];
            let form = document.updateProfile;
            let form_data = new FormData();
            form_data.set("avatar", avatar);
            form_data.set("first_name", form.first_name.value);
            form_data.set("last_name", form.last_name.value);
            form_data.set("dob", form.dob.value);
            form_data.set("gender", form.gender.value);
            form_data.set("email", form.email.value);
            form_data.set("phone", form.phone.value);
            form_data.set("marital_status", form.marital_status.value);
            form_data.set("address", form.address.value);
            form_data.set("city", form.city.value);
            form_data.set("state", form.state.value);
            form_data.set("country", form.country.value);
            form_data.set("bio", form.bio.value);
            form_data.set("department", form.department.value);
            form_data.set("position", form.position.value);
            form_data.set("work_type", form.work_type.value);
            form_data.set("date_employed", form.date_employed.value);
            form_data.set("work_status", form.work_status.value);
            form_data.set("csrfmiddlewaretoken", form.csrfmiddlewaretoken.value);

            AjaxRequest(form_data);
        });
    };

    const displayAvatar = function () {
        $('input#avatar').on('change', function (evt) {
            let f = evt.target.files[0]; // FileList object
            let reader = new FileReader();

            // Closure to capture the file information.
            reader.onload = (function (theFile) {
                return function (e) {
                    // Render thumbnail.
                    $('img.img-thumbnail').attr('src', e.target.result);
                };
            })(f);

            // Read in the image file as a data URL.
            reader.readAsDataURL(f);
        });
    };

    const displayAvatarName = function () {

        $(document).on('change', ':file', function () {
            let input = $(this),
                numFiles = input.get(0).files ? input.get(0).files.length : 1,
                label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
            input.trigger('fileselect', [numFiles, label]);
        });

        $(':file').on('fileselect', function (event, numFiles, label) {
            let input = $(this).parents('.input-group').find(':text'),
                log = numFiles > 1 ? numFiles + ' files selected' : label;

            if (input.length) {
                input.val(log);
            } else {
                if (log) alert(log);
            }

        });
    };

    return {
        init: function () {
            displayAvatarName();
            displayAvatar();
            postDetails();
        }
    }
})(jQuery);

$(document).ready(function () {
    UpdateProfile.init();
});