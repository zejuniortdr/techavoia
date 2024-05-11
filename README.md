# TechAvoIA

## O que é:
O TechAvoIA é uma interface amigável para apoio em problemas cotidianos relacionadios a tecnologia, porém não limitado a este contexto, com público-alvo desde crianças até idosos, com ou sem conhecimentos técnicos, para que todos tenham um passo a passo bem explicado de como resolver problemas como: como parear um fone bluetooth com um celular, como resetar de fábrica um celular, como fazer fórmulas no excel, como configurar uma impressora, etc.


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
3. Rode `make setup` para criar o `.env` e o configue com suas chaves
4. Para subir o container, execute o comando `make`
5. Ao final do processo, acesse seu navegador com o endereço `http://localhost:9000` para a interface de usuário
6. Caso queira ver a interface adminsitrativa, acesse `http://localhost:9000/admin` com usuario `root` e senha `123`
7. Para criação de novas credenciais do admin, execute o comando `make create_admin` com o container rodando
8. Para parar o serviço, execute comando `make stop`


## Requisitos para avaliação do projeto:
- [x] Subir em um repositório do Github
- [x] Desenvolva um Projeto Relacionado à Aula 4 e/ou Aula 5 da Imersão IA 2ª Edição
- [x] Utilização da API KEY [feito aqui](https://github.com/zejuniortdr/techavoia/blob/0ef52fb44eea92cf3feab1a424ef3e21c796352d/apps/clients/aistudio.py#L11)
- [x] Criação de conteúdo através da AI com GenerativeModel feito [aqui](https://github.com/zejuniortdr/techavoia/blob/2199d5b998321742e5e69a8c1cfd728bb8e906e4/apps/clients/aistudio.py#L28-L39) e invocado [aqui](https://github.com/zejuniortdr/techavoia/blob/34cf0406fe8b4736df1feb7aa9358e491c36462a/apps/articles/models.py#L46)
- [x] Relacionamento dos conteúdos gerados com outros previamente salvos através das gerações de embeddings feito [aqui](https://github.com/zejuniortdr/techavoia/blob/2199d5b998321742e5e69a8c1cfd728bb8e906e4/apps/clients/aistudio.py#L41-L62) e invocado [aqui](https://github.com/zejuniortdr/techavoia/blob/34cf0406fe8b4736df1feb7aa9358e491c36462a/apps/articles/tasks.py#L45)
- [x] Submissão do projeto através do formulário entre os dias 09/05 e 11/05, até as 23h59.
![image](https://github.com/zejuniortdr/techavoia/assets/1136994/d72db064-a10c-4bb6-a30a-eec17ed10fad)

