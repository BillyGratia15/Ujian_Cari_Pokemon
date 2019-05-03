# Soal 3
# UJIAN_CARI_POKEMON    

from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return render_template('1home.html')

@app.route('/hasil', methods = ['GET', 'POST'])
def hasil():
    namapoke = request.form['nama']
    url = 'https://pokeapi.co/api/v2/pokemon/'
    datapoke1 = requests.get(url+namapoke)
    pokedex = 'https://pokeapi.co/api/v2/pokedex/1/'
    datapoke2 = requests.get(pokedex)
    for i in range(len(datapoke2.json()['pokemon_entries'])):
        if namapoke == datapoke2.json()['pokemon_entries'][i]['pokemon_species']['name']:
            return render_template('1hasil.html', datapoke1 = datapoke1)
    else:
        return render_template('1error.html')

@app.errorhandler(404)
def notFound(error):            
    return render_template('1error.html')

if __name__ == '__main__':
    app.run(debug = True)