# TechAvoIA

## O que é:
O TechAvoIA é uma interface amigável para apoio em problemas cotidianos relacionadios a tecnologia, porém não limitado a este contexto com público-alvo desde crianças até idosos, com ou sem conhecimentos técnicos, para que todos tenham um passo a passo bem explicado de como resolver problemas como: como parear um fone bluetooth com um celular, como resetar de fábrica um celular, como fazer fórmulas no excel, como configurar uma impressora, etc.


## Como funciona:
Focado na busca como seu principal recurso, a pergunta do usuário é repassada para a Inteligência Artificial do Google através de um client para o AI Studio, e gera as resposta e um breve resumo redirecionando o usuário para o conteúdo desejado. Essa resposta fica salva para que novos usuários possam aproveitar de uma busca já realizada. Também através da IA, o conteúdo recém criado é relacionado automaticamente a conteúdos similares, exibidos como leitura complementar para usuários que buscam por aquele contexto.


## Público alvo:
A interface mais simples do que as telas de chatbots atuais visa atender a todos, e por manter um histórico colaborativo, facilita o compartilhamento de conhecimento.


## Tecnologias utilizadas:
- docker
- python
- django
- google-generativeai
- numpy
- pandas


## Pre-requisitos:
- Docker


## Setup do projeto:
1. Clone ou faça download deste repositório
2. Acesse a pasta techavoia através do comando `cd techavoia`
3. Para subir o container, execute o comando `make`
4. Ao final do processo, acesse seu navegador com o endereço `http://localhost:9000` para a interface de usuário
5. Caso queira ver a interface adminsitrativa, acesse `http://localhost:9000/admin`
6. Para criação das credenciais do admin, execute o comando `make create_admin` com o container rodando
7. Para parar o serviço, execute comando `make stop`


## Requisitos para avaliação do projeto:
- [x] Subir em um repositório do Github
- [x] Desenvolva um Projeto Relacionado à Aula 4 e/ou Aula 5 da Imersão IA 2ª Edição
- [x] Utilização da API KEY [feito aqui](https://)
- [x] Criação de conteúdo através da AI com GenerativeModel [feito aqui](https://)
- [x] Relacionamento dos conteúdos gerados com outros previamente salvos através das gerações de embeddings [feito aqui](https://)
- [x] Submissão do projeto através do formulário entre os dias 09/05 e 11/05, até as 23h59.
