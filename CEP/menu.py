
from cep import Cep,maps
from flask import Flask, render_template,request


app = Flask(__name__)

@app.route("/")
def menu():
    return render_template('index.html')

@app.route('/consulta',methods=["POST"])
def consulta():
    consulta_cep = request.form['digito']

    content = Cep(consulta_cep)
    ver = maps(consulta_cep)

    return render_template('index.html',final=content, ver_map=ver)

app.run(use_reloader=True)


"""
    html = []
    for i in content:
        html.append(f'{i} {content.get(i)} \n')
"""
    
