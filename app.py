from flask import Flask
from flask import render_template

app = Flask(__name__)

def TotalCost(height, radius):
    pi = 3.14
    areaTankTop = pi*(radius**2)
    areaTankSide = 2*pi*(radius*height)
    areaTotal = areaTankTop + areaTankSide
    areaSqFt = areaTotal/144
    materialCostTotal = areaSqFt*25
    laborCostTotal = areaSqFt*15
    TotalCostEst = materialCostTotal + laborCostTotal
    return TotalCostEst



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html')

@app.route('/estimate', methods=['POST'])
def add_inputs():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])

        tankCost = TotalCost(height, radius)
        
        return render_template('estimate.html', pageTitle='Estimate', estimate=Cost)
    return render_template('estimate.html', pageTitle='estimate')

if __name__ == '__main__':
    app.run(debug=False)