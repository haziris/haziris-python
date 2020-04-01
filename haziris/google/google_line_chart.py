import json

GOOGLE_LINE_CHART_HTML = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title>Haziris: Google Line Chart</title>
</head>
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>

<body>
 <div id='chart-div'></div>
  <script>
    function googleLineChart( df, intervals, options ){

      google.charts.load('current', {'packages': ['corechart']})

      $('#chart-div')
          .width(  0.95*window.innerWidth  )
          .height( 0.95*window.innerHeight )

      google.charts.setOnLoadCallback( chart )

      function chart(){
        let data = new google.visualization.DataTable();
        
        df[0].forEach(function(col,i){  
          if(i==0) data.addColumn(typeof df[1][0] === 'string' ? 'string' : 'number', col)
          else if(intervals.includes(col)) data.addColumn({id:col,type: 'number',role: 'interval'})
          else data.addColumn('number', col)
        })

        data.addRows(df.slice(1))

        let chart = new google.visualization.LineChart(document.getElementById('chart-div'));

        chart.draw( data, options );
      }
    }
 
    googleLineChart(
      //haziris_data//
    )
  </script>
 </div>
</body>
</html>
"""

def google_line_chart( df, out_file, options=None, intervals =[]):
  """
  Args:
    df       : Pandas data frame.
    out_file : HTML output file to be created
    options  : optional dictionary with options for the visualization
    intervals: Optional list of columns in df to be used as intervals
  """

  with open(out_file, 'w') as f:

    haziris_data = (
      json.dumps( [list( df.columns )] + df.values.tolist(), indent=4 ) +
      ',' +
      json.dumps( intervals ) +
      ',' +
      json.dumps( options or {}, indent=4 )
    )

    f.write( GOOGLE_LINE_CHART_HTML.replace('//haziris_data//', haziris_data ) )


