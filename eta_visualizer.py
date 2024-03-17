import plotly.graph_objs as go
from flask import render_template, Flask
from datetime import datetime
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    print('---loading data for monitoring form file---')
    data = load_data()
    print('---creating plots---')
    plots = create_plots(data)
    print('---rendering template---')
    return render_template('index.html', plots=plots)


# load in the data.csv to pandas
def load_data():
    df = pd.read_csv('data.csv')
    df.set_index('Zeit', inplace=True)
    print(df.head())
    return df


def create_plots(data):
    plots = []
    timestamps = [datetime.strptime(ts.strip(), '%d.%m.%Y %H:%M:%S') for ts in data.index]
    for column in data.columns:
        if column != 'Zeit':
            try:
                values = data[column].apply(lambda x: float(str(x).replace('°C', '')
                                                            .replace('bar', '')
                                                            .replace('U/min', '')
                                                            .replace('kg', '')
                                                            .replace('%', '')
                                                            .replace('kW', '')
                                                            .replace('°', '')))
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=timestamps, y=values, mode='lines', name=column))
                fig.update_layout(title=f'Verlauf von {column}', xaxis_title='Zeit', yaxis_title=column)
                plots.append(fig.to_json())
            except ValueError:
                continue
    return plots


if __name__ == "__main__":
    app.run(debug=True)
