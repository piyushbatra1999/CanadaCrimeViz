"""
A sample of 8 of the 26 Bootstrap themed Plotly figure templates available
in the dash-bootstrap-template library

"""
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.express as px
from data_youth import initial_entry_status_pie_chart, plot_actual_in_counts

df = px.data.gapminder()
# fig1 = initial_entry_status_pie_chart(1999, 2001, ['Alberta'])
fig2 = plot_actual_in_counts(2018,2022)
figures = [fig2]

templates = [
    "bootstrap",
    "minty",
    "pulse",
    "flatly",
    "quartz",
    "cyborg",
    "darkly",
    "vapor",
]

load_figure_template(templates)

# figures = [
#     px.scatter(
#         df.query("year==2007"),
#         x="gdpPercap",
#         y="lifeExp",
#         size="pop",
#         color="continent",
#         log_x=True,
#         size_max=60,
#         template=template,
#         title="Gapminder 2007: '%s' theme" % template,
#     )
#     for template in templates
# ]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([dcc.Graph(figure=fig, className="m-4") for fig in figures])

if __name__ == "__main__":
    app.run_server(debug=True)