from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        csv_file = request.files['upload_file']
        # Read the CSV file and return the data to fill out the table
        # Example below:
        # return render_template('index.html', items=[{'name': 'JS', 'contact': '+27', 'country': 'South Africa'}])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
