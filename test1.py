import pandas as pd
import numpy as np
import holoviews as hv
import bokeh

print(bokeh.__version__)
print(hv.__version__)

hv.extension('bokeh')
station_info = pd.read_csv('assets/station_info.csv')
station_info.head()
scatter = hv.Scatter(station_info, kdims=['services'], vdims=['ridership'])
scatter

