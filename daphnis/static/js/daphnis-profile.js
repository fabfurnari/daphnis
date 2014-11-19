$(document).ready(function() {
    $("#password").keyup(function() {
        if ($("#password").val().length < 5) {
            $("input[id='pw_submit']").prop("disabled",true);
            $("#password").parents('.form-group').addClass('has-error');
        }
        else {
            $("#password").parents('.form-group').removeClass('has-error');
            $("#password").parents('.form-group').addClass('has-success');
        }
    });
    $("#r_password").keyup(function() {
        var password = $("#password").val();
        var confirmPassword = $("#r_password").val();
        
        if (password != confirmPassword) {
            $("input[id='pw_submit']").prop("disabled",true);
            $("#r_password").parents('.form-group').addClass('has-error');
        }
        else {
            $("input[id='pw_submit']").prop("disabled",false);
            $("#r_password").parents('.form-group').removeClass('has-error');
            $("#r_password").parents('.form-group').addClass('has-success');
        }
    });
    $("#confirmation").keyup(function() {
        if ($("#confirmation").val() == 'yesiwant') {
            $("input[id='deluser']").prop("disabled",false);
            $("#confirmation").parents('.form-group').addClass('has-error');
            
        }});
});
