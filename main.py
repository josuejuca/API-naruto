from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import naruto as n

app = FastAPI()

naruto = {
    "nome": "Naruto",
    "desc": "Momentos antes do nascimento de Naruto Uzumaki, um enorme demônio conhecido como o Kyuubi, a Raposa de Nove Caudas, atacou o vilarejo da folha oculta Konoha, causando destruição. Para pôr fim à devastação de Kyuubi, o líder da aldeia, o quarto Hokage, sacrificou sua vida e selou o monstruoso animal dentro do recém-nascido Naruto. Agora, Naruto é um ninja hiperativo e cabeça dura que ainda vivem em Konoha. Evitado pelos demais habitantes por causa da Kyuubi dentro dele, Naruto se esforça para encontrar seu lugar na aldeia, enquanto o seu ardente desejo de se tornar o Hokage de Konoha o leva a conhecer alguns grandes novos amigos, e também alguns inimigos mortais.",
    "ano": "2002",
    "capa": "https://assets-juca.netlify.app/img/playanimes/anime/capa/naruto/a0008.jpg",
    "nota": "4.7",
    "direcao": "Hayato Date.",    
    "roteiro": "Masashi Kishimoto.",
    "eps": "220/220",
    "link": "/anime/naruto",
    "url": "/naruto",
    "criacao": "Masashi Kishimoto.",
    "studio": "Studio Pierrot.",
}

def my_schema():
    openapi_schema = get_openapi(
        title="API Naruto",
        version="1.0",
        routes=app.routes,
    )
    openapi_schema["info"] = {
        "title": "API Naruto",
        "version": "1.0",
        "description": "Api utilizada no site playanimes",
        "contact": {
            "name": "Play Animes",
            "url": "http://playanimes.tk/",            
        }        
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema
app.openapi = my_schema

# /id_anime/ep/id_ep


@app.get("/")
def home():
    return 'API está no ar'


@app.get("/anime")
def anime_list():
    return naruto


@app.get("/{id_anime}")
def anime(id_anime: str):
    if id_anime == 'naruto':
        return naruto
    else :
        return {"Erro": "ID inexistente"}


@app.get("/{id_anime}/ep/{id_ep}")
def pegar_ep(id_anime: str, id_ep):
    if id_anime == 'naruto':
        if id_ep == 'list':
            return n.naruto
        return n.naruto[id_ep]
    else:
        return {"Erro": "ID inexistente"}
