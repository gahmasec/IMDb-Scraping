[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/guilhermevieira98/IMDb-Scraping) 

# IMDb Scraping
Desenvolvi este projeto por ser um aficionado por filmes, e deste modo poder organizar as minhas listas pessoais. 
Como qualquer fã uso muito o IMDb para poder estar sempre atualizado, no entanto não considero que as listas que nos permite criar sejam as mais práticas. 
Deste modo resolvi desenvolver um projeto que extrai os dados das listas que já tenho criadas, dando-me a possibilidade de puder manipular esta informação do jeito que entender. 

# Dependências necessárias

- lxml (https://pypi.org/project/lxml/)
- bs4 (https://pypi.org/project/bs4/)
- requests (https://pypi.org/project/requests/)

# Extrair os dados das listas #

Para extrair os dados é necessário ter em atenção: 
- Chart List

![personal](https://user-images.githubusercontent.com/32024844/78297703-0ae2d180-7528-11ea-93a6-abb60ea4c473.png)

``` python
movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
```
- Personal List

![chart](https://user-images.githubusercontent.com/32024844/78297504-a0ca2c80-7527-11ea-933c-6d7615a28626.png)

``` python
movies = soup.select('h3.lister-item-header')
links = [a.attrs.get('href') for a in soup.select('h3.lister-item-header  a')]
crew = [a.attrs.get('title') for a in soup.select('h3.lister-item-header  a')]
```
A configuraçao de cada tipo de lista diverge devido à forma de como a estrutura das listas do website foi desenvolvida. 

# Run #
Ao executarmos "save.py" automaticamente o script "imdb-list.py" é executado e extrai os dados da lista que desejamos.
Este script para além disso, irá armazenar os dados obtidos do output num ficheiro.

``` python
import subprocess
with open("output.txt", "w+") as output:
    subprocess.call(["python", "./imdb-list.py"], stdout=output);

```
> Nota: É importante lembrar que os "nomes" estão separados dos "anos" por virgulas para ser possivél que o Excell compreenda e automaticamente insira os dados de modo perceptivel.

## Executar ##
``` python
python save.py

```
