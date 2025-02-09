// $(document).ready(function(){
//     $("#file-input").on("change", function(){
//         var files = $(this)[0].files;
//         $("#preview-container").empty();
//         if(files.length > 0){
//             for(var i = 0; i < files.length; i++){
//                 var reader = new FileReader();
//                 reader.onload = function(e){
//                     $("<div class='preview'><img src='" + e.target.result + "'><button class='delete'>Delete</button></div>").appendTo("#preview-container");
//                 };
//                 reader.readAsDataURL(files[i]);
//             }
//         }
//     });

//     $("#preview-container").on("click", ".delete", function(){
//         $(this).parent(".preview").remove();
//         $("#file-input").val(""); // Clear input value if needed
//     });
    
// });


$(document).ready(function(){
    $("#file-input").on("change", function(){
        var files = $(this)[0].files;
        $("#preview-container").empty();
        
        if(files.length > 0){
            for(let i = 0; i < files.length; i++){
                let file = files[i];
                let reader = new FileReader();
                
                reader.onload = function(e){
                    let img = new Image();
                    img.src = e.target.result;
                    
                    img.onload = function(){
                        let width = this.width;
                        let height = this.height;
                        
                        let previewHtml = `
                            <div class='preview'>
                                <img src='${e.target.result}' alt='Image Preview'>
                                <p>Size: ${width} x ${height} px</p>
                                <button class='delete'>Delete</button>
                            </div>`;
                        
                        $("#preview-container").append(previewHtml);
                    };
                };
                
                reader.readAsDataURL(file);
            }
        }
    });

    $("#preview-container").on("click", ".delete", function(){
        $(this).parent(".preview").remove();
        $("#file-input").val(""); // Clear input value if needed
    });
});
