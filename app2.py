from flask import Flask, render_template, request
print("1. Import Flask OK")

from black_scholes import black_scholes
print("2. Import black_scholes OK")  # Ajoute cette ligne

app = Flask(__name__)
print("3. Flask app created OK")

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
    app.run(debug=True, host='0.0.0.0', port=5001)

