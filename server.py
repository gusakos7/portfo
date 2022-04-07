import csv
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


def write_to_text(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    with open('database.txt', 'a') as file:
        file.write(f"{email}, {subject}, {message}\n")


def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']

    with open('database.csv', 'a') as file:
        csv_writer = csv.writer(file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/")
@app.route("/index.html")
def homepage():
    return render_template('index.html')


@app.route("/<string:page_name>")
def works(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()

        write_to_csv(data)
        return redirect('/thank_you.html')
    else:
        return 'something went wrong'
