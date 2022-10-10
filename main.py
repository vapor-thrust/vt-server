from fastapi import FastAPI

app = FastAPI()


@app.get('/items/{item}')
def read_item(item: int, q:str):
    return {'item': item, 'query': q}
