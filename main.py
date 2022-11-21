import dash
import plotly.express as px
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

df = pd.read_csv("dt.csv")

print(df.iloc[:5, [0, 2, 3, 4, 14, 15, 18]])
print(df.Collection_complete.nunique())
print(sorted(df.Collection_complete.unique()))
print(sorted(df.id.unique()))


#------------------------------------------------------------------------

# fig_pie = px.pie(data_frame=df, names='Version', values='Collection_complete', title=('Круговая диаграмма заряженных коллекций'))
# fig_pie = px.pie(data_frame=df, names='Version', values='Level', title=('Круговая диаграмма набранных уровней'))
# fig_pie = px.pie(data_frame=df, names='Version', values='Buy_energy', title=('Круговая диаграмма покупки энергетиков'))
fig_pie = px.pie(data_frame=df, names='Version', values='M3_finish', title=('Круговая диаграмма успешно завершенных уровней match-3'))
fig_pie.show()

# fig_bar = px.bar(data_frame=df, x='Version', y='Buy_gold')
# fig_bar.show()

# fig_hist = px.histogram(data_frame=df, x='Version', y='Buy_food', color="Version", title=('Гистограмма купленной еды'))
# fig_hist.show()

# fig_hist = px.histogram(data_frame=df, x='Version', y='Buy_amulet', color="Version", title=('Гистограмма купленных амулетов'))

# fig_hist = px.histogram(data_frame=df, x='Version', y='M3_start', color="Version", title=('Гистограмма стартов Match-3 уровней'))
# fig_hist.show()

#------------------------------------------------------------------------


#----------------------------Версия с фильтром---------------------------
# app = dash.Dash(__name__)
#
# app.layout=html.Div([
#     html.H1("Графики Cradle of Empires"),
#     dcc.Dropdown(id='Version',
#                  options=[{'label':x, 'value':x}
#                         for x in sorted(df.Version.unique())],
#                  value='v1'
#                  ),
#     dcc.Graph(id='my-graph', figure={}
#               )
# ])
#
# @app.callback(
#     Output(component_id='my-graph', component_property='figure'),
#     Input(component_id='Version', component_property='value')
# )
# def interactive_graph(value_Version):
#     print(value_Version)
#     dff = df[df.Version==value_Version]
#     fig = px.bar(data_frame=df, x='Version', y='Buy_energy')
#     return fig
#
# if __name__ =='__main__':
#     app.run_server()
#------------------------------------------------------------------------