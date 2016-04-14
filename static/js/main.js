function loadFunction(name) {
    console.log(name)
     
    $.ajax({
        type: 'GET',
        url: "stations",
        data: name,
        dataType: 'json',
        success: function(result){
            var items = document.getElementById('stations');
            items.innerHTML = "";

            $.each(result, function(index, value){
                var button = document.createElement('input');
                button.setAttribute("type", "button");
                button.setAttribute("value", value.station_name);
                
                items.appendChild(button);

                console.log(value.station_name);
            });
        }
    });
}
