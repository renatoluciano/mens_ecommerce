# 👔 Mens E-commerce - MVP

Um sistema completo de e-commerce voltado para moda masculina, desenvolvido com foco em boas práticas de programação, separação de conceitos e interface amigável.

---

## 🚀 Funcionalidades

- **Vitrine de Produtos:** Listagem dinâmica de roupas com fotos reais, preços e tamanhos.
- **Filtro por Categoria:** Menu interativo para separar roupas por tipo (ex: Camisas, Calças).
- **Carrinho de Compras Completo:**
  - Adicionar e remover itens individualmente.
  - Controle de quantidade interativo (`+` e `-`).
  - Cálculo automático de subtotais e somatório final.
  - Opção para esvaziar todo o carrinho.
  - Trava de segurança para impedir finalização de carrinho vazio.
- **Painel Administrativo:** Área restrita do Django para cadastro e gestão do estoque.
- **Design Responsivo:** Interface moderna construída utilizando o framework Bootstrap.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Framework Web:** Django
- **Estilização:** Bootstrap 5 (via pacote `django-bootstrap5`)
- **Banco de Dados:** SQLite (padrão de desenvolvimento)
- **Controle de Versão:** Git & GitHub

---

## ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o projeto na sua máquina:

**1. Clone o repositório:**
```bash
git clone https://github.com
cd ecommerce_masculino
```

**2. Crie e ative o ambiente virtual:**
No Windows:
```powershell
python -m venv venv
.\venv\Scripts\Activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Execute as migrações do banco de dados:**
```bash
python manage.py migrate
```

**5. Crie um usuário administrador (opcional):**
```bash
python manage.py createsuperuser
```

**6. Inicie o servidor de desenvolvimento:**
```bash
python manage.py runserver
```
Acesse no navegador: `http://127.0.0`

---

## 🚧 Próximos Passos (Evolução)
- Ativar a virtualização na BIOS para migrar o ambiente para **Docker**.
- Integrar com banco de dados **PostgreSQL**.
- Implementar sistema de login e cadastro de clientes.
- Integrar com gateways de pagamento (Pix / Cartão).
