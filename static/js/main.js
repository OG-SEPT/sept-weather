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
                fav_button.setAttribute("value", "+");
                fav_button.addEventListener('click', function(){
                    addFavorite(value.url, value.station_name);
                });
                station_data.appendChild(fav_button); 
            });
        }
    });
}


// adds a station to favorite 
// display graph here
function addFavorite(url, name){
    
    $.ajax({
        type: 'GET',
        url: 'station_fav',
        data: {'url': url, 'name': name},
        dataType: 'json',
        success: function(result){
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
            
            document.getElementById('stations_table').style.display = "block"
             
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
                td.textContent = value.minT;            // MIN
                items.appendChild(td);  
                
                var td = document.createElement('td');
                td.textContent = value.maxT;            // MAX
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


// reset the database 
function resetDatabase() {
    
    $.ajax({
        type: 'GET',
        url: 'reset_database',
        success: function(result){
            
            console.log("success");

            document.getElementById("favs").style="display:none";
        }
    });
}


// Chart 
function openChart(url) {
    
    popupWindow = window.open(
        url,'popUpWindow','height=650,width=1100,left=125,top=125');
}


// import the chart google API stuff
google.charts.load('current', {'packages':['line']});
google.charts.setOnLoadCallback(drawChart);


function drawChart() {

    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Days');
    data.addColumn('number', 'Min');
    data.addColumn('number', 'Max');
    data.addColumn('number', '9am');
    data.addColumn('number', '3pm');
    

    data.addRows([
        [1,  37.8, 80.8, 41.8, 23],
        [2,  30.9, 69.5, 32.4, 56],
        [3,  25.4,   57, 25.7, 23],
        [4,  11.7, 18.8, 10.5, 23],
        [5,  11.9, 17.6, 10.4, 86],
        [6,   8.8, 13.6,  7.7, 38],
        [7,  11.9, 17.6, 10.4, 86],
        [8,  11.9, 17.6, 10.4, 86],
        [9,  11.9, 17.6, 10.4, 86],
        [10,  11.9, 17.6, 10.4, 86],
        [11,  11.9, 17.6, 10.4, 86],
        [12,  11.9, 17.6, 10.4, 86],
        [13,  11.9, 17.6, 10.4, 86],
        [14,  11.9, 17.6, 10.4, 86],
        [15,  11.9, 17.6, 10.4, 86],
        [16,  11.9, 17.6, 10.4, 86],
        [17,  11.9, 17.6, 10.4, 86],
        [18,  11.9, 17.6, 10.4, 86],
        [19,  11.9, 17.6, 10.4, 86],
        [20,  11.9, 17.6, 10.4, 86]
    ]);

    var options = {
        chart: {
            title: 'Weather Chart',
        },
        width: 1000,
        height: 600,
    };

    var chart = new google.charts.Line(document.getElementById('linechart_material'));

    chart.draw(data, options);
}

