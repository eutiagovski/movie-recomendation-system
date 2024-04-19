# Recomenda Ae
Sistema de recomendação de Filmes e Séries de TV baseado em conteúdo em potuguês.

<a href='https://recomenda-ae.streamlit.app'>Acesse aqui o recomendador e descubra os melhores filmes!</a>

## Introdução

Na era digital, encontrar um filme para assistir pode se tornar uma tarefa desafiadora diante da vasta quantidade de opções disponíveis. Com a proliferação de plataformas de streaming e catálogos cada vez mais extensos, os espectadores muitas vezes se veem perdidos em meio a uma infinidade de escolhas, sem saber por onde começar.

Cansado de passar horas procurando filmes com boas recomendações para assistir, decidi criar um algoritmo de recomendação de filmes baseado no conteúdo. Este projeto visa facilitar a vida dos cinéfilos, fornecendo uma solução inteligente e eficiente para a difícil tarefa de escolher o próximo filme a assistir.

Ao utilizar técnicas avançadas de análise de dados e processamento de linguagem natural, nosso objetivo é criar um sistema de recomendação personalizado, capaz de sugerir filmes relevantes com base nas preferências de cada usuário. Com isso, esperamos proporcionar uma experiência cinematográfica mais satisfatória e enriquecedora, ajudando os espectadores a descobrir novos filmes e redescobrir antigos favoritos de maneira simples e intuitiva.

## Objetivo

O objetivo deste projeto é desenvolver um sistema de recomendação de filmes em língua portuguesa que ofereça aos usuários sugestões personalizadas e relevantes, levando em consideração as características dos filmes. Dividimos este trabalho em três partes:

- Coleta dos dados públicos do site IMDB combinados com datasets disponibilizados pelo próprio site.

- Criação de um algoritmo robusto de recomendação baseado em conteúdo, que analise as características intrínsecas dos filmes, como gênero, elenco, direção e sinopse, para identificar padrões e relacionamentos entre eles, utilizando técnicas avançadas de processamento de linguagem natural para analisar críticas e avaliações de filmes, a fim de compreender melhor o conteúdo e as preferências dos usuários.

- Desenvolver um aplicativo acessível e intuitivo, no qual os usuários possam buscar por filmes e explorar informações detalhadas sobre cada título.

### Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

## Medologia

Para este projeto utilizaremos tecnologias como webscraping para coleta dos reviews, url das imagens e outras informações diretamente do site público IMDB. O webscraping é uma técnica amplamente empregada para extrair informações de páginas da web de forma automatizada, permitindo a obtenção de dados de maneira eficiente e precisa. Combinaremos esses dados coletados com datasets públicos disponibilizados pelo IMDB, tais como críticas, classificações, e informações sobre o elenco e equipe técnica para formar um dataset único.

Além disso, exploraremos técnicas de processamento de linguagem natural (NLP) para analisar as descrições dos filmes e séries, a fim de extrair características e padrões que serão utilizados na construção do modelo de recomendação. A NLP é uma área da inteligência artificial que se concentra na interação entre computadores e linguagem humana, permitindo a análise e compreensão de texto de forma automatizada.

Ao final, utilizaremos o Streamlit, que é um framework de código aberto que simplifica a criação de aplicativos web interativos em Python. Com o Streamlit, podemos transformar nosso código Python em um aplicativo web com facilidade, incorporando componentes interativos para melhorar a experiência do usuário. Essa escolha permite que desenvolvamos um aplicativo de recomendação de filmes intuitivo e dinâmico, onde os usuários podem buscar por filmes, receber recomendações personalizadas e explorar informações detalhadas sobre cada título de forma interativa e acessível.

## Desenvolvimento

O desenvolvimento deste trabalho está detalhado nos noeteboks que seguem:

- <a href='https://github.com/eutiagovski/movie-recomendation-system/blob/master/notebooks/create_data.ipynb'>Coleta, limpeza e transformação dos dados</a>
- <a href='https://github.com/eutiagovski/movie-recomendation-system/blob/master/notebooks/create_model.ipynb'>Modelagem do algoritmo</a>

## Conclusões

## Próximos Passos

- Integrar as notas dos usuários do <a href=''>Adoro Cinema</a> no aplicativo para uma experiência ainda mais "abrasileirada".

## Críticas e Sugestões

Se você deseja fazer alguma crítica ou sugestão ao projeto, entre em contato comigo diretamente pelo meu <a href='https://www.linkedin.com/in/tiagomachadodev'>Linkedin</a>