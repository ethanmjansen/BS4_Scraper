from flask import Flask, render_template, request
from scraper_functions import Article_Summary

# news_article = 'https://www.npr.org/2020/03/26/819126947/white-house-works-on-new-coronavirus-guidelines-to-classify-counties-by-risk'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST']) #allow both GET and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        url = request.form.get('url')
        ratio = float(request.form['ratio'])

        return Article_Summary(url, ratio)

    return '''<form method="POST">
                  URL: <input type="text" name="url"><br>
                  Ratio: <input type="text" name="ratio"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''


if __name__ == "__main__":
    app.run()