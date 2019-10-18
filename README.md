# AAT - 8500

## Como desenvolver?

1. Clone o repositório.
2. Crie um virtual env com python 3.7
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:fnscoder/aat-8500.git aat-8500
cd aat-8500
python -m venv .ve
source .ve/bin/activate
pip install -r requirements.txt
cd contrib/env-sample .env
python manage.py test
```