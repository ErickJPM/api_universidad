import web
import app
import json
import csv
render = web.template.render('application/views/')

class Alumnos:
    def GET(self):
        try:
            datos=web.input()
            if datos['token']=="1234":
                result=[]
                result2={}
                if datos['action']=="get":
                    with open('static/csv/alumnos.csv','r') as csvfile:#a+ es de append,r es de read as csvfile= una variable cualquiera
                        reader = csv.DictReader(csvfile)
                        for row in reader:
                            result.append(row)
                            result2['status']="200 ok"
                            result2['alumnos']=result
                    return json.dumps(result2) 
                else:
                    result2={}
                    result2['status']="Command not found"
                    return json.dumps(result2)
            else:
                result={}
                result['status']="datos incorrectos"
                return json.dumps(result)
        except Exception as e:
            result={}
            result['status']="Faltan valores"
            return json.dumps(result)
            
            

