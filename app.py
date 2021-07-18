from flask import Flask
from flask import render_template,request
from werkzeug.utils import redirect

carrito=[]

app = Flask(__name__)
#_____________Pagina Index.html_______________
@app.route('/')
def index():
    return render_template('index.html')
#_____________Pagina de bebidas_frias______________
@app.route('/bebidas_frias', methods=['GET','POST'])
def bebidas_frias(): 
    frias=['Te frio','Cocacola','Pepsi','Cerveza']
    precios=['34.50','15.01','20.40','30.10']
    try:
        if request.method=="POST":
            producto_seleccionado=request.form.get("producto0")
            precio_producto=request.form.get("precio0")
            print(producto_seleccionado)
            print(precio_producto)
            return redirect(url_for('bebias_frias'))
        else:
            return render_template('bebidas_frias.html', lista_bebidas_frias=frias,lista_precios=precios)
    except:
        return render_template('bebidas_frias.html', lista_bebidas_frias=frias,lista_precios=precios)    



if __name__=='__main__':
    app.run(threaded=True,debug=True,port=8000)