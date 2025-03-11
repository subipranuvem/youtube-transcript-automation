# Youtube Transcript N8N Example

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

## API em Python

Esse repositório conta com uma API em Python para obter a transcrição de um vídeo do YouTube dado uma URL ou um ID do vídeo.

Para acessar a documentação, acesse:

👉 http://localhost:8001/docs

### Exemplo

Você pode chamar a API usando esse comando abaixo no terminal:

```sh
curl http://localhost:8000/youtube/transcript\?video_id\=9Dzttt1sCuM
```