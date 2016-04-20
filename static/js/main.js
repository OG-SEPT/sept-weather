// loads the station names
function loadFunction(name) {
     
    $.ajax({
        type: 'GET',
        url: "stations",
        data: name,
        dataType: 'json',
        success: function(result){
            var station_data = document.getElementById('station');
            station_data.innerHTML = "";

            var add_favorite = document.getElementById('add_favorite');
            add_favorite.innerHTML = "";

            $.each(result, function(index, value){
                var button = document.createElement('input');
                button.setAttribute("type", "button");
                button.setAttribute("value", value.station_name);
                button.addEventListener('click', function(){
                    getStationData(value.url);
                });
                station_data.appendChild(button);
                
                
                var fav_button = document.createElement('input');
                fav_button.setAttribute("type", "button");
                fav_button.setAttribute("value", "fav");
                fav_button.addEventListener('click', function(){
                    addFavorite(value.url);
                });
                station_data.appendChild(fav_button); 
            });
        }
    });
}

// adds a station to favorite 
// display graph here
function addFavorite(url){
    
    $.ajax({
        type: 'GET',
        url: 'station_fav',
        data: url,
        dataType: 'json',
        success: function(result){
            console.log("success!: " + result);
        }
    });
}

// loads the station weather data
function getStationData(url){
    $.ajax({
        type: 'GET',
        url: 'stations_info',
        data: url,
        dataType: 'json',
        success: function(result){

            // handles the wetaher station data
            var items = document.getElementById('station_data');
            items.innerHTML = "";
            
            $.each(result, function(index, value){
                var td = document.createElement('td');
                td.textContent = value.date; 
                items.appendChild(td);
                
                var td = document.createElement('td');
                td.textContent = value.day;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.minT;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.maxT;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.rain;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.evap;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.sun;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.dirW;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.spdW;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.timeW;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.temp9;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.rh9;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.cld9;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.dir9;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.spd9;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.mslp9;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.temp3;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.rh3;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.cld3;
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.dir3;
                items.appendChild(td);
                
                var td = document.createElement('td');
                td.textContent = value.spd3;
                items.appendChild(td);    
                
                var td = document.createElement('td');
                td.textContent = value.mslp3;
                items.appendChild(td);  
                         
                var tr = document.createElement('tr');
                items.appendChild(tr);


            });   

        }
            
    });
}
