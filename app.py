from flask import Flask
from flask import render_template,request

carrito=[]

app = Flask(__name__)
#_____________Pagina Index.html_______________
@app.route('/')
def index():
    return render_template('index.html')
#_____________Pagina de bebidas_frias______________
@app.route('/bebidas_frias')
def bebidas_frias(): 
    frias=['Te frio','Cocacola','Pepsi','Cerveza']
    precios=['34.50','15.01','20.40','30.10']
    return render_template('bebidas_frias.html', lista_bebidas_frias=frias,lista_precios=precios)



if __name__=='__main__':
    app.run(threaded=True,debug=True,port=8000)