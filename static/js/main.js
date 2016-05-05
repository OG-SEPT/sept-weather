/* 
 * this function loads the station names
*/   
function loadFunction(name) {
     
    $.ajax({
        type: 'GET',
        url: 'stations',
        data: name,
        dataType: 'json',
        success: function(result){
            var station_data = document.getElementById('station');
            station_data.innerHTML = "";

            var add_favorite = document.getElementById('add_favorite');
            add_favorite.innerHTML = "";
            
            var inst = document.getElementById('inst');
            inst.innerHTML = 'Select station name to view observation:';
            var inst_1 = document.getElementById('inst_1');
            inst_1.innerHTML = 'Add to your favorites with: +';


            $.each(result, function(index, value){
                var button = document.createElement('input');
                button.setAttribute('type', 'button');
                button.setAttribute('value', value.station_name);
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
            
            document.getElementById('stations_table').style.display = "block"
             
            // handles the wetaher station data
            var items = document.getElementById('station_data');
            items.innerHTML = "";
            
            $.each(result, function(index, value){
                //Date
                var td = document.createElement('td')
                td.style.backgroundColor = '#f2f2f2';
                td.textContent = value.date; 
                items.appendChild(td);
                //Day
                var td = document.createElement('td');
                td.style.backgroundColor = '#ffffff';
                td.textContent = value.day;
                items.appendChild(td);   
                //min c
                var td = document.createElement('td');
                td.textContent = value.minT;            // MIN
                td.style.backgroundColor = '#f2f2f2'
<<<<<<< HEAD
                items.appendChild(td);
                min.push(value.minT);    
=======
                items.appendChild(td); 
                min.push(value.minT); 
>>>>>>> 0caeffcd7cf21786f2ee041f1fb10b551451626a
                //max c
                var td = document.createElement('td');
                td.textContent = value.maxT;            // MAX
                td.style.backgroundColor = '#ffffff'
                items.appendChild(td);
                max.push(value.maxT);   
                //rain mm
                var td = document.createElement('td');
                td.style.backgroundColor = '#f2f2f2'
                td.textContent = value.rain;
                items.appendChild(td);  
                //evap
                var td = document.createElement('td');
                td.style.backgroundColor = '#ffffff'
                td.textContent = value.evap;
                items.appendChild(td);  
                //sun
                var td = document.createElement('td');
                td.style.backgroundColor = '#f2f2f2'
                td.textContent = value.sun;
                items.appendChild(td);  
                //wind: dir
                var td = document.createElement('td');
                td.style.backgroundColor = '#ffffff'
                td.textContent = value.dirW;
                items.appendChild(td);  
                //wind spd
                var td = document.createElement('td');
                td.style.backgroundColor = '#f2f2f2'
                td.textContent = value.spdW;
                items.appendChild(td);  
                //wind: time
                var td = document.createElement('td');
                td.style.backgroundColor = '#ffffff'
                td.textContent = value.timeW;
                items.appendChild(td);  
                //9am: temp
                var td = document.createElement('td');
                td.style.backgroundColor = '#f2f2f2'
                td.textContent = value.temp9;
                items.appendChild(td);
                am.push(value.temp9);  
                //9am: RH
                var td = document.createElement('td');
                td.style.backgroundColor = '#ffffff'
                td.textContent = value.rh9;
                items.appendChild(td);  
                //9am: Cld
                var td = document.createElement('td');
                td.style.backgroundColor = '#f2f2f2'
                td.textContent = value.cld9;
                items.appendChild(td);  
                //9am: Dir
                var td = document.createElement('td');
                td.style.backgroundColor = '#ffffff'
                td.textContent = value.dir9;
                items.appendChild(td);  
                //9am: Spd
                var td = document.createElement('td');
                td.style.backgroundColor = '#f2f2f2'
                td.textContent = value.spd9;
                items.appendChild(td);  
                //9am: MSLP
                var td = document.createElement('td');
                td.style.backgroundColor = '#ffffff'
                td.textContent = value.mslp9;
                items.appendChild(td);  
                //3pm: Temp
                var td = document.createElement('td');
                td.style.backgroundColor = '#f2f2f2'
                td.textContent = value.temp3;
                items.appendChild(td);
                pm.push(value.temp3);   
                //3pm: RH
                var td = document.createElement('td');
                td.style.backgroundColor = '#ffffff'
                td.textContent = value.rh3;
                items.appendChild(td);  
                //3pm: Cld
                var td = document.createElement('td');
                td.style.backgroundColor = '#f2f2f2'
                td.textContent = value.cld3;
                items.appendChild(td);  
                //3pm: D
                var td = document.createElement('td');
                td.style.backgroundColor = '#ffffff'
                td.textContent = value.dir3;
                items.appendChild(td);  
                //3pm: speed 
                var td = document.createElement('td');
                td.style.backgroundColor = '#f2f2f2'
                td.textContent = value.spd3;
                items.appendChild(td);  
                //3pm: mslp
                var td = document.createElement('td');
                td.style.backgroundColor = '#ffffff'
                td.textContent = value.mslp9;
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

// Open popup window
function openChart(url) {
    
    console.log(min);
    console.log(max); 
    console.log(am); 
    console.log(pm);
    
    popupWindow = window.open(
        url,'popUpWindow','height=700,width=1100,left=125,top=125,resizable=0,titlebar=0,menubar=0,scrollbars=0');       
    }

// import the chart google API stuff
google.charts.load('current', {'packages':['line']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    
    var min = window.opener.min;
    var max = window.opener.max;
    var am = window.opener.am;
    var pm = window.opener.pm;
    
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'Date');
    data.addColumn('number', 'Min');
    data.addColumn('number', 'Max');
    data.addColumn('number', '9am');
    data.addColumn('number', '3pm');
    
    for (var i = 0; i < 30; i++) {
        var j = i + 1;
        data.addRows([
            [ j, parseFloat(min[i]), parseFloat(max[i]), parseFloat(am[i]), parseFloat(pm[i]) ]
        ]);
    }
    
    min.length = 0;
    max.length = 0;
    am.length = 0;
    pm.length = 0;
    
    var options = {
        chart: {
            title: 'Weather Chart',
            subtitle: 'Temperatures (°C)'
        },
        width: 1000,
        height: 600,
        vAxis: {title:'Temperature'},        //Not working for some reason
        hAxis: {minValue: 1}                //Not working for some reason
    };

    var chart = new google.charts.Line(document.getElementById('linechart_material'));
    chart.draw(data, options);
}
