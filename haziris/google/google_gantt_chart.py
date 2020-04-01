import json

GOOGLE_GANTT_CHART_HTML = """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <title>Haziris: Google Gantt Chart</title>
</head>
<script src="https://www.gstatic.com/charts/loader.js"></script>
<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>

<body>
 <div id='chart-div'></div>
  <script>
    function googleGanttChart( df, options ){
      google.charts.load('current', {'packages': ['gantt']})

      $('#chart-div')
          .width(  0.95*window.innerWidth  )
          .height( 0.95*window.innerHeight )

      google.charts.setOnLoadCallback( chart )

      function chart(){
        let mapRow = (r => ([
           r[ 'Task ID'         ],
           r[ 'Task Name'       ],
           r[ 'Resource'        ],
           r[ 'Start Date'      ] != null ? new Date(r['Start Date']) : null,
           r[ 'End Date'        ] != null ? new Date(r['End Date'  ]) : null,
           r[ 'Duration'        ],
           r[ 'Percent Complete'],
           r[ 'Dependencies'    ]
        ]))

        let ganttData = df.map( r => mapRow(r) )

        let data =  new google.visualization.DataTable();

        data.addColumn( 'string', 'Task ID'          );
        data.addColumn( 'string', 'Task Name'        );
        data.addColumn( 'string', 'Resource'         );
        data.addColumn( 'date'  , 'Start Date'       );
        data.addColumn( 'date'  , 'End Date'         );
        data.addColumn( 'number', 'Duration'         );
        data.addColumn( 'number', 'Percent Complete' );
        data.addColumn( 'string', 'Dependencies'     );

        data.addRows(ganttData)

        let chart = new google.visualization.Gantt(document.getElementById('chart-div'));

        chart.draw( data, options );
      }
  }
  googleGanttChart(
    //haziris_data//
  )
  </script>
 </div>
</body>
</html>
"""

def google_gantt_chart( df, out_file, options=None ):
  """
  Args:
    df       : Pandas data frame.
    out_file : HTML output file to be created
    options  : optional dictionary with options for the visualization
  """

  with open(out_file, 'w') as f:

    haziris_data = (
      df.to_json(orient='records', indent=4) +
      ',' +
      json.dumps( options or {}, indent=4 )
    )

    f.write( GOOGLE_GANTT_CHART_HTML.replace('//haziris_data//', haziris_data ) )
