<html>
<head>
<style>
table, th, td {        
        border: 1px solid black;
        border-collapse: collapse;
        }
th, td {        
        padding: 7px;
        text-align: center;
        }
</style>
</head>
<body>
</body>
<script>
var data = {'Aduvie': 0, 'Dessin': 0, 'Employee': 0, 'config': 0, 'testRpa': 0, 'develop': 0, 'teNew': 0, 'Audiotek': 10, 'Sifi': 0, 'highroads': 0, 'test': 0, 'local': 0, 'Kalakshetra':20};   

// Create a new table
var table = document.createElement("table");
table.setAttribute('Border','1');
table.setAttribute('width','100%')

// Add the table header
var tr = document.createElement('tr');
var leftRow = document.createElement('td');
leftRow.innerHTML = "TENANT NAME";
leftRow.style.backgroundColor = '#BDC0C3';
tr.appendChild(leftRow);

var rightRow = document.createElement('td');
rightRow.innerHTML = "Application Count";
rightRow.style.backgroundColor = '#BDC0C3';
tr.appendChild(rightRow);

table.appendChild(tr);

// Add the table rows
for (var name in data) {        
        var value = data[name];
        var tr = document.createElement('tr');
        var leftRow = document.createElement('td');
        leftRow.innerHTML = name;
        tr.appendChild(leftRow);
                            
        var rightRow = document.createElement('td');
        rightRow.innerHTML = value;
        tr.appendChild(rightRow);
                                        
        table.appendChild(tr);
        }

// Add the created table to the HTML page
document.body.appendChild(table);
</script>
<html>
