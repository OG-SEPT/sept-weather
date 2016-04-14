function loadFunction(name) {
     
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
                var link = value.url;
                button.setAttribute("type", "button");
                button.setAttribute("value", value.station_name);
                button.addEventListener('click', function(){
                    getRequest(value.url);
                });
                
                items.appendChild(button);
                
            });
        }
    });
}


function getRequest(url){
    $.ajax({
        type: 'GET',
        url: "stations_info",
        data: url,
        dataType: 'json',
        success: function(result){
            var items = document.getElementById('station_data');
            items.innerHTML = "";
            
            $.each(result, function(index, value){
                var td = document.createElement('td');
                
                td.textContent = value.date; 
                items.appendChild(td);
                
                var td = document.createElement('td');
                td.textContent = value.day;
                items.appendChild(td);                
                                
                var tr = document.createElement('tr');
                items.appendChild(tr);
            });   

        }
            
    });
}
