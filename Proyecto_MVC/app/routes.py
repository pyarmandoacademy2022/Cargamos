from flask import render_template, request,redirect
#todo importando la aplicacion y la conexion a la base de datos
from app import app,db
#todo importando el modelo = tabla
from app.models import Grupos

@app.route('/')
def index():
    #todo el objeto grupo almacena todos los registros de la tabla
    #todo select * from grupos
    gps= Grupos.query.all()
    template_name="index.html"
    return render_template(template_name,grupos=gps)


@app.route('/agregar' ,methods=['POST'])
def agregar():
    if request.method == "POST":
        #todo recogiendo los varlores del formulario
        form=request.form
        nombre_grupo=form.get("grupo")
        estado=form.get("estado")
        if not nombre_grupo or estado:
            #todo se agregan los datos del formulario a la clase
            grupos=Grupos(nombre_grupo=nombre_grupo,estado=estado)
            #todo se agrega a la tabla de mysql
            db.session.add(grupos)
            #todo commit insertar los valores a la tabla
            db.session.commit()
            #todo recarga la pagina con los nuevos valores =F5
            return redirect('/')
        return "termino la grabacion"
            
            
        
        
        


    


