function displayLoadScreen() {
    $("#main-content").empty();
    $("body").append(
        '<div class="load-animation">'+
            '<div class="d-flex flex-column align-items-center">'+
            '<strong class="mb-4 text-primary" style="font-size:20px">Loading</strong>'+
                '<div class="spinner-border text-primary" style="height:80px;width:80px;font-size:40px" role="status">'+
                    '<span class="sr-only">Loading...</span>'+
                '</div>'+
            '</div>'+
        '</div>'
    );

}

function removeLoadScreen() {
    $("div").remove(".load-animation");
}
