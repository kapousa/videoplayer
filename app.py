from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/<vid_id>/videosshow')
def videosshow(vid_id):  # put application's code here
    return render_template('videosshow.html', vid_id=vid_id)


if __name__ == '__main__':
    app.run()
