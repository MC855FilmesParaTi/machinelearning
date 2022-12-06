# Filmes Para Ti

O Filmes Pra Ti é um projeto para a disciplina MC855 A - Projeto em Sistemas de Computação, ministrada pela Prof. Dra. Juliana Freitag Borin e pelo PED Paulo Cesar Kussler.
Nosso grupo é composto por:
- Heigon Alafaire Soldera Pires RA:217638
- Luana Felipe de Barros      RA: 201705
- Lucas B.A. Farias RA:220650
- Marcela Medicina Ferreira RA: 183266
- Murilo de Lima Cruz RA: 138923
- Piethro Cesar de Andrade RA:223549

Neste repositório, deixaremos todo o projeto de Machine Learning. Para organização dele, decidimos utilizar o template do <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">Cookiecutter</a>, muito comum em projetos de Machine Learning e Data Science, porém adaptamos o template de acordo com as necessidades do nosso projeto.

Para obter os dados finais, você pode baixá-los <a target="_blank" href="https://drive.google.com/drive/folders/1eABXKaebgqPZEvNfjDPIWcwFmir05Fg-?usp=sharing">aqui</a> e guardar nas pastas adequadas (conforme a organização do projeto). Devido ao limite de tamanho dos arquivos no git, não pudemos carregar processed e raw diretamente. 

Também sobre os dados, você pode obtê-los de maneira automatizada rodando o script 'make_dataset.py' localizado na pasta src/data, mas já enfrentamos problemas de indisponibilidade da API, e nesses casos, vale fazer o download do Kaggle - assim como fizemos.

## Organização do Projeto 

------------

    ├── README.md          <- O top-level README para os desenvolvedores usando este projeto.
    ├── data
    │   ├── processed      <- Dados finais, os que de fato serão usados no modelo.
    │   └── raw            <- Os dados originais, dados crus.
    │    
    ├── models             <- Parâmetros de modelos previamente treinados com 1M e 100K reviews, assim como notebook e dados usados.
    │
    ├── notebooks          <- Notebooks com análises exploratórias e experimentos. O convenção de nomes é um número (para ordem), 
    │                         iniciais do nome da pessoa criou, e um `-` para delimitação da descrição. 
    │                         ex: `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Artigos científicos usados na revisão. 
    │
    ├── reports            <- Análises geradas.
    │   └── figures        <- Figuras e gráficos usados nos reports.
    │
    ├── requirements.txt   <- O arquivo de requerimentos para reproduzir o projeto, 
    |                      <- Execute o comando `pip install -r requirements.txt` 
    │
    ├── src                <- Código fonte do projeto.
        │
        ├── data           <- Scripts para baixar ou gerar dados.
        │   └── make_dataset.py
        │
        ├── models         <- Scripts para treinar os modelos e fazer previsões.
        │   ├── model-ncf.py

  


--------

## Problema Investigado

Para a frente de ML, tínhamos o objetivo de treinar modelos para realizar recomendações para usuários de forma automática.
Testamos duas abordagens principais: filtros colaborativos e filtros colaborativos neurais. 
Os filtros colaborativos são uma abordagem muito utilizada na literatura para recomendações, mas da forma que implementamos, não era escalável para uma quantidade grande de recomendações além de ser muito demorado.

Como alternativa, utilizamos filtros colaborativos neurais (NCF), e nessa abordagem pudemos usar modelos tensorflow, o que nos permitiu rodar os modelos em GPU usando o Google Colab. Vale ressaltar que para a versão de 1M de avaliações é necessário usar os recursos do Colab Pro (que infelizmente, é pago).

Na abordagem de NCF nos baseamos numa implementação da biblioteca "reco-utils", que estava escrita em uma versão não compatível com o colab. Tivemos que adaptar todo o código para que pudêssemos usá-lo com nossos dados e realizar nossos testes. 
Por tanto, a quem interessar, vale realizar os experimentos com as duas metodologias para fins compativos e científicos.


## Passos Futuros 

Como mencionado anteriormente, conseguimos um ganho de performance bem considerável com os NCF mas essa abordagem tem um problema: você não pode adicionar novos usuários. Ou seja, os usuários do teste, necessariamente deverão estar no treino para que você possa obter resultados consistentes. Uma alternativa, seria implementar um algoritmo que aceite a inserção de novos usuários, como por exemplo o Neural Graph Collaborative Filtering.

Outra alternativa para passos futuros seria também procurar uma forma para rodar os filtros colaborativos tradicionais em GPU. Algumas possíveis libs pesquisadas seriam cudf/cupy e implicit. 
