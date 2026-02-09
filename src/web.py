from flask import Flask, render_template
import os
import data
import webbrowser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app =Flask(__name__,
            template_folder =os.path.join(BASE_DIR,"templates"),
            static_folder   =os.path.join(BASE_DIR,"static"))

@app.route("/")
def home():

    app = data.Busca()

    rank = app.RankSaldos()

    tabela , nao_usar = app.Tabela()

    return render_template("index.html", rank_anual= rank , tabela = tabela)


if __name__ == "__main__":
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open("http://127.0.0.1:5000")

    app.run(debug=True)