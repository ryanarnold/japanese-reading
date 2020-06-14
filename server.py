from flask import Flask
from flask import render_template
from utils import retrieve_content_list

app = Flask(__name__)

@app.route('/')
def index():
    short_stories = retrieve_content_list('stories')
    return render_template('index.html', short_stories=short_stories)


@app.route('/content/<subdir>/<content_id>')
def latest_log_file(subdir=None, content_id=None):
    content = ''

    with open('static\\content\\' + subdir + '\\' + content_id + '.txt', 'r', encoding='utf-8') as c:
        content = c.read()

    content = content.replace('\n', '<br>')
    print(content)
    
    return render_template('content.html', content_title=content_id, content=content)
