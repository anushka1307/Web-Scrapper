from flask import Flask, render_template, request, jsonify
from flask_cors import cross_origin
from Scrapper import main


app = Flask(__name__)


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")


@app.route('/products', methods=['POST', 'GET'])  # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ", "")
            main(searchString)

            file = open('temp.txt', 'r')
            lines = file.readlines()
            reviews = []
            for line in lines:
                line = line.replace('â‚¹', '₹')
                name = line.split('\t')[0]
                offers = line.split('\t')[3]
                price = line.split('\t')[1]
                specification = line.split('\t')[2]
                mydict = {'Name': name, 'Price': price, 'Specification': specification, 'Offers': offers}
                reviews.append(mydict)
            return render_template('results.html', reviews=reviews[0:(len(reviews) - 1)])
        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'
    # return render_template('results.html')

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
