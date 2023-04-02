from flask import Flask, render_template, request
import wikipedia

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html ')


@app.route('/responder', methods=['POST'])
def responder():
    pergunta = request.form['pergunta']
    wikipedia.set_lang("pt")
    resposta = wikipedia.summary(pergunta, sentences=1)
    return resposta

if __name__ == '__main__':
    app.run(debug=True)