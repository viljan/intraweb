$(function() {
    $(".execute_button").click(function() {
        var button = $(this);
        button.addClass("disabled");
        execute_utility($(this).attr("data-id"), 
            function(msg){
                button.siblings(".list-group-item-text").after(msg);
                button.removeClass("disabled");
            },
            function() {
                button.removeClass("disabled");
            }
        );
    });
    
    $("#backup_form").submit(function() {
        var button = $(this).children("#backup_button");
        button.addClass("disabled");
        var form = $(this);
        execute_backup($(this).serialize(), 
            function(msg) {
                form.siblings(".list-group-item-text").after(msg);
                button.removeClass("disabled");
            },
            function() {
                button.removeClass("disabled");
            }
        );
        return false;
    });
    
    $("#restore_select_database").change(function() {
        var select_database = $(this);
        get_backups(select_database.val(), 
            function(msg){
                var select_backup = $("#restore_select_backup");
                select_backup.html(msg);
                select_backup.prop('disabled', false);
            }
        );
    });
    
    $("#restore_form").submit(function() {
        var button = $(this).children("#restore_button");
        button.addClass("disabled");
        var form = $(this);
        execute_restore($(this).serialize(), 
            function(msg) {
                form.siblings(".list-group-item-text").after(msg);
                button.removeClass("disabled");
            },
            function() {
                button.removeClass("disabled");
            }
        );
        return false;
    });
});

function execute_utility(utility_id, success_fn, error_fn) {
    $.ajax({
        url: "/utility/" + utility_id + "/execute/",
        type: "POST",
        success: success_fn,
        error: error_fn
    });
}

function execute_backup(form_data, success_fn, error_fn) {
    $.ajax({
        url: "/utility/backup/execute/",
        type: "POST",
        data: form_data,
        success: success_fn,
        error: error_fn
    });
}

function execute_restore(form_data, success_fn, error_fn) {
    $.ajax({
        url: "/utility/restore/execute/",
        type: "POST",
        data: form_data,
        success: success_fn,
        error: error_fn
    });
}

function get_backups(db_name, success_fn) {
    $.ajax({
        url: "/utility/restore/backups/",
        type: "POST",
        data: {'database': db_name},
        success: success_fn
    });
}