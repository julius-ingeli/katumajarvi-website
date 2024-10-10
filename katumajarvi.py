from flask import Flask, render_template, redirect, url_for
import pandas as pd
from datetime import datetime

app = Flask(__name__, template_folder="templates")
file_path = 'C:\\Users\\julko\\Desktop\\School stuff\\HAMK\\yr2\\module1\dfproj\\katumajarvi-website\\data.csv'

def get_temperature_data():
    df = pd.read_csv(file_path, delimiter=';')
    return df['ts'].tolist(), df['temperature'].tolist()


def get_ph_data():
    df = pd.read_csv(file_path, delimiter=';')
    return df['ts'].tolist(), df['pH'].tolist()

def get_tds_data():
    df = pd.read_csv(file_path, delimiter=';')
    return df['ts'].tolist(), df['Tds'].tolist()


def get_latest_data():
    df = pd.read_csv(file_path, delimiter=';')

    latest_temp = df['temperature'].iloc[-1]
    latest_temp = round(latest_temp, 1)

    latest_ph = df['pH'].iloc[-1]
    latest_ph = round(latest_ph, 1)

    
    latest_tds = df['Tds'].iloc[-1]
    latest_tds = round(latest_tds, 1)

    latest_ts = df['ts'].iloc[-1]
    latest_ts = datetime.fromisoformat(latest_ts[:-1])
    latest_ts = latest_ts.strftime('%d.%m.%Y')

    

    return latest_temp, latest_ph, latest_tds, latest_ts

@app.route('/')
def home():
    temp,ph,tds,ts = get_latest_data()
    return render_template('eng.html', temp=temp, pH=ph, tds=tds, ts=ts)

@app.route('/tempdetails')
def tempdetails():
    timestamps, temperatures = get_temperature_data()
    
    return render_template('tempgraph.html', timestamps=timestamps, temperatures=temperatures)


@app.route('/phdetails')
def phdetails():
    timestamps, ph = get_ph_data()
    
    return render_template('phgraph.html', timestamps=timestamps, ph=ph)


@app.route('/tdsdetails')
def tdsdetails():
    timestamps, tds = get_tds_data()
    
    return render_template('tdsgraph.html', timestamps=timestamps, tds=tds)

@app.route('/fi')
def fi():
    temp,ph,tds,ts = get_latest_data()
    
    return render_template('fin.html',temp=temp, pH=ph, tds=tds, ts=ts)

if __name__ == '__main__':
    app.run(debug=True)
