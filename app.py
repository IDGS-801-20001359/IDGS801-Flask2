from flask import Flask, render_template
from flask import request
#referencias nuevas para las cookies
from flask import make_response
from flask import flash
from flask_wtf import CSRFProtect


import forms
app=Flask(__name__)

app.config['SECRET_KEY']="esta es tu clave encriptada"
csrf=CSRFProtect()

@app.route("/calcular",methods=["GET"])
def calcular():
    return render_template("calcular.html")

@app.route("/cookie",methods=['GET','POST'])
def cookie():
    reg_user=forms.LoginForm(request.form) #instanciamos clase formulario
    
    if request.method=='POST' and reg_user.validate():
        user=reg_user.username.data
        pasw=reg_user.password.data
        datos=user+"@"+pasw
        success_message='Bienvenido {}'.format(user)#estructura del mensaje
        response.set_cookie('datos_user',datos) #creas cookie
        flash(success_message)
    response=make_response(render_template('cookie.html',form=reg_user)) #pasamos estructura del formualrio ala vista
        #print(user+' '+pasw)
    return response


@app.route("/Alumnos",methods=["GET","POST"])
def alumnos():
    reg_alum=forms.UserForm(request.form)
    mat=''
    nom=''
    if request.method == 'POST' and reg_alum.validate():
        mat=reg_alum.matricula.data
        nom=reg_alum.nombre.data
    return render_template('Alumnos.html',form=reg_alum,mat=mat,nom=nom)

#actividad de traductor
@app.route('/traductor', methods=['GET', 'POST'])
def traductor():
    words = forms.WordsForm(request.form)
    datosEncontrados = ''
    if(request.method == 'POST' and words.validate()):
        btnGuardar = request.form.get('btnGuardar')
        btnTraducir = request.form.get('btnTraducir')
        if(btnGuardar == 'Guardar'):    
            file = open('palabras.txt', 'a')
            file.write('\n' + words.español.data.upper() + '\n' + words.ingles.data.upper())
            file.close()
        if(btnTraducir == 'Traducir'):
            opcion = request.form.get('translate')
            file = open('palabras.txt', 'r')
            palabras = [linea.rstrip('\n') for linea in file]
            if(opcion == 'español'):
                espPalabra = request.form.get('txtEspañol')
                for posicion in range(len(palabras)):
                    if(palabras[posicion] == espPalabra.upper()):
                        datosEncontrados = palabras[posicion + 1]
            elif(opcion == 'ingles'):
                engPalabra = request.form.get('txtIngles')
                for posicion in range(len(palabras)):
                    if(palabras[posicion] == engPalabra.upper()):
                        datosEncontrados = palabras[posicion - 1]
                        print(datosEncontrados)

    return render_template('traductor.html', form = words, datosEncontrados = datosEncontrados)


#este es parte de mi codigo de la actividad cajas 
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
    #csrf.init_app(app)
    app.run(debug=True,port=3000)






