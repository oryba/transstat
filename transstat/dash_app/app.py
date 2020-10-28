import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

from data import get_count_data, get_model_stats, get_cities
from helpers import const, types


def create_app():
    external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    cities = get_cities()

    app.layout = html.Div(
        className='mx-5',
        children=[
            html.H1(
                className="text-center",
                children='Статистика міського транспорту України'
            ),

            html.Div(
                className="text-center m-auto w-50",
                children=dcc.Dropdown(
                    id='city',
                    options=[{'label': c.name, 'value': c.id} for c in cities],
                    value=1,
                    placeholder="Виберіть місто",
                ),
            ),

            dcc.Checklist(
                options=[
                    {'label': 'Групувати по тижням', 'value': 'group_by_weeks'},
                ],
                value=['group_by_weeks'],
                id="count_options"
            ),

            dcc.Loading(
                id="loading_count",
                children=html.Div(
                    id='count_output'
                ),
            ),

            dcc.Checklist(
                options=[
                    {'label': 'Тільки робочі', 'value': 'working_only'},
                    {'label': 'Включити службові та музейні', 'value': 'include_serv'},
                ],
                value=['working_only'],
                id="model_options",
                labelStyle={'display': 'block'}
            ),

            dcc.Loading(
                id="loading_models_stats",
                children=html.Div(
                    id='models_output'
                )
            ),
        ])

    @app.callback(
        Output('count_output', 'children'),
        [Input('city', 'value'), Input('count_options', 'value')]
    )
    def update_chart(city_id, count_options):
        selected_df = get_count_data(city_id, types.HashablePlainList(count_options))
        colors_seq = ['#db2c09', '#ffb0a1', '#0980db', '#a6d8ff'] if 'group_by_weeks' in count_options else ['#db2c09',
                                                                                                             '#0980db']
        fig = px.line(
            selected_df,
            x="Date",
            y="Count",
            color_discrete_sequence=colors_seq,
            color="Type")

        fig.update_layout(plot_bgcolor='#fffdeb', yaxis={"gridcolor": "#cfcfcf"})

        return dcc.Graph(
            id='count-graph',
            figure=fig
        )

    @app.callback(
        Output('models_output', 'children'),
        [Input('city', 'value'), Input('model_options', 'value')]
    )
    def update_chart(city_id, model_options):
        model_stats = get_model_stats(city_id, types.HashablePlainList(model_options))

        if model_stats is None:
            return html.Center("Дані ще не готові")

        figs = [dcc.Graph(
            id=f'model-stats-{t}',
            className='col-sm-12 col-lg-6',
            figure=px.pie(
                model_stats[model_stats['type'] == t],
                values='count',
                names='model',
                title='Моделі РС',
            )
        ) for t in const.TYPE.values()]

        return html.Div(
            className="row",
            children=figs
        )

    return app
