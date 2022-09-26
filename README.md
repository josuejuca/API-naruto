<p align="center">
  <a href="https://github.com/josuejuca/API-naruto/">
    <img src="https://assets-juca.netlify.app/img/playanimes/anime/capa/naruto/a0008.jpg" alt="[ ]">
  </a>

  <h3 align="center">Naruto API</h3>

  <p align="center">
    <samp>Uma API de streaming de anime gratuita do  <a href="https://playanimes.tk/">Play Animes</a></samp>
    <br />
    <br />
    <a href="#rotas"><strong>Explorar a API »</strong></a>
    
  </p>
</p>

> ### Note:
> Essa [API](https://api--naruto.herokuapp.com/) foi feita para um teste de desempenho, pode ser que daqui um tempo ela não esteja funcionando.

<h1> Índice </h1>

- [Instalação](#install)
  - [Local](#local)
  - [Heroku](#heroku)
- [Rotas](#rotas)
  - [Detalhes do Anime](#get-anime-details)
  - [Streaming URLs](#get-streaming-urls)

    
## Instalação <br id="install">



### Local 

Execute o seguinte comando para clonar o repositório e instale as dependências:

```sh
git clone https://github.com/josuejuca/API-naruto.git
cd API-naruto
pip install -r requirements.txt
```

Inicie o servidor com o seguinte comando:

```sh
uvicorn main:app --reload
```
Agora o servidor está rodando http://127.0.0.1:8000/

### Heroku
Hospede sua própria instância da api no heroku usando o botão abaixo.

[![Deploy no Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/josuejuca/API-naruto/tree/main)


## Rotas <br id="rotas">
Abaixo você encontrará exemplos usando [Requests Python](https://requests.readthedocs.io/en/latest/) mas você pode usar qualquer outra biblioteca http disponível.





### Obter detalhes do Anime  <br id="get-anime-details">

| Parameter      | Description                                                                          |
| -------------- | ------------------------------------------------------------------------------------ |
| `:id` (string) | **Essa API é composta por apenas um animeID, no nosso caso esse animeID é 'naruto'** |

```py
  link = requests.get("https://api--naruto.herokuapp.com/naruto")
  list = link.json()
  anime_details = list
```

Resultado >>

```json
{
  "nome": "Naruto",
  "desc": ...,
  "ano": "2002",
  "capa": "https://assets-juca.netlify.app/img/playanimes/anime/capa/naruto/a0008.jpg",
  "nota": "4.7",
  "direcao": "Hayato Date.",
  "roteiro": "Masashi Kishimoto.",
  "eps": "220/220",
  "link": "/anime/naruto",
  "url": "/naruto",
  "criacao": "Masashi Kishimoto.",
  "studio": "Studio Pierrot."
}
```

### Obter URLs de streaming <br id="get-streaming-urls">

Você pode precisar do URL de referência para ignorar o código HTTP 403 (Proibido).

| Parameter      | Description                                                                                                                    |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `:id` (string) | **Para verificar o id de cada episódio, veja a propriedade /naruto/ep/list/ no exemplo abaixo.** |

```py
  link = requests.get("https://api--naruto.herokuapp.com/naruto/ep/list")
  list = link.json()
  anime_details = list 
```

Resultado >>

```json
 {
  "1": "https://playersdevideo.com/links/2022/7623200209.html",
  "2": "https://playersdevideo.com/links/2022/6025100983.html",
  "3": "https://playersdevideo.com/links/2022/3959200895.html",
  "4": "https://playersdevideo.com/links/2022/1896633360.html",
  "5": "https://playersdevideo.com/links/2022/6847505705.html",
  "6": "https://playersdevideo.com/links/2022/794003930.html",
  ...
}
```

#### Filtrar ep específico

```py
  link = requests.get("https://api--naruto.herokuapp.com/naruto/ep/list")
  list = link.json()
  anime_details = list['220'] # Número do ep
```

Resultado >>

```json
{
  "https://playersdevideo.com/links/2022/5585473246.html"
}
```
