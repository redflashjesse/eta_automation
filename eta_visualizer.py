import plotly.graph_objs as go
from flask import render_template, Flask
from datetime import datetime
import pandas as pd
import re

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
                # Extract values and units from cells
                values = []
                units = ''
                for cell in data[column]:
                    match = re.match(r"([-+]?\d*\.\d+|\d+)(.*)", str(cell))
                    if match:
                        values.append(float(match.group(1)))
                        units = match.group(2).strip()
                    else:
                        values.append(float('nan'))
                fig = go.Figure() # todo maker thourough an x setting and line setting for the plot betwenn the points --
                fig.add_trace(go.Scatter(x=timestamps, y=values, mode='markers', name=column))
                # Append units to y-axis title
                fig.update_layout(title=f'Verlauf von {column}', xaxis_title='Zeit', yaxis_title=f"{column} [{units}]")
                plots.append(fig.to_json())
            except ValueError:
                continue
    return plots


if __name__ == "__main__":
    app.run(debug=True)
