from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Products page
@app.route('/products')
def products():
    return render_template('products.html')

# Thank you page
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

