import base64
import string
from io import BytesIO

from barcode import Code39
from barcode.writer import ImageWriter


#Genera un codigo de barras de tipo "code39", content es un string del cual se genera el código (normalmente el id de una herramienta)
#Si se provee un "filename", la imagen se guardará en donde se encuentre el proyecto.
#Devuelve la imagen generada como base64 para que pueda ser vista en el navegador sin que haga falta guardarla antes.
def code39(content:string,filename:string=None):
    file = BytesIO()
    code = Code39(content,ImageWriter(),False)
    code.write(file)
    if filename!=None:
        code.save(filename)
    #print(base64.b64encode(file.getvalue()))
    return (base64.b64encode(file.getvalue()))