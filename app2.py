from flask import Flask, render_template, request
import math
from scipy.stats import norm
from "B&S Model" import black_scholes

app = Flask(__name__)

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return price

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        S = float(request.form['S'])
        K = float(request.form['K'])
        T = float(request.form['T'])
        r = float(request.form['r'])
        sigma = float(request.form['sigma'])
        option_type = request.form['option_type']

        price = black_scholes(S, K, T, r, sigma, option_type)
        return render_template('index.html', price=price)

    return render_template('index.html', price=None)

if __name__ == '__main__':
    app.run(debug=True)
