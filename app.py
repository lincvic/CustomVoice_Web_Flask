from flask import Flask, render_template, request
from custom_voice_Util import creatRequest, ssmlBuilder

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/trans_voice', methods=['POST', 'GET'])
def trans_voice():
    voiceText = request.form['voice']
    print(voiceText)
    ssml = ssmlBuilder('zh-CN', 'wangyijiang1', voiceText)

    creatRequest(ssml)
    return render_template("result.html")


if __name__ == '__main__':
    app.run()
