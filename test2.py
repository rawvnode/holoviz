source = ColumnDataSource(df)

hover =HoverTool(
    tooltips=[("Count", "@count")]
)

plot = Bar(df
        , 'start_date'
        , values='count'
        , agg='median'
        , title='Test'
        , legend='top_left'
        , bar_width=0.6
        , group='os'
        , color='os'
        , palette=["green", PuBu[7][2]]
        , source=source)

plot.add_tools(hover)

output_notebook()
show(plot)
