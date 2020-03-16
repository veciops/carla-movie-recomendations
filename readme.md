# Sistema de Recomendação de filmes


### Estutura do projeto:

## Aplicação

A API responsável retorna uma lista de recomendações e uma lista de filtros a serem usados no aplicativo cliente.

A API contém as seguintes rotas:

## / Recommendations

Retorna uma lista de recomendações de filmes com base em uma lista de filtros informados nos parâmetros da string de consulta. 

### Atributos do Método GET (Parâmetros):

* Title
* Cast
* Release_year
* Director
* Listed_in
* Duration

### Exemplo de uma string de consulta:

* title= Good People
* release_year= 2015
* director= Henrik Ruben Genz
* duration= 90 min



## / Filtros

Retorna os filtros mostrados pelo aplicativo cliente para permitir que o usuário possa selecionar suas preferências.


* title
* cast
* country
* release_year
* director
* listed_ind
* duration


Método: GET Parâmetros: Nenhum parâmetro é necessário

## Sistema de Recomendação de Filmes

O sistema foi construído com base no algoritmo [KNN](https://www.linkedin.com/pulse/aplica%C3%A7%C3%A3o-pr%C3%A1tica-em-python-do-algoritmo-k-nearest-knn-rober-junior) e em um conjunto de dados de características de filmes baixados do  [Kaggle](https://www.kaggle.com/shivamb/netflix-shows) . Para construir o projeto, foi usada a implementação do KNN existente na biblioteca [scikit-learn](https://scikit-learn.org/stable/modules/neighbors.html).

## Aplicativo Cliente

Para representar as recomendações para um usuário, um aplicativo da web foi desenvolvido. Onde, o usuário pode selecionar muitos filtros (com base no conteúdo do conjunto de dados) e, após um clique em "Filtro", a API retorna uma lista de recomendações com base nas preferências do usuário ou nula (quando nada atinge o Preferências de usuário).

## A implantação

Para implantar, a plataforma Heroku foi usada. Abaixo os URLs da API e do aplicativo Cliente são informados.

## API:


## CLIENTE:
