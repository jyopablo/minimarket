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
#_____________Pagina de bebidas_bebidas______________
@app.route('/bebidas', methods=['GET','POST'])
def bebidas_bebidas():
    global validar 
    bebidas=['Jugo nectar','Shangrila','Cocacola','Agua Saborizada','Sha Kala','Agua de Coco','Horchata Concentrada','Revive Blu','De la Granja','RapTor','Savilove']
    precios=['3.50','5.00','13.50','5.00','3.00','10.00','13.40','5.00','8.00','5.00','5.75']
    imgs=['18.jpg','24.jpg','25.jpg','42.jpg','80.jpg','102.jpg','125.jpg','136.jpg','144.jpg','152.jpg','188.jpg']
    try:
        if request.method=='POST':
            for i in range(0,11):
                producto_seleccionado=request.form.get("producto"+str(i))
                precio_producto=request.form.get("precio"+str(i))
                if producto_seleccionado != None and precio_producto != None:
                    break
            se_agrego_antes= producto_seleccionado in carrito
            if se_agrego_antes == False:
                carrito.append(producto_seleccionado)
                precio_carrito.append(precio_producto)
                validar=True
            else:
                return render_template('bebidas.html', lista_imgs=imgs, lista_bebidas=bebidas,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('bebias'))
        else:
            return render_template('bebidas.html', lista_imgs=imgs, lista_bebidas=bebidas,lista_precios=precios,validar=validar)
    except:
        return render_template('bebidas.html', lista_imgs=imgs, lista_bebidas=bebidas,lista_precios=precios,validar=validar)    

#_____________Pagina de abarrotes_______________
@app.route('/abarrotes', methods=['GET','POST'])
def abarrotes():
    global validar 
    abarrotes=['Incaparina','Pasta','Ablandador y Sasonador','Arroz','Harrina de Panqueques','Avena','Mayonesa','Alimento para Perro','Avena','8 Cereales','Azucar','Compota','Lentejas','Oregano','Miel','Huevos','Sal','Consome','Aceite Commestible','Manteca Vegetal','Salsa','Vinagre','Te','Frambuesas']
    precios=['8.20','7.50','7.00','6.05','10.50','12.00','9.40','300.00','12.50','12.50','6.00','3.50','11.95','7.95','15.00','28.00','7.00','12.75','14.00','12.00','10.50','15.00','13.00','15.00']
    imgs=['1.jpg','10.jpg','13.jpg','21.jpg','22.jpg','26.jpg','27.jpg','32.jpg','34.jpg','36.jpg','41.jpg','43.jpg','49.jpg','50.jpg','51.jpg','59.jpg','73.jpg','74.jpg','82.jpg','86.jpg','91.jpg','94.jpg','96.jpg','105.jpg']
    try:
        if request.method=='POST':
            for i in range(0,24):
                producto_seleccionado=request.form.get("producto"+str(i))
                precio_producto=request.form.get("precio"+str(i))
                if producto_seleccionado != None and precio_producto != None:
                    break
            se_agrego_antes= producto_seleccionado in carrito
            if se_agrego_antes == False:
                carrito.append(producto_seleccionado)
                precio_carrito.append(precio_producto)
                validar=True
            else:
                return render_template('abarrotes.html', lista_imgs=imgs, lista_abarrotes=abarrotes,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('abarrotes'))
        else:
            return render_template('abarrotes.html', lista_imgs=imgs, lista_abarrotes=abarrotes,lista_precios=precios,validar=validar)
    except:
        return render_template('abarrotes.html', lista_imgs=imgs, lista_abarrotes=abarrotes,lista_precios=precios,validar=validar)    



if __name__=='__main__':
    app.run(threaded=True,debug=True,port=8000)