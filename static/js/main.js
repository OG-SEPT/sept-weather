function loadFunction(name) {
    console.log(name)
     
    $.ajax({
        type: 'GET',
        url: "stations",
        data: name,
        success: function(result){
            console.log(result);
            $("#station").html(result.station);
        }
    });
}
