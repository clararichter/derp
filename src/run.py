from derp import app

# if the application is run
if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run(port=app.config['PORT'], host=app.config['HOST'])
