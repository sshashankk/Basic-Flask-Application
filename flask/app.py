from flask import Flask, redirect, url_for, render_template, request

#Instance of the flask application
app = Flask(__name__)

@app.route("/")
def books():  
    
    genre_category = request.form["genre"]

    url = f'http://openlibrary.org/subjects/{genre_category}.json?'

    published_range = str(2000-2010)
    ebooks_condition = str(True)

    parameters = {
            'published_in': '2000-2010',
            'details': 'True'
        }

    resp = requests.get(url, parameters)
    if (resp.status_code == 200):
        print("Everything was ok:", resp.status_code)
    else:
        print("There was a problem:", resp.status_code)
    
    title_list = []
    data = json.loads(resp.text)['works']
    print("Total number of books fetched: ",len(title))

    for book_title in range(1,len(data)):
      title_list.append(data[book_title]['title'])
    print(title_list)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)