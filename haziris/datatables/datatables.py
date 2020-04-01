import json

DATATABLES_HTML = """

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <title>Haziris: Datatable</title>
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.20/css/jquery.dataTables.min.css">
  <style>
    #haziris-datatables{
      padding:5%;
    }
    #haziris-datatables table{
      width:100%;
    }
  </style>
</head>
<script src="https://code.jquery.com/jquery-3.3.1.js"></script>
<script src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>

<body>
  <div id='haziris-datatables'>
  //datatables-table//
  </div>
  <script>
    $(document).ready(function() {
        $('#haziris-datatables > table').DataTable(
          //datatables-options//
        );
    } );
  </script>
 </div>
</body>
</html>

"""

def datatables( html_table, out_file, options=None ):
  """
  Args:
    df       : Pandas data frame.
    out_file : HTML output file to be created
    options  : optional dictionary with options for the datatables
  """

  with open(out_file, 'w') as f:

    html_content = DATATABLES_HTML \
      .replace('//datatables-table//'  , html_table )\
      .replace('//datatables-options//', json.dumps( options or {}, indent=4 ) )

    f.write( html_content )
