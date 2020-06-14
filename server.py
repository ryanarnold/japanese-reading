from flask import Flask
from flask import render_template
from flask import request
from utils import retrieve_content_list
import re

app = Flask(__name__)

@app.route('/')
def index():
    short_stories = retrieve_content_list('stories')
    news_articles = retrieve_content_list('news')
    light_novels = retrieve_content_list('ln')
    return render_template('index.html', short_stories=short_stories, news_articles=news_articles, light_novels=light_novels)


@app.route('/content/<subdir>/<content_id>')
def latest_log_file(subdir=None, content_id=None):
    content = ''

    with open('static\\content\\' + subdir + '\\' + content_id + '.txt', 'r', encoding='utf-8') as c:
        content = c.read()

    content = content.replace('\n', '<br>')
    print(content)
    
    return render_template('content.html', content_title=content_id, content=content)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        content_title = request.form['title']
        content_type = request.form['type']
        content = request.form['content']

        with open('static\\content\\' + content_type + '\\' + content_title + '.txt', 'w', encoding='utf-8') as c:
            c.write(content)

    return render_template('upload.html')
