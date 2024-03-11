from flask import Flask, render_template, redirect, url_for, request

import Bingo
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


@app.route("/Bingo/<string:subject>")
def Bingo_redir(subject):
    if subject == "":
        return 404
    print(Bingo.create_random_Bingo_token(subject,4**2))
    redirect(f"/Bingo/{subject}/{Bingo.create_random_Bingo_token(subject,4**2)}")

@app.route("/Bingo/<string:subject>/<string:token>")
def Bingo_game(subject,token):
    if token == "" or subject == "":
        return 404

    render_template("Bingo.html", Card = json.dumps(Bingo.load_Bingo()))

@app.route("/Bingo_generate/<string:token>")
def bingo_kacheln(subject, size):
    if subject == "":
        return 404
    if size == 0 or size == None:
        return 404

    return json.dumps(Bingo.create_random_Bingo_field(subject,size))


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
