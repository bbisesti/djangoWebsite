$(document).ready(function() {

    var backgroundColors = ["#0074D9", "#FF4136", "#2ECC40", "#FF851B", "#7FDBFF", "#B10DC9", "#FFDC00", "#001f3f", "#39CCCC", "#01FF70", "#85144b", "#F012BE", "#3D9970", "#111111", "#AAAAAA"]

    $.ajax({
        url: "/data",
        success: function(data) {

            var labels = [];
            var records = [];
            var colors = [];

            if(data['data'].length > 0) {
                data['data'].forEach(function(record){
                    labels.push(record.help_type);
                    records.push(record.values);
                    var rand = Math.floor(Math.random() * backgroundColors.length);
                    colors.push(backgroundColors[rand]);
                })

                data = {
                    datasets: [{
                        data: records,
                        backgroundColor: colors
                    }],
                    labels: labels,
                };

                var ctx = document.getElementById('resultsPieChart').getContext('2d');

                var chart = new Chart(ctx,{
                    type: 'doughnut',
                    data: data,
                    options: {}
                });

                document.getElementById("resultsPieChart").style.display = 'block';
            } else {
                document.getElementById("errorMessage").innerHTML = 'There were no rows returned';
                document.getElementById("errorMessage").style.display = 'block';
            }

        },
        error: function(err) {
            $('#errorMessage').innerHTML = 'There was an error gathering data';
            $('#errorMessage').style.display = 'block';
        }
    })

    $.ajax({
        url: "/user",
        success: function(data) {

            var labels = [];
            var records = [];
            var colors = [];

            if(data['data'].length > 0) {
                data['data'].forEach(function(record){
                    labels.push(record.first_name);
                    records.push(record.values);
                    var rand = Math.floor(Math.random() * backgroundColors.length);
                    colors.push(backgroundColors[rand]);
                })

                data = {
                    datasets: [{
                        data: records,
                        backgroundColor: colors
                    }],
                    labels: labels,
                };

                var ctx = document.getElementById('userPieChart').getContext('2d');

                var chart = new Chart(ctx,{
                    type: 'doughnut',
                    data: data,
                    options: {}
                });

                document.getElementById("userPieChart").style.display = 'block';
            } else {
                document.getElementById("errorMessage").innerHTML = 'There were no rows returned';
                document.getElementById("errorMessage").style.display = 'block';
            }

        },
        error: function(err) {
            $('#errorMessage').innerHTML = 'There was an error gathering data';
            $('#errorMessage').style.display = 'block';
        }
    })
});