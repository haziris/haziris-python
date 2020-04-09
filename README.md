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

Here is an example for creating a Material bar chart

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
- [DataTables](http://vizjs.org/examples/haziris-python-datatables)
- [DataTables - Bootstrap 4 ](http://vizjs.org/examples/haziris-python-datatables_bootstrap4)
- [DataTables - Material](http://vizjs.org/examples/haziris-python-datatables_material)
- [DataTables - Vertical scroll](http://vizjs.org/examples/haziris-python-datatables_vertical_scroll)
- [Google Area](http://vizjs.org/examples/haziris-python-google_area)
- [Google Bar](http://vizjs.org/examples/haziris-python-google_bar)
- [Google Bar Ex1](http://vizjs.org/examples/haziris-python-google_bar_1)
- [Google Bar Stacked](http://vizjs.org/examples/haziris-python-google_bar_stacked)
- [Google Bubble](http://vizjs.org/examples/haziris-python-google_bubble)
- [Google Bubble Temperature](http://vizjs.org/examples/haziris-python-google_bubble_temperature)
- [Google Calendar](http://vizjs.org/examples/haziris-python-google_calendar)
- [Google Candlestick](http://vizjs.org/examples/haziris-python-google_candlestick)
- [Google Column](http://vizjs.org/examples/haziris-python-google_column)
- [Google Column Grouped](http://vizjs.org/examples/haziris-python-google_column_grouped)
- [Google Column Stacked](http://vizjs.org/examples/haziris-python-google_column_stacked)
- [Google Column Stacked Full](http://vizjs.org/examples/haziris-python-google_column_stacked_full)
- [Google Gantt](http://vizjs.org/examples/haziris-python-google_gantt)
- [Google Gantt Grouped](http://vizjs.org/examples/haziris-python-google_gantt_grouping)
- [Google Geo](http://vizjs.org/examples/haziris-python-google_geo)
- [Google Line](http://vizjs.org/examples/haziris-python-google_line)
- [Google Line Interval](http://vizjs.org/examples/haziris-python-google_line_interval)
- [Google Line Interval Area](http://vizjs.org/examples/haziris-python-google_line_interval_area)
- [Google Line Trendlines](http://vizjs.org/examples/haziris-python-google_line_trendlines)
- [Google Material Bar](http://vizjs.org/examples/haziris-python-google_material_bar)
- [Google Material Bar Horizontal](http://vizjs.org/examples/haziris-python-google_material_bar_horizontal)
- [Google Material Line](http://vizjs.org/examples/haziris-python-google_material_line)
- [Google Material Scatter](http://vizjs.org/examples/haziris-python-google_material_scatter)
- [Google Material Scatter Dual Y](http://vizjs.org/examples/haziris-python-google_material_scatter_dual_y)
- [Google Pie](http://vizjs.org/examples/haziris-python-google_pie)
- [Google Pie 3D](http://vizjs.org/examples/haziris-python-google_pie_3d)
- [Google Pie Donut](http://vizjs.org/examples/haziris-python-google_pie_donut)
- [Google Sankey](http://vizjs.org/examples/haziris-python-google_sankey)
- [Google Sankey Multiple](http://vizjs.org/examples/haziris-python-google_sankey_multiple)
- [Google Scatter](http://vizjs.org/examples/haziris-python-google_scatter)
- [Google Scatter Diff](http://vizjs.org/examples/haziris-python-google_scatter_diff)
- [Google Scatter Dual Y](http://vizjs.org/examples/haziris-python-google_scatter_dual_y)
- [Google Stepped Area](http://vizjs.org/examples/haziris-python-google_stepped_area)
- [Google Timeline](http://vizjs.org/examples/haziris-python-google_timeline)
- [Google Timeline Grouping](http://vizjs.org/examples/haziris-python-google_timeline_grouping)
- [Google Timeline Label](http://vizjs.org/examples/haziris-python-google_timeline_label)
- [Google Timeline No Label](http://vizjs.org/examples/haziris-python-google_timeline_no_label)
- [Google Treemap](http://vizjs.org/examples/haziris-python-google_treemap)
- [Google Treemap Highlights](http://vizjs.org/examples/haziris-python-google_treemap_highlights)