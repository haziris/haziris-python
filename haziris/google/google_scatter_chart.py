import json

GOOGLE_SCATTER_CHART_HTML = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title>Haziris: Google Scatter Chart</title>
</head>
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>

<body>
 <div id='chart-div'></div>
  <script>
    function googleScatterChart(current, options, previous){
      
      google.charts.load('current', {'packages': ['corechart']})

      $('#chart-div')
          .width(  0.95*window.innerWidth  )
          .height( 0.95*window.innerHeight )
      
      google.charts.setOnLoadCallback( arguments.length == 2 ? chart : diffChart )

      function chart(){
        let data = google.visualization.arrayToDataTable(current);

        let chart = new google.visualization.ScatterChart(document.getElementById('chart-div'));

        chart.draw(data, options);
      }

      function diffChart(){
        let data = google.visualization.arrayToDataTable(current);

        let chart = new google.visualization.ScatterChart(document.getElementById('chart-div'));

        let prevData = google.visualization.arrayToDataTable(previous);
        let diffData = chart.computeDiff(prevData, data);

        chart.draw(diffData, options);
      }
  }

  googleScatterChart(
    //haziris_data//
  )
  </script>
 </div>
</body>
</html>
"""

def google_scatter_chart(df, out_file, options=None, previous=None):
  """
  Args:
    df       : Pandas data frame. 
    out_file : HTML output file to be created
    options  : optional dictionary with options for the visualization
    previous : Optional data frame for creating a diff chart
  """

  with open(out_file, 'w') as f:

    haziris_data = (
      json.dumps( [list( df.columns )] + df.values.tolist(), indent=4 ) +
      ',' +
      json.dumps( options or {} )
    )

    if previous is not None:
      haziris_data += ',' + json.dumps( [list( previous.columns )] + previous.values.tolist(), indent=4 )

    f.write( GOOGLE_SCATTER_CHART_HTML.replace('//haziris_data//', haziris_data ) )


