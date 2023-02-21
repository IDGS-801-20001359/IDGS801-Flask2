from flask import Flask, render_template
from flask import request


import forms

app=Flask(__name__)

@app.route("/calcular",methods=["GET"])
def calcular():
    return render_template("calcular.html")

@app.route("/Alumnos",methods=["GET","POST"])
def alumnos():
    reg_alum=forms.UserForm(request.form)
    mat=''
    nom=''
    if request.method == 'POST':
        mat=reg_alum.matricula.data
        nom=reg_alum.nombre.data
    return render_template('Alumnos.html',form=reg_alum,mat=mat,nom=nom)

@app.route('/')
def formulario():
    return render_template('cajasDinamicas.html')
           
@app.route("/Caja", methods = ['GET', 'POST'])
def caja():
    if request.method == 'POST':
        campoN = int(request.form.get('txtCampoN'))
        return render_template('AnalisisDeCajas.html', campoN = campoN)

@app.route("/cajasDinamicas",methods=["POST"])
def cajas():
    numeroString = request.form.getlist('txtNumber')
    numeroInt = list(map(int, numeroString))

    maximo = int(numeroInt[0])
    for a in numeroInt:
        if int(maximo) > int(a):
            maximo = maximo
        else:
            maximo=a
   
    menor = int(numeroInt[0])
    for m in numeroInt:
        if int(menor) < int(m):
            menor = menor
        else:
            menor=m

    calculo = sum(numeroInt) / len(numeroInt)

    results = []
    for number in numeroInt:
        resultado = numeroInt.count(number)
        results.append("{} aparece {} veces".format(number, resultado))

    return render_template('resultado.html', maximo = maximo, menor = menor, calculo = calculo, results = results)


if __name__ == "__main__":
    app.run(debug=True,port=3000)






