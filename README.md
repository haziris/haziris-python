# haziris
Visualizations for Python

- [Wiki](https://github.com/haziris/haziris-python/wiki)

## Installation
Binary installers for the latest released version are available at the [Python
package index](https://pypi.org/project/haziris/) 

```sh
pip install haziris
```

### Google Charts
The package contains a number of wrapper python modules to create Google charts in an HTML file from a pandas data frame.

An example for creating a Material bar chart:

```py
import pandas as pd
import haziris as hz

df = pd.DataFrame([
    ['2014', 1000,  400, 200],
    ['2015', 1170,  460, 250],
    ['2016',  660, 1120, 300],
    ['2017', 1030,  540, 350]
  ],
  columns = ['Year', 'Sales', 'Expenses', 'Profit']
)

hz.google_material_bar_chart(df, "Google material bar.html", {'legned':'None'})
```

The examples folder, contains more such examples.


### Examples
- [DataTables](http://haziris.org/examples/haziris-python-datatables.html)
- [DataTables - Bootstrap 4 ](http://haziris.org/examples/haziris-python-datatables_bootstrap4.html)
- [DataTables - Material](http://haziris.org/examples/haziris-python-datatables_material.html)
- [DataTables - Vertical scroll](http://haziris.org/examples/haziris-python-datatables_vertical_scroll.html)
- [Google Area](http://haziris.org/examples/haziris-python-google_area.html)
- [Google Bar](http://haziris.org/examples/haziris-python-google_bar.html)
- [Google Bar Grouped](http://haziris.org/examples/haziris-python-google_bar_1.html)
- [Google Bar Stacked](http://haziris.org/examples/haziris-python-google_bar_stacked.html)
- [Google Bubble](http://haziris.org/examples/haziris-python-google_bubble.html)
- [Google Bubble Temperature](http://haziris.org/examples/haziris-python-google_bubble_temperature.html)
- [Google Calendar](http://haziris.org/examples/haziris-python-google_calendar.html)
- [Google Candlestick](http://haziris.org/examples/haziris-python-google_candlestick.html)
- [Google Column](http://haziris.org/examples/haziris-python-google_column.html)
- [Google Column Grouped](http://haziris.org/examples/haziris-python-google_column_grouped.html)
- [Google Column Stacked](http://haziris.org/examples/haziris-python-google_column_stacked.html)
- [Google Column Stacked Full](http://haziris.org/examples/haziris-python-google_column_stacked_full.html)
- [Google Gantt](http://haziris.org/examples/haziris-python-google_gantt.html)
- [Google Gantt Grouped](http://haziris.org/examples/haziris-python-google_gantt_grouping.html)
- [Google Geo](http://haziris.org/examples/haziris-python-google_geo.html)
- [Google Line](http://haziris.org/examples/haziris-python-google_line.html)
- [Google Line Interval](http://haziris.org/examples/haziris-python-google_line_interval.html)
- [Google Line Interval Area](http://haziris.org/examples/haziris-python-google_line_interval_area.html)
- [Google Line Trendlines](http://haziris.org/examples/haziris-python-google_line_trendlines.html)
- [Google Material Bar](http://haziris.org/examples/haziris-python-google_material_bar.html)
- [Google Material Bar Horizontal](http://haziris.org/examples/haziris-python-google_material_bar_horizontal.html)
- [Google Material Line](http://haziris.org/examples/haziris-python-google_material_line.html)
- [Google Material Scatter](http://haziris.org/examples/haziris-python-google_material_scatter.html)
- [Google Material Scatter Dual Y](http://haziris.org/examples/haziris-python-google_material_scatter_dual_y.html)
- [Google Pie](http://haziris.org/examples/haziris-python-google_pie.html)
- [Google Pie 3D](http://haziris.org/examples/haziris-python-google_pie_3d.html)
- [Google Pie Donut](http://haziris.org/examples/haziris-python-google_pie_donut.html)
- [Google Sankey](http://haziris.org/examples/haziris-python-google_sankey.html)
- [Google Sankey Multiple](http://haziris.org/examples/haziris-python-google_sankey_multiple.html)
- [Google Scatter](http://haziris.org/examples/haziris-python-google_scatter.html)
- [Google Scatter Diff](http://haziris.org/examples/haziris-python-google_scatter_diff.html)
- [Google Scatter Dual Y](http://haziris.org/examples/haziris-python-google_scatter_dual_y.html)
- [Google Stepped Area](http://haziris.org/examples/haziris-python-google_stepped_area.html)
- [Google Timeline](http://haziris.org/examples/haziris-python-google_timeline.html)
- [Google Timeline Grouping](http://haziris.org/examples/haziris-python-google_timeline_grouping.html)
- [Google Timeline Label](http://haziris.org/examples/haziris-python-google_timeline_label.html)
- [Google Timeline No Label](http://haziris.org/examples/haziris-python-google_timeline_no_label.html)
- [Google Treemap](http://haziris.org/examples/haziris-python-google_treemap.html)
- [Google Treemap Highlights](http://haziris.org/examples/haziris-python-google_treemap_highlights.html)