from flask import Flask
from flask import render_template,request
from werkzeug.utils import redirect
validar=False
carrito=[]
precio_carrito=[]


app = Flask(__name__)
#_____________Pagina Index.html_______________
@app.route('/')
def index():
    global validar
    return render_template('index.html',validar=validar)
#_____________Pagina de bebidas_frias______________
@app.route('/bebidas_frias', methods=['GET','POST'])
def bebidas_frias():
    global validar 
    frias=['Te frio','Cocacola','Pepsi','Cerveza']
    precios=['34.50','15.01','20.40','30.10']
    try:
        if request.method=="POST":
            for i in range(0,4):
                producto_seleccionado=request.form.get("producto"+str(i))
                precio_producto=request.form.get("precio"+str(i))
                if producto_seleccionado != None and precio_producto != None:
                    break
            carrito.append(producto_seleccionado)
            precio_carrito.append(precio_producto)
            validar=True
            return redirect(url_for('bebias_frias'))
        else:
            return render_template('bebidas_frias.html', lista_bebidas_frias=frias,lista_precios=precios,validar=validar)
    except:
        return render_template('bebidas_frias.html', lista_bebidas_frias=frias,lista_precios=precios,validar=validar)    



if __name__=='__main__':
    app.run(threaded=True,debug=True,port=8000)