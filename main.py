from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {'Saludo': 'Hello, world!'}


@app.get("/despedida")
def next():
    return {
            'Despedida': 'Esto no es un adios',
            'Bueno': 'Parece que si lo es, adios!'
            }


@app.get('/encuentro')
def prev():
    return 'Parece que nos volvimos a ver'
