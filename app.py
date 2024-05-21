from flask import Flask, render_template

app = Flask(_name_, static_url_path='/static')

@app.route('/')
def home():
    return render_template('joinnow.html')

if _name_ == '_main_':
    app.run(debug=True)