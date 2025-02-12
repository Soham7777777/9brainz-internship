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
                        
                        const filtered_sizes = window.ValidSizes.filter((size) => size[0] === width && size[1] === height)
                        let previewHtml = ''
                        if(filtered_sizes.length !== 0 ) {
                            previewHtml = `
                            <div class='preview'>
                                <img src='${e.target.result}' alt='Image Preview'>
                                <p>Size: ${width} x ${height}</p>
                            </div>`;
                        } else {
                            previewHtml = `
                            <div class='preview'>
                                <img src='${e.target.result}' alt='Image Preview'>
                                <p style="color:red;">Image with size ${width} x ${height} is not allowed</p>
                            </div>
                            `
                        }
                        
                        $("#preview-container").append(previewHtml);
                    };
                };
                
                reader.readAsDataURL(file);
            }
        }
    });

    $("#preview-container").on("click", ".delete", function(){
        $(this).parent(".preview").remove();
    });
});

// <button class='delete'>Delete</button>

// document.addEventListener("DOMContentLoaded", function(event) {

//     document.querySelector("#file-input").addEventListener("change", function(event) {
//         renderFiles();
//     });


//     function renderFiles() {
//         document.querySelector("#preview-container").innerHTML = ''
//         for (const file of document.querySelector("#file-input").files) {
//             let img = new Image();
//             img.src = window.URL.createObjectURL(file);

//             document.querySelector("#preview-container").innerHTML += `
//                 <div class='preview'>
//                     <img src='${img.src}' alt='Image Preview'>
//                     <p>Size: ${img.naturalWidth} x ${img.naturalHeight} px</p>
//                     <button class='delete'>Delete</button>
//                 </div>
//             `;
//         }
//     }
// });
