from flask import Flask
from flask import render_template

app = Flask(__name__)
#_____________Pagina Index.html_______________
@app.route('/')
def index():
    return render_template('index.html')
#_____________Pagina de bebidas_frias______________
@app.route('/bebidas_frias')
def bebidas_frias():
    return render_template('bebidas_frias.html')




if __name__=='__main__':
    app.run(threaded=True,debug=True,port=8000)