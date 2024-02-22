from flask import Flask, render_template, redirect, url_for, request
import Vokabeln
import json

app = Flask(__name__)


@app.route('/Bingo')
def hello_world():
    Stark = ["Stark!!", "Scheibe wird geklatscht", "Es lehnt zurück!!!", "Zieh doch, ich will Musklen sehen", "Herr Böge",
            "Kartbahn", "Schnee 👃", "Mathe Stäb", "Physik fertig, ab hier kommt Henle", "leut des müsst ihr wissen",
            "seil kann nur ziehen", "N/mm²", "Joker :)", "Ganz Sportlich", "Sicher",
            "Achtung!", "Starker Witz", "ist Klar oder", "Haug wird Aufgerufen", "Kurrios",
            "bis zum nächsten mal", "Erst mal überziehen", "kenned se", "Alte Firma", "Stahl"]
    # put application's code here
    return render_template("Bingo_Kacheln.html", Begriffe = json.dumps(Stark))

@app.route("/Vokabeln/<string:letters>/<int:len>")
def voc_abfragen(letters:str ,len:int):

    fehler = Vokabeln.check_parameters(len, letters)

    if fehler:
        return redirect(url_for("generate_voc", Fehler=fehler))

    return render_template("Voc_1.html", Vocabeln = json.dumps(Vokabeln.get_vocabulary(len, letters.upper())))

@app.route("/Vokabeln")
def generate_voc():

    return render_template("Voc_Home.html", Fehler = request.args.get("Fehler", False))

@app.route("/Vokabeln/get/<string:token>")
def get_voc(token):
    temp = token.split(":")
    return Vokabeln.Vocabeln.get(temp[0]).get(int(temp[1]))



if __name__ == '__main__':
    app.run(debug=True)
