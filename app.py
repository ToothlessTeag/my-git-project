from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for the "About Tigers" page
@app.route('/about_tigers')
def about_tigers():
    return render_template('about_tigers.html')

if __name__ == '__main__':
    app.run(debug=True)
