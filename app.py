import web  # pip installl web.py

urls = (
    '/alumnos/?', 'application.controllers.alumnos.Alumnos',  # /= raiz  Hello la clase 
)
app = web.application(urls, globals())

render = web.template.render('templates/')



if __name__ == "__main__":
    web.config.debug= False
    app.run()