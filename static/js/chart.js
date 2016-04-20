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
		[6,   8.8, 13.6,  7.7, 38]
	]);

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


