Sistema de Recomendação de filmes


Estutura do projeto:

API

Uma API responsável retornando uma lista de recomendações e uma lista de filtros a serem usados ​​no aplicativo cliente.

A API contém as seguintes rotas:

/ Recommendations

Essa rota retorna uma lista de recomendações com base em uma lista de filtros informados nos parâmetros da string de consulta. Abaixo, um exemplo de uma string de consulta é informado.

Método: GET Params:


 self.get_recommendations(request.args.get('title'),
                                     request.args.get('cast'),
                                     request.args.get('country'),
                                     request.args.get('release_year'),
                                     request.args.get('director'),
                                     request.args.get('listed_in'),
                                     request.args.get('duration')))

get_recommendations(self, title, cast, country, release_year, director, listed_in, duration);


/ filtros
Essa rota retorna os filtros mostrados pelo aplicativo cliente para permitir que o usuário possa selecionar suas preferências.


get_index_from_features(self, title, cast, country, release_year, director, listed_in, duration):
        rows = df[(((title == None) | (title == df['title']))) &
              (((cast == None) | (cast == df['cast']))) &
              (((country == None) | (country == df['country']))) &
              (((release_year == None) | (release_year == str(df['release_year'])))) &
              (((director == None) | (director == df['director']))) &
              (((listed_in == None) | (listed_in == df['listed_in']))) &
              (((duration == None) | (duration == df['duration'])))]


filters["title"] = (df["title"].unique()).tolist()
        filters["cast"] = (df["cast"].unique()).tolist()
        filters["country"] = (df["country"].unique()).tolist()
        filters["release_year"] = ((df["release_year"]).unique()).tolist()
        filters["director"] = (df["director"].unique()).tolist()
        filters["listed_in"] = (df["listed_in"].unique()).tolist()
        filters["duration"] = (df["duration"].unique()).tolist()


Método: GET Params: Nenhum parâmetro é necessário

Sistema de recomendação de filmes

O sistema foi construído com base no algoritmo [KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) e em um conjunto de dados de características de filmes baixados do Kaggle . Para construir o projeto, foi usada a implementação do KNN existente na biblioteca scikit-learn .

Aplicativo Cliente

Para representar as recomendações para um usuário, um aplicativo da web foi desenvolvido. Onde, o usuário pode selecionar muitos filtros (com base no conteúdo do conjunto de dados) e, após um clique em "Filtro", a API retorna uma lista de recomendações com base nas preferências do usuário ou nula (quando nada atinge o Preferências de usuário).

A implantação

Para implantar, a plataforma Heroku foi usada. Abaixo os URLs da API e do aplicativo Cliente são informados.

API:


CLIENTE:
