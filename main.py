import argparse
import json

parser = argparse.ArgumentParser(description="Gerenciador de Despesas CLI")

#definir args
parser.add_argument("acao", choices=["adicionar","visualizar"], help="Escolher ação executada")
parser.add_argument("nome_despesa", type=str, nargs="?", help="Nome da despesa")
parser.add_argument("valor", type=float, nargs="?", help="Valor da despesa")

#Processando os argumentos
args = parser.parse_args()

#nome do arquivo onde vai salvar as despesas
arquivo_despesas = "despesas.json"

def carregar_despesas():
    try:
        with open(arquivo_despesas, "r", encoding="utf-8") as f:
            return json.load(f)  # Converte JSON para lista de dicionários
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Retorna lista vazia se o arquivo não existir ou estiver corrompido)
    
# Função para salvar as despesas no JSON
def salvar_despesas(despesas):
    with open(arquivo_despesas, "w", encoding="utf-8") as f:
        json.dump(despesas, f, indent=4, ensure_ascii=False)  # Escreve a lista no arquivo
despesas = carregar_despesas()

#Funçoes
def adicionarDespesa(nome_despesa, valor):
    if nome_despesa and valor:
        nova_despesa = {"id": len(despesas) + 1, "nome_despesa": nome_despesa, "valor": valor}
        despesas.append(nova_despesa)  # Adiciona na lista
        salvar_despesas(despesas)  # Salva no JSON
        print(f"Despesa '{nome_despesa}' no valor de R$ '{valor:.2f}' adicionada!")
    else:
        print("Parâmetros incorretos")

def listarDespesas():
    if not despesas:
        print("Nenhuma despesa disponível")
    else:
        for despesa in despesas:
            print(f"[{despesa['id']}] {despesa['nome_despesa']} - {despesa['valor']}")

#Quando seleciona acao
if args.acao == "adicionar":
    if args.nome_despesa and args.valor:
        adicionarDespesa(args.nome_despesa, args.valor)
    else:
        print("Por favor, insira dados válidos")

if args.acao =="visualizar":
    if not despesas:
        print("Não há despesas para visuakizar")
    else:
        listarDespesas()