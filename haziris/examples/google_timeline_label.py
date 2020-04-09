import pandas as pd
import haziris as hz

df = pd.DataFrame([
    [ '1', 'George Washington', '1789-03-30 00:00:00', '1797-02-04 00:00:00' ],
    [ '2', 'John Adams'       , '1797-02-04 00:00:00', '1801-02-04 00:00:00' ],
    [ '3', 'Thomas Jefferson' , '1801-02-04 00:00:00', '1809-02-04 00:00:00' ]
  ],
  columns = [ 'Term', 'Name', 'Start', 'End' ]
)

hz.google_timeline_chart( df, "google_timeline_label.html" )
