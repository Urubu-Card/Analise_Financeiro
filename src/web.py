from flask import Flask, render_template
import os
import data

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app =Flask(__name__,
            template_folder =os.path.join(BASE_DIR,"templates"),
            static_folder   =os.path.join(BASE_DIR,"static"))

@app.route("/")
def home():

    app = data.Busca()

    rank = app.RankSaldos()


    return render_template("index.html", rank_anual= {rank})

if __name__ == "__main__":
    app.run(debug=True)