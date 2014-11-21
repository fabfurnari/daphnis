$(document).ready(function() {
    $('#tags').tagsInput();

    $('#addEntryForm').hide();
    $('#addEntry').on('click', function () {
//        var $btn = $(this).button('loading')

        if($("#addEntryForm").is(":visible")){
           $("#addEntryForm").hide();
        } else {
           $("#addEntryForm").show();
        }
//        $btn.button('reset');
        //don't follow the link (optional, seen as the link is just an anchor)
        return false;
  })
});
