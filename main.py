import argparse
import json

parser = argparse.ArgumentParser(description="Gerenciador de Despesas CLI")

#definir args
parser.add_argument("acao", choices=["adicionar","visualizar", "editar", "excluir"], help="Escolher ação executada")
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

#Funçoes
def adicionarDespesa(nome_despesa, valor): #passa os argumentos definidos no parser
    despesas = carregar_despesas()  # Carrega os dados antes de modificar
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
            print(f"[{despesa['id']}] {despesa['nome_despesa']} - {despesa['valor']:.2f}")

def editarDespesa(nome_despesa):
    despesas = carregar_despesas()  # Carrega os dados antes de modificar
    encontrada = False

    for despesa in despesas:
        if despesa["nome_despesa"] == nome_despesa:
            try:  # <-- Aqui estava desalinhado antes
                novo_nome = input(f"Digite o novo nome para '{nome_despesa}': ").strip()
                novo_valor = float(input(f"Digite o novo valor para '{nome_despesa}': ").strip())

                despesa["nome_despesa"] = novo_nome
                despesa["valor"] = novo_valor

                salvar_despesas(despesas)
                print(f"Despesa '{nome_despesa}' atualizada para '{novo_nome}' com valor R$ {novo_valor:.2f}")
                encontrada = True  # Marca como encontrada
                break  # Sai do loop pois a despesa já foi editada

            except ValueError:
                print("Erro: Insira um valor numérico válido.")

    if not encontrada:
        print(f"Despesa '{nome_despesa}' não encontrada.")

def excluirDespesa(nome_despesa):
    despesas = carregar_despesas()  # Carrega os dados antes de modificar
    nova_lista = [despesa for despesa in despesas if despesa["nome_despesa"] != nome_despesa]

    if len(nova_lista) == len(despesas):
        print(f"Despesa '{nome_despesa}' não encontrada")
    else:
        salvar_despesas(nova_lista)
        print(f"despesa '{nome_despesa}' foi removida com sucesso")

#Quando seleciona acao
if args.acao == "adicionar":
    if args.nome_despesa and args.valor:
        adicionarDespesa(args.nome_despesa, args.valor)
    else:
        print("Por favor, insira dados válidos")

if args.acao =="visualizar":
    despesas = carregar_despesas() # Carrega os dados somente quando necessário
    if not despesas:
        print("Não há despesas para visualizar")
    else:
        listarDespesas()
        
if args.acao =="editar":
    if args.nome_despesa:
        editarDespesa(args.nome_despesa)
    else:
        print("Por favor insir ao nome da despesa que deseja editar")

if args.acao =="excluir":
    if args.nome_despesa:
        excluirDespesa(args.nome_despesa)
    else:
        print("Por favor, insira o nome da despesa que deseja excluir")