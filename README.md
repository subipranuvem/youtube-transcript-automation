# Youtube Transcript N8N Example

API em Python para Transcrição de Vídeos do YouTube que é utilizado como uma _Tool_ em um agente de IA no N8N.

## Requisitos

Antes de começar, você precisa instalar alguns programas:

### 1. Docker (para rodar o N8N)

- Se estiver usando Windows ou Mac, baixe o Docker Desktop: https://docs.docker.com/desktop/
- Se estiver usando Linux, siga este guia: https://docs.docker.com/engine/install/

### 2. Chave da API do Gemini (para integração com IA)

- Se ainda não tem uma chave, crie uma aqui: https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br
- Se já tem uma chave, acesse-a aqui: https://aistudio.google.com/app/apikey

## Guia em Vídeo

Gravamos um vídeo para te guiar no processo. Assista aqui: [INSERIR LINK DO VÍDEO].

## Por que rodar o N8N localmente?

Se você criar uma conta no site oficial do N8N, terá acesso apenas à versão trial, que é paga após um período. Ao rodar o N8N localmente, você poderá utilizá-lo de forma gratuita e sem limitações da versão trial.

## Como acessar o N8N

Depois que o N8N estiver rodando, abra seu navegador e acesse:

👉 http://localhost:5678

## Como iniciar e parar o projeto

### Para iniciar as dependências do projeto
Abra o terminal (ou PowerShell no Windows), vá até a pasta do projeto e execute:
```sh
 docker compose up -d
```
Isso inicia as dependências em segundo plano (se você fechar o terminal ou PowerShell, as dependências ainda continuarão executando).

### Para parar as dependências do projeto
Caso precise desligar as dependências, use:
```sh
 docker compose down
```

### Para parar as dependências e apagar os dados salvos
Se quiser limpar tudo ao desligar:
```sh
 docker compose down --volumes
```

# API em Python para Transcrição de Vídeos do YouTube

Este repositório contém uma API desenvolvida em Python que obtém a transcrição de um vídeo do YouTube a partir de uma URL ou ID do vídeo.

## 📖 Documentação  

Acesse a documentação interativa via Swagger:  

👉 [http://localhost:8001/docs](http://localhost:8001/docs)  

---

## 🚀 Exemplo de Uso  

Você pode chamar a API usando o seguinte comando no terminal:

```sh
curl "http://localhost:8000/youtube/transcript?video_id=9Dzttt1sCuM"
```

---

## ⚙️ Rodando a API Localmente sem utilizar Docker (Opcional)

Por padrão a API roda em um container quando o comando docker é executado. Mas, se você quiser rodar a API localmente, sem utilizar o Docker, abaixo seguem as instruções.

### 1. Criar um ambiente virtual  

```sh
python -m venv .venv
```

### 2. Ativar o ambiente virtual  

- **Linux/macOS**:  
  ```sh
  source .venv/bin/activate
  ```
- **Windows** (PowerShell):  
  ```sh
  .venv\Scripts\Activate
  ```

### 3. Instalar o Poetry  

Se ainda não tiver o Poetry instalado, siga as instruções: [Guia de Instalação do Poetry](https://python-poetry.org/docs/#installation)

### 4. Instalar dependências  

```sh
poetry install
```

### 5. Iniciar a API  

```sh
python app.py
```


## ⚠️ Configuração da Porta  

Por padrão, a API roda:  
- Na **porta 8000** quando executada localmente.  
- Na **porta 8001** quando executada via Docker.  

Se desejar alterar a porta, edite o arquivo `.env` e adicione:

```sh
PORT=9000
```

## Subindo a imagem para o Docker Hub ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

A [imagem da API](https://hub.docker.com/r/subipranuvem/youtube_transcript_api) foi armazenada no Docker Hub para que seja possível que outras pessoas a reutilizem.

Para subir a imagem para o Docker Hub, primeiro, logue no DockerHub subistituindo o `{usuario_docker_hub}` pelo seu usuário:

```sh
docker build -t {usuario_docker_hub}/youtube_transcript_api . && docker push {usuario_docker_hub}/youtube_transcript_api
```

Em seguida execute esse comando:

```sh
docker build -t {usuario_docker_hub}/youtube_transcript_api . && docker push subipranuvem/youtube_transcript_api
```