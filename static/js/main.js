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
                var stations_link = document.createElement('a');
                var stations = document.createElement('tr');
                
                stations.innerHTML = value.station_name;
                stations_link.innerHTML = value.url;
                items.appendChild(stations);
                items.appendChild(stations_link);

                console.log(value.station_name);
            });
        }
    });
}
