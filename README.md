# Gerenciador de Despesas CLI

Este projeto é um **Gerenciador de Despesas** baseado em **linha de comando (CLI)**, permitindo adicionar, visualizar, editar e excluir despesas de um arquivo JSON.

## 📌 Funcionalidades
- **Adicionar** uma nova despesa com nome e valor.
- **Visualizar** todas as despesas salvas.
- **Editar** uma despesa existente.
- **Excluir** uma despesa pelo nome.

##  Como Usar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/despesas-cli.git
   cd despesas-cli
   ```

2. Execute o script com os seguintes comandos:

   - **Adicionar despesa:**
     ```bash
     python main.py adicionar "nome" valor
     ```
     Exemplo:
     ```bash
     python main.py adicionar comida 20
     ```
   
   - **Visualizar despesas:**
     ```bash
     python main.py visualizar
     ```
   
   - **Editar uma despesa:**
     ```bash
     python main.py editar "nome"
     ```
     Depois, siga as instruções para inserir os novos valores.
   
   - **Excluir uma despesa:**
     ```bash
     python main.py excluir "nome"
     ```

## 🛠 Tecnologias Utilizadas
- **Python** (Manipulação de arquivos JSON e entrada de dados)
- **argparse** (Processamento de argumentos de linha de comando)
- **JSON** (Armazenamento das despesas de forma estruturada)

## 📂 Estrutura do Projeto
```
/despesasCLI
│-- main.py  # Script principal
│-- despesas.json  # Banco de dados das despesas (JSON)
│-- README.md  # Documentação
```

##  Autor
Desenvolvido por Millena França.

