from flask import redirect, render_template, Flask, session
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "Secret key for flask app."

texts = json.loads(open('texts.json', 'r').read())

@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.ico')

@app.route('/static/<file>')
def sendfile(file):
    return app.send_static_file(file)

@app.route("/changelang/<lang>")
def changelang(lang):
    session['lang'] = lang
    return redirect('/')

@app.route('/')
def index():
    lang = session.get('lang')

    text1 = texts[lang]['text1']
    text2 = texts[lang]['text2']
    text3 = texts[lang]['text3']
    help = texts[lang]['help']
    ruschat = texts[lang]['ruschat']
    engchat = texts[lang]['engchat']
    text4 = texts[lang]['text4']
    text5 = texts[lang]['text5']
    github = texts[lang]['github']
    install = texts[lang]['install']

    return render_template('index.html', text1=text1, text2=text2, 
                            text3=text3, help=help,
                            ruschat=ruschat, engchat=engchat,
                            text4=text4, text5=text5, github=github, install=install)

@app.route('/install')
def install():
    lang = session.get('lang')
    
    title = texts[lang]['title']
    default = texts[lang]['default']
    installed1 = texts[lang]['installed1']
    installed2 = texts[lang]['installed2']

    return render_template('install.html', title=title, default=default,
                            installed1=installed1, installed2=installed2)
if __name__ == "__main__":
    app.run(debug=True)
