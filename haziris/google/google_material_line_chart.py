import json

GOOGLE_MATERIAL_LINE_CHART_HTML = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title>Haziris: Google Material Line Chart</title>
</head>
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>

<body>
 <div id='chart-div'></div>
  <script>
    function googleMaterialLineChart( df, options ){

      google.charts.load('current', {'packages': ['line']})

      $('#chart-div')
          .width(  0.95*window.innerWidth  )
          .height( 0.95*window.innerHeight )
      
      google.charts.setOnLoadCallback( chart )

      function chart(){
        let chart = new google.charts.Line(document.getElementById('chart-div'));

        chart.draw( google.visualization.arrayToDataTable( df ), options );
      }
  }
  googleMaterialLineChart(
    //haziris_data//
  )
  </script>
 </div>
</body>
</html>
"""

def google_material_line_chart( df, out_file, options=None ):
  """
  Args:
    df       : Pandas data frame.
    out_file : HTML output file to be created
    options  : optional dictionary with options for the visualization
  """

  with open(out_file, 'w') as f:

    haziris_data = (
      json.dumps( [list( df.columns )] + df.values.tolist(), indent=4 ) +
      ',' +
      json.dumps( options or {}, indent=4 )
    )

    f.write( GOOGLE_MATERIAL_LINE_CHART_HTML.replace('//haziris_data//', haziris_data ) )




