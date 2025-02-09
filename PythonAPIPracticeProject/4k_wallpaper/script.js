$(document).ready(function(){
    $("#file-input").on("change", function(){
        var files = $(this)[0].files;
        $("#preview-container").empty();
        if(files.length > 0){
            for(var i = 0; i < files.length; i++){
                var reader = new FileReader();
                reader.onload = function(e){
                    $("<div class='preview'><img src='" + e.target.result + "'><button class='delete'>Delete</button></div>").appendTo("#preview-container");
                };
                reader.readAsDataURL(files[i]);
            }
        }
    });

    $("#preview-container").on("click", ".delete", function(){
        $(this).parent(".preview").remove();
        $("#file-input").val(""); // Clear input value if needed
    });
    
});
