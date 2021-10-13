$(document).ready(function () {
    $("#image_upload_form").submit(function(e) {
        e.preventDefault();
        if (!$('#image_0')[0].files.length || !$('#image_1')[0].files.length){
            show_snackbar_message('Please select images first', 'error');
            return;
        }
        show_snackbar_message('Uploading Images...', 'success');

        let formData = new FormData();
        formData.append('csrfmiddlewaretoken', window.csrfToken);
        formData.append('image_0', $("#image_0")[0].files[0]);
        formData.append('image_1', $("#image_1")[0].files[0]);
        $.ajax({
            url: "/check_muscle/",
            type: "POST",
            data: formData,
            contentType: false,
            processData: false,
            enctype: 'multipart/form-data',
            beforeSend: function () {
                $(".loader").show();
            },
            success: function (resp) {
                if (resp.success) {
                    $('.final_image_div').show();
                    $("#final_image").attr("src",resp.image_str);
                    $('#image_upload_form').hide();
                    show_snackbar_message(resp.message, "success");
                } else {
                    show_snackbar_message(resp.message, "error");
                    $('#image_upload_form').hide();
                }
            },
            error: function () {
                $(".loader").hide();
                show_snackbar_message("Something went wrong.", "error");
            },
            complete: function () {
                $(".loader").hide();
            }
        });
    });
    $(document).on("change", "#image_0, #image_1", function(event) {
        event.preventDefault();
        var img_selector = $(this).parent().find('img');
        if (this.files && this.files[0]) {
          //Reading Seelcted Image
          var reader = new FileReader();
          //Showing Image in Preview
          reader.onload = function(e) {
            img_selector.attr("src", e.target.result);
            img_selector.show();
          };
          reader.readAsDataURL(this.files[0]);
        } else {
            img_selector.hide();
        }
    });
    $(document).on("click", ".do_another", function(event) {
        event.preventDefault();
        $('#image_upload_form').show();
        $('.final_image_div').hide();
        $('#image_0').val("");
        $('#image_1').val("");
        $('#image_0_preview').hide();
        $('#image_1_preview').hide();
    });
});