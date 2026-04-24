import urllib.request
import urllib.parse
from datetime import date

PESSOAS = [
    {"nome": "Maria Rita", "dia": 8, "mes": 1},
    {"nome": "Rone", "dia": 23, "mes": 1},
    {"nome": "Gustavo", "dia": 14, "mes": 2},
    {"nome": "Ana Maria", "dia": 18, "mes": 2},
    {"nome": "Eduardo", "dia": 19, "mes": 2},
    {"nome": "Lucas", "dia": 21, "mes": 2},
    {"nome": "Maria", "dia": 21, "mes": 2},
    {"nome": "Paulo", "dia": 28, "mes": 2},
    {"nome": "Mari", "dia": 28, "mes": 2},
    {"nome": "João Lucas", "dia": 1, "mes": 3},
    {"nome": "Pedro", "dia": 25, "mes": 3},
    {"nome": "Jonas", "dia": 28, "mes": 3},
    {"nome": "Davi", "dia": 5, "mes": 4},
    {"nome": "Vanéria", "dia": 17, "mes": 4},
    {"nome": "Laura", "dia": 7, "mes": 5},
    {"nome": "Danilo", "dia": 18, "mes": 5},
    {"nome": "André Assunção", "dia": 1, "mes": 6},
    {"nome": "Miguel", "dia": 2, "mes": 6},
    {"nome": "Isabel", "dia": 23, "mes": 6},
    {"nome": "José", "dia": 5, "mes": 7},
    {"nome": "Mateus", "dia": 16, "mes": 7},
    {"nome": "Davi", "dia": 23, "mes": 7},
    {"nome": "Tomás", "dia": 6, "mes": 8},
    {"nome": "Isabel", "dia": 5, "mes": 8},
    {"nome": "Guilherme", "dia": 8, "mes": 8},
    {"nome": "Mateus Assunção", "dia": 18, "mes": 8},
    {"nome": "Rafael", "dia": 25, "mes": 8},
    {"nome": "Juliana", "dia": 3, "mes": 9},
    {"nome": "Júlia", "dia": 8, "mes": 9},
    {"nome": "Francisco José", "dia": 15, "mes": 9},
    {"nome": "Teresa", "dia": 16, "mes": 9},
    {"nome": "Gabriel", "dia": 20, "mes": 9},
    {"nome": "Tiago", "dia": 1, "mes": 10},
    {"nome": "André", "dia": 7, "mes": 10},
    {"nome": "Filipe", "dia": 9, "mes": 10},
    {"nome": "Raul", "dia": 21, "mes": 10},
    {"nome": "Teresa", "dia": 22, "mes": 10},
    {"nome": "Helena", "dia": 26, "mes": 10},
    {"nome": "Cecília", "dia": 27, "mes": 10},
    {"nome": "Maria Fernanda", "dia": 7, "mes": 11},
    {"nome": "Gabriel Assunção", "dia": 20, "mes": 11},
    {"nome": "Maria Clara", "dia": 1, "mes": 12},
    {"nome": "Bia", "dia": 3, "mes": 12},
    {"nome": "Fabrícia", "dia": 3, "mes": 12},
    {"nome": "João", "dia": 15, "mes": 12},
]

# Números que vão receber o aviso — formato: (numero_com_ddi, api_key)
# A api_key você recebe do CallMeBot após ativar
DESTINATARIOS = [
    ("5516991981267", "7722638"),
]

def verificar_e_disparar():
    hoje = date.today()
    aniversariantes = [
        p["nome"] for p in PESSOAS
        if p["dia"] == hoje.day and p["mes"] == hoje.month
    ]

    if not aniversariantes:
        print("Nenhum aniversariante hoje.")
        return

    nomes = " e ".join(aniversariantes)
    if len(aniversariantes) == 1:
        msg = f"🎂 Hoje é aniversário de *{nomes}*! Não esqueça de mandar parabéns! 🎉"
    else:
        msg = f"🎂 Hoje fazem aniversário: *{nomes}*! Mande parabéns para eles! 🎉"

    print(f"Aniversariantes hoje: {nomes}")

    for numero, apikey in DESTINATARIOS:
        if apikey == "SUA_API_KEY_AQUI":
            print(f"⚠️  Configure a API Key do CallMeBot para o número {numero}")
            continue
        url = f"https://api.callmebot.com/whatsapp.php?phone={numero}&text={urllib.parse.quote(msg)}&apikey={apikey}"
        try:
            urllib.request.urlopen(url)
            print(f"✅ Mensagem enviada para {numero}")
        except Exception as e:
            print(f"❌ Erro ao enviar para {numero}: {e}")

if __name__ == "__main__":
    verificar_e_disparar()
