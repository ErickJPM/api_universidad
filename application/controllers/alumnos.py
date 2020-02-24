import web
import app
import json
import csv


class Alumnos:
    file="/static/csv/alumnos.csv"
    app_version="0.1.0"
    def __init__(self):
        pass

    def GET(self):
        try:
            datos=web.input()
            if datos['token']=="1234":
                if datos['action']=="get":
                    result2=self.optionget(self.app_version,self.file)
                    return json.dumps(result2)
                elif datos['action']=="search":
                    matricula=datos['matricula']
                    result2=self.optionsearch(self.app_version,self.file,matricula)
                    return json.dumps(result2)
                elif datos['action']=="help":
                    help=datos['action']
                    result=self.optionhelp(self.app_version,self.file,help)
                    return json.dumps(result)
                else:
                    result2={}
                    result2['status']="Command not found"
                    result2['help']="Para ayuda escribe ?token=xxxx&action=help"
                    return json.dumps(result2)
            else:
                result={}
                result['status']="Token incorrecto"
                return json.dumps(result)
        except Exception as e:
            result={}
            result['status']="Faltan valores"
            result['help']="Para ayuda escribe ?token=xxxx&action=help"
            return json.dumps(result)

    @staticmethod
    def optionget(app_version,file):
        try:
                result=[]
                result2={}
                with open('static/csv/alumnos.csv','r') as csvfile:#a+ es de append,r es de read as csvfile= una variable cualquiera
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        result.append(row)
                        result2['app_version']=app_version
                        result2['status']="200 ok"
                        result2['alumnos']=result
                return result2 
        except Exception as e:
            result={}
            result['version']=app_version
            result['status']="ErrorG"
            return json.dumps(result)
    @staticmethod
    def optionsearch(app_version,file,matricula):
        try:
                result=[]
                result2={}
                with open('static/csv/alumnos.csv','r') as csvfile:#a+ es de append,r es de read as csvfile= una variable cualquiera
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        if(matricula==row['matricula']):
                            print(matricula)
                            result.append(row)
                            result2['app_version']=app_version
                            result2['status']="200 ok"
                            result2['alumnos']=result
                            break
                        else:
                            result2={}
                            result2['status']="matricula no encontrada"
                return result2 
        except Exception as e:
            result={}
            result['version']=app_version
            result['status']="ErrorS"
            return json.dumps(result)
    @staticmethod
    def optionhelp(app_version,file,help):
        result={}
        result['version']=app_version
        result['status']="200 ok"
        result['get']='?token=xxxx&action=get'
        result['search']='?token=xxxx&action=search&matricula=xxxxxxxxxx'
        return result
            

