# Network-platform

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

> Rede social desenvolvida com **Django e JavaScript (AJAX)**. Usuários podem criar posts, seguir usuários e curtir conteúdo. Inclui edição em tempo real, paginação e perfis.

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas para as seguintes tarefas:

- [ ] Integrar postgres
- [ ] Alimentar com testes para todos os endpoints necessários.
- [ ] Sistema de notificações em tempo real com WebSockets para curtidas, seguidores e menções.
- [ ] Upload de imagens, GIFs e vídeos com galeria de mídia nos perfis.

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente do [Python 3.13+](https://www.python.org/)

## 🚀 Instalando

Para instalar, siga estas etapas:

1. Clone o repositório
```bash
git clone https://github.com/Ayrton-Machado/network-platform

cd network-platform
```

2. Instale as dependências
```bash
pip install -r requirements.txt
```

3. Configure o banco de dados
```bash
python manage.py makemigrations

python manage.py migrate
```


## ☕ Usando

Para usar, siga estas etapas:

```bash
python manage.py runserver
```
- http://localhost:8000/