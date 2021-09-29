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

#_____________Pagina de carrito Vacio _______________
@app.route('/carritovacio')
def carritovacio():
    global validar
    return render_template('carritovacio.html',validar=validar)

#_____________Pagina de carrito Vacio _______________
@app.route('/carritolleno')
def carritolleno():
    global validar
    tamaño=len(carrito)
    return render_template('carritolleno.html',validar=validar, tamaño=tamaño,carrito=carrito,precio_carrito=precio_carrito)    

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
    abarrotes=['Incaparina','Pasta','Ablandador y Sasonador','Arroz','Harrina de Panqueques','Avena','Mayonesa','Alimento para Perro','Avena','8 Cereales','Azucar','Compota','Lentejas','Oregano','Miel','Huevos','Sal','Consome','Aceite Commestible','Manteca Vegetal','Salsa','Vinagre','Te','Frambuesas','Cereal','Cafe Instantaneo','Salsa','Frijoles Volteados','Canela en Raja','Frijol','flan','Pasta','Cafe Instantaneo','Sopa Instantanea','Sopa Pollo y Fideos']
    precios=['8.20','7.50','7.00','6.05','10.50','12.00','9.40','300.00','12.50','12.50','6.00','3.50','11.95','7.95','15.00','28.00','7.00','12.75','14.00','12.00','10.50','15.00','13.00','15.00','18.00','21.00','15','7.00','7.00','9.25','6.00','7.50','30.50','4.70','3.70']
    imgs=['1.jpg','10.jpg','13.jpg','21.jpg','22.jpg','26.jpg','27.jpg','32.jpg','34.jpg','36.jpg','41.jpg','43.jpg','49.jpg','50.jpg','51.jpg','59.jpg','73.jpg','74.jpg','82.jpg','86.jpg','91.jpg','94.jpg','96.jpg','105.jpg','106.jpg','107.jpg','110.jpg','115.jpg','123.jpg','126.jpg','150.jpg','161.jpg','163.jpg','174.jpg','189.jpg',]
    try:
        if request.method=='POST':
            for i in range(0,35):
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

#_____________Pagina de botanas_______________
@app.route('/botanas', methods=['GET','POST'])
def botanas():
    global validar 
    botanas=['Papa','Palomitas','Frituras de Maiz','Cacahuates','Botanas Saldas','Barras Nutriticas','Nueces y Semillas']
    precios=['8.00','2.00','5.00','20.95','7.20','16.90','16.00']
    imgs=['90.jpg','167.jpg','17.jpg','120.jpg','84.jpg','53.jpg','146.jpg']
    try:
        if request.method=='POST':
            for i in range(0,7):
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
                return render_template('botanas.html', lista_imgs=imgs, lista_botanas=botanas,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('botanas'))
        else:
            return render_template('botanas.html', lista_imgs=imgs, lista_botanas=botanas,lista_precios=precios,validar=validar)
    except:
        return render_template('botanas.html', lista_imgs=imgs, lista_botanas=botanas,lista_precios=precios,validar=validar) 

#_____________Pagina de confiteria_______________
@app.route('/confiteria', methods=['GET','POST'])
def confiteria():
    global validar 
    confiteria=['Caramelos','Chocolate de Mesa','Chocolate en Polvo','Chocolate','Gomas de Mascar']
    precios=['10.00','17.00','10.00','10.85','14.85']
    imgs=['9.jpg','165.jpg','151.jpg','130.jpg','195.jpg']
    try:
        if request.method=='POST':
            for i in range(0,5):
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
                return render_template('confiteria.html', lista_imgs=imgs, lista_confiteria=confiteria,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('confiteria'))
        else:
            return render_template('confiteria.html', lista_imgs=imgs, lista_confiteria=confiteria,lista_precios=precios,validar=validar)
    except:
        return render_template('confiteria.html', lista_imgs=imgs, lista_confiteria=confiteria,lista_precios=precios,validar=validar) 

#_____________Pagina de enlataados_______________
@app.route('/enlatados', methods=['GET','POST'])
def enlatados():
    global validar 
    enlatados=['Aceitunas','Champiñones','Chicharos con Zanahoraia','Chicharos','Frijoles Volteados','Frutas en Almibar','Sardinas','Atun en Agua/Aceite','Chiles Enlatados','Granos de Elote','Sopa']
    precios=['9.75','17.40','9.85','8.35','17.95','22.00','11.00','12.00','5.50','7.45','13.55']
    imgs=['72.jpg','160.jpg','58.jpg','145.jpg','124.jpg','178.jpg','47.jpg','154.jpg','44.jpg','48.jpg','88.jpg']
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
                return render_template('enlatados.html', lista_imgs=imgs, lista_enlatados=enlatados,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('enlatados'))
        else:
            return render_template('enlatados.html', lista_imgs=imgs, lista_enlatados=enlatados,lista_precios=precios,validar=validar)
    except:
        return render_template('enlatados.html', lista_imgs=imgs, lista_enlatados=enlatados,lista_precios=precios,validar=validar)         

#_____________Pagina de lacteos_______________
@app.route('/lacteos', methods=['GET','POST'])
def lacteos():
    global validar 
    lacteos=['Leche Condensada','Leche Deslactosada','Leche en Polvo','Leche Evaporada','Leche Light','Leche Pasteurizada','Leche Saborizada','Leche Semidescremada','Crema en Vaso','Yoghurt','Margarina','Queso Rodaja','Queso Duro','Queso Capas','Queso Mozarella','Queso Crema']
    precios=['5.65','15.15','30.00','15.25','14.00','10.00','4.50','10.00','9.00','5.00','7.00','15.00','14.00','23.00','29.00','15.00']
    imgs=['54.jpg','116.jpg','2.jpg','176.jpg','33.jpg','100.jpg','80.jpg','175.jpg','77.jpg','19.jpg','20.jpg','156.jpg','4.jpg','78.jpg','6.jpg','7.jpg']
    try:
        if request.method=='POST':
            for i in range(0,16):
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
                return render_template('lacteos.html', lista_imgs=imgs, lista_lacteos=lacteos,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('lacteos'))
        else:
            return render_template('lacteos.html', lista_imgs=imgs, lista_lacteos=lacteos,lista_precios=precios,validar=validar)
    except:
        return render_template('lacteos.html', lista_imgs=imgs, lista_lacteos=lacteos,lista_precios=precios,validar=validar) 

#_____________Pagina de harinas_______________
@app.route('/harinas', methods=['GET','POST'])
def harinas():
    global validar 
    harinas=['Tortillas de Maiz','Galletas Dulces','Galletas Saldas','Pastelillos','Pan de Caja','Pan Molido','Pan Tostado','Sandwich']
    precios=['13.00','10.20','7.20','5.30','12.50','12.40','18.85','17.55']
    imgs=['69.jpg','12.jpg','139.jpg','66.jpg','5.jpg','67.jpg','127.jpg','186.jpg']
    try:
        if request.method=='POST':
            for i in range(0,8):
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
                return render_template('harinas.html', lista_imgs=imgs, lista_harinas=harinas,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('harinas'))
        else:
            return render_template('harinas.html', lista_imgs=imgs, lista_harinas=harinas,lista_precios=precios,validar=validar)
    except:
        return render_template('harinas.html', lista_imgs=imgs, lista_harinas=harinas,lista_precios=precios,validar=validar) 

#_____________Pagina de Frutas y Verduras_______________
@app.route('/frutasyverduras', methods=['GET','POST'])
def frutasyverduras():
    global validar 
    frutasyverduras=['Aguacates','Ajos','Cebollas','Chiles','Cilantro/Perejil','Jitomate','Papas','Limones','Manzanas','Naranjas','Platanos']
    precios=['13.20','4.90','5.70','8.95','9.50','6.50','7.15','18.50','12.30','17.25','11.00']
    imgs=['65.jpg','87.jpg','63.jpg','60.jpg','61.jpg','173.jpg','90.jpg','76.jpg','70.jpg','85.jpg','62.jpg']
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
                return render_template('frutasyverduras.html', lista_imgs=imgs, lista_frutasyverduras=frutasyverduras,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('frutasyverduras'))
        else:
            return render_template('frutasyverduras.html', lista_imgs=imgs, lista_frutasyverduras=frutasyverduras,lista_precios=precios,validar=validar)
    except:
        return render_template('frutasyverduras.html', lista_imgs=imgs, lista_frutasyverduras=frutasyverduras,lista_precios=precios,validar=validar) 

#_____________Pagina de Preparados_______________
@app.route('/preparados', methods=['GET','POST'])
def preparados():
    global validar 
    preparados=['Pasta','Sopa en Vaso','Carnes','Salchicha','Mortadela','Tocino','Jamon','Manteca','Chorizo']
    precios=['3.45','4.50','21.50','25.00','15.00','20.00','7.80','20.00','21.50']
    imgs=['10.jpg','174.jpg','109.jpg','57.jpg','172.jpg','128.jpg','81.jpg','86.jpg','138.jpg','114.jpg']
    try:
        if request.method=='POST':
            for i in range(0,9):
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
                return render_template('preparados.html', lista_imgs=imgs, lista_preparados=preparados,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('preparados'))
        else:
            return render_template('preparados.html', lista_imgs=imgs, lista_preparados=preparados,lista_precios=precios,validar=validar)
    except:
        return render_template('preparados.html', lista_imgs=imgs, lista_preparados=preparados,lista_precios=precios,validar=validar) 

#_____________Pagina de Medicina_______________
@app.route('/medicina', methods=['GET','POST'])
def medicina():
    global validar 
    medicina=['Suero','Preservativos','Alcohol','Gasas','Analgesicos','Antigripales','Antiacidos','Curitas','Agua Oxigenada','Gel','Algodon','Pañales Adulto','Acetaminofen','Cofal','Aspirina','Dorival','Pañales','Pomada La Campana','Alka Seltzer','Vitaflenaco','Bicarbonato','Vitapyrena','Pepto Bismol','Tabcin','Salandrews','Loratadina','Neumonil','Vick VapoRub']
    precios=['16.00','8.00','9.75','5.00','15.75','28.00','24.75','10.50','11.50','5.00','11.00','240.00','11.00','25.00','14.75','29.00','20.00','14.50','19.00','19.00','15.00','15.00','33.50','24.00','11.00','59.00','17.50','24.50']
    imgs=['194.jpg','103.jpg','55.jpg','113.jpg','185.jpg','104.jpg','45.jpg','38.jpg','56.jpg','137.jpg','46.jpg','179.jpg','133.jpg','40.jpg','157.jpg','39.jpg','129.jpg','149.jpg','183.jpg','92.jpg','79.jpg','11.jpg','184.jpg','190.jpg','182.jpg','95.jpg','148.jpg','155.jpg']
    try:
        if request.method=='POST':
            for i in range(0,28):
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
                return render_template('medicina.html', lista_imgs=imgs, lista_medicina=medicina,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('medicina'))
        else:
            return render_template('medicina.html', lista_imgs=imgs, lista_medicina=medicina,lista_precios=precios,validar=validar)
    except:
        return render_template('medicina.html', lista_imgs=imgs, lista_medicina=medicina,lista_precios=precios,validar=validar) 

#_____________Pagina de Higiene Personal _______________
@app.route('/higienepersonal', methods=['GET','POST'])
def higienepersonal():
    global validar 
    higienepersonal=['Toallas Húmedas','Aceite para Bebe','Toallas Femenidas','Tinte para Cabello','Biberonres','Talco','Cepillo de Dientes','Shampo','Hisopos','Rasuradoras','Crema Corporal','Papel Higenico','Crema para Afeitar','Pasta Dental','Desodorante','Enjuague Bucal','Lubricante para Labios']
    precios=['10.00','27.00','22.00','49.00','15.00','27.00','10.00','25.00','5.00','8.70','27.00','23.75','22.00','20.00','22.00','40.00','15.00']
    imgs=['30.jpg','101.jpg','97.jpg','147.jpg','111.jpg','37.jpg','112.jpg','75.jpg','192.jpg','131.jpg','117.jpg','171.jpg','108.jpg','181.jpg','159.jpg','141.jpg','169.jpg']
    try:
        if request.method=='POST':
            for i in range(0,17):
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
                return render_template('higienepersonal.html', lista_imgs=imgs, lista_higienepersonal=higienepersonal,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('higienepersonal'))
        else:
            return render_template('higienepersonal.html', lista_imgs=imgs, lista_higienepersonal=higienepersonal,lista_precios=precios,validar=validar)
    except:
        return render_template('higienepersonal.html', lista_imgs=imgs, lista_higienepersonal=higienepersonal,lista_precios=precios,validar=validar) 


#_____________Pagina de Uso Domestico _______________
@app.route('/usodomestico', methods=['GET','POST'])
def usodomestico():
    global validar 
    usodomestico=['Baterias','Shampo para Ropa','Servilletas','Aromatizante','Cera para Automovil','Cera para Calzado','Pastillas Sanitarias','Limpiador para pizo','Jabon de Bola','Cerillos','Cloro galon','Cloro litro','Jabon en Barra','Insectizidas','Fibras Limpiadoras','Desinfectantes','Detergente para Trastes','Detergente Suavitel']
    precios=['15.75','13.00','5.15','18.00','44.50','6.75','50.00','67.90','12.75','19.50','10.00','16.00','20.75','6.25','15.00','15.00','17.50','12.00']
    imgs=['98.jpg','89.jpg','99.jpg','197.jpg','198.jpg','121.jpg','29.jpg','31.jpg','93.jpg','164.jpg','166.jpg','3.jpg','83.jpg','143.jpg','28.jpg','193.jpg','158.jpg','89.jpg']
    try:
        if request.method=='POST':
            for i in range(0,18):
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
                return render_template('usodomestico.html', lista_imgs=imgs, lista_usodomestico=usodomestico,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('usodomestico'))
        else:
            return render_template('usodomestico.html', lista_imgs=imgs, lista_usodomestico=usodomestico,lista_precios=precios,validar=validar)
    except:
        return render_template('usodomestico.html', lista_imgs=imgs, lista_usodomestico=usodomestico,lista_precios=precios,validar=validar) 

#_____________Pagina de Otros _______________
@app.route('/otros', methods=['GET','POST'])
def otros():
    global validar 
    otros=['Tarjeta Telefonicas','Hielo']
    precios=['15.00','11.95']
    imgs=['180.jpg','71.jpg']
    try:
        if request.method=='POST':
            for i in range(0,2):
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
                return render_template('otros.html', lista_imgs=imgs, lista_otros=otros,lista_precios=precios,validar=validar,se_agrego_antes=se_agrego_antes)
            print(carrito)    
            return redirect(url_for('otros'))
        else:
            return render_template('otros.html', lista_imgs=imgs, lista_otros=otros,lista_precios=precios,validar=validar)
    except:
        return render_template('otros.html', lista_imgs=imgs, lista_otros=otros,lista_precios=precios,validar=validar) 

        



if __name__=='__main__':
    app.run(threaded=True,debug=True,port=8000)