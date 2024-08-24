# Projeto de watchlist de Animes

## Descrição
Este projeto Django é um gerenciador de animes simples que permite aos usuários:

* **Buscar animes:** Pesquisar por animes através de uma API externa e salvar no banco de dados.
* **visualizar os animes pesquisados:** Adicionar animes encontrados à lista de animes para assistir.
* **Remover animes:** Remover animes da lista de animes salvos(remove também da watchlist).
* **Adicionar à watchlist:** Adicionar animes encontrados à lista de animes para assistir.
* **Remover da watchlist:** Remover animes da lista de animes.
* **Visualizar watchlist:** Verificar todos os animes adicionados à watchlist.

## Pré-requisitos
* Python (versão 3.6 ou superior)
* Django (instalar com `pip install django`)
* Um banco de dados (SQLite é o padrão do Django)

## Instalação
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/MateusIR/workshop-fabrica-2024.2.git


1. **Crie um ambiente virtual:**
```Bash
python -m venv venv
```

3. **Ative o ambiente virtual:**

Windows: ```venv\Scripts\activate```

Linux/macOS: ```source venv/bin/activate```


4. **Instale as dependências:**
```Bash
pip install -r requirements.txt
```

5. **Faça as migrações:**
```Bash
python manage.py makemigrations
python manage.py migrate
```


6. **Execute o servidor de desenvolvimento:**
```Bash
python manage.py runserver
```

### Uso:

Acesse a aplicação no seu navegador (por exemplo, http://127.0.0.1:8000/).
Utilize a interface para buscar animes, adicionar à watchlist e visualizar a lista.

### Estrutura do Projeto:

**animes:** Aplicativo principal, contendo modelos, views, forms e URLs para a funcionalidade de buscar e gerenciar animes.

**watchlist:** Aplicativo para gerenciar a watchlist do usuário.