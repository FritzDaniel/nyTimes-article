import requests
from flask import Flask, render_template

app = Flask(__name__)

apiKey = "JLBtTAFcRJRKAnMSnQ4Ds653FphWu2on"

@app.route("/")
def home():
    req = requests.get('https://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=' + apiKey)
    if not req.content:
        return None
    return render_template('articles.html', data=req.json())


@app.route("/articleDetail/<article_index>")
def articleDetail(article_index):
    req = requests.get('https://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key=' + apiKey)
    if not req.content:
        return None
    json = req.json()
    if len(json['results'][int(article_index)-1]['media']) > 0:
        data = {
            "title": json['results'][int(article_index) - 1]['title'],
            "published_date": json['results'][int(article_index) - 1]['published_date'],
            "byline": json['results'][int(article_index) - 1]['byline'],
            "abstract": json['results'][int(article_index) - 1]['abstract'],
            "img_url": json['results'][int(article_index) - 1]['media'][0]['media-metadata'][2]['url'],
            "url": json['results'][int(article_index) - 1]['url']
        }
    elif len(json['results'][int(article_index)-1]['media']) == 0:
        data = {
            "title": json['results'][int(article_index) - 1]['title'],
            "published_date": json['results'][int(article_index) - 1]['published_date'],
            "byline": json['results'][int(article_index) - 1]['byline'],
            "abstract": json['results'][int(article_index) - 1]['abstract'],
            "img_url": "",
            "url": json['results'][int(article_index) - 1]['url']
        }
    return render_template('detail.html', data=data)


if __name__ == "__main__":
    app.run()