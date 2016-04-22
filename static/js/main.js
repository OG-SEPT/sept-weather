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
// Chart Arrays
var min = [];
var max = [];
var am = [];
var pm = [];

// loads the station weather data
function getStationData(url){
    
    $.ajax({
        type: 'GET',
        async: true,
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
                td.textContent = value.minT;            // MIN
                items.appendChild(td);
                min.push(value.minT);  
                
                var td = document.createElement('td');
                td.textContent = value.maxT;            // MAX
                items.appendChild(td);
                max.push(value.maxT);  
                
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
                td.textContent = value.temp9;            // 9AM
                items.appendChild(td);
                am.push(value.temp9);
                
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
                td.textContent = value.temp3;            // 3PM
                items.appendChild(td);
                pm.push(value.temp3);  
                
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

function resetDatabase() {
    $.ajax({
        type: 'GET',
        url: 'reset_database',
        success: function(result){
            console.log("success");
        }
    });
}

   
// Open window 
function openChart(url) {
    
    console.log(min);
    console.log(max); 
    console.log(am); 
    console.log(pm);
    
    popupWindow = window.open(
        url,'popUpWindow','height=650,width=1100,left=125,top=125,resizable=0,titlebar=0,menubar=0,scrollbars=0');       
}

// Chart
google.charts.load('current', {'packages':['line']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    
    var min = window.opener.min;
    var max = window.opener.max;
    var am = window.opener.am;
    var pm = window.opener.pm;
    
//    min = parseFloat(min);
//    max = parseFloat(max);
//    am = parseFloat(am);
//    pm = parseFloat();
    
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Days');
    data.addColumn('number', 'Min');
    data.addColumn('number', 'Max');
    data.addColumn('number', '9am');
    data.addColumn('number', '3pm');
    
    console.log(min);
    console.log(max); 
    console.log(am); 
    console.log(pm);
    
    for (var i = 0; i < 21; i++) {
        data.addRows([
            [ i, parseFloat(min[i]), parseFloat(max[i]), parseFloat(am[i]), parseFloat(pm[i]) ]
        ]);
    }
    
    var options = {
        chart: {
            title: 'Weather Chart',
        },
        width: 1000,
        height: 600
    };

    var chart = new google.charts.Line(document.getElementById('linechart_material'));
    chart.draw(data, options);
}



