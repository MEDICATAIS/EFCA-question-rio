import streamlit as st

def classificar(score, faixa):
    if score <= faixa[0]:
        return "Baixo"
    elif score <= faixa[1]:
        return "Médio"
    else:
        return "Alto"

perguntas = {
    "Comer Emocional": [
        "Acalmo minhas emoções com comida.",
        "Tenho o hábito de beliscar.",
        "Belisco entre as refeições por emoções negativas.",
        "Como nos momentos em que estou emocionalmente abalado."
    ],
    "Hiperfagia": [
        "Como até me sentir muito cheio.",
        "Peço mais comida quando termino meu prato.",
        "Costumo comer mais de um prato nas refeições principais."
    ],
    "Comer Hedônico": [
        "Quando começo a comer algo que gosto muito, tenho dificuldade em parar.",
        "Sinto-me tentado a comer ao ver/cheirar comida de que gosto.",
        "Como algo que gosto muito, mesmo sem fome.",
        "Quando como algo que gosto, finalizo toda a porção."
    ],
    "Comer Desorganizado": [
        "Tomo café da manhã todos os dias (pontuação invertida).",
        "Pulo alguma refeição principal.",
        "Passo mais de 5 horas do dia sem comer."
    ],
    "Comer Compulsivo": [
        "Como muita comida em pouco tempo.",
        "Quando como algo que gosto muito, como muito rápido."
    ]
}

limites = {
    "Comer Emocional": (8, 12),
    "Hiperfagia": (5, 8),
    "Comer Hedônico": (11, 14),
    "Comer Desorganizado": (4, 6),
    "Comer Compulsivo": (3, 6)
}

st.title("Questionário EFCA - Avaliação de Comportamento Alimentar")
st.write("Responda cada pergunta selecionando a opção que melhor descreve seu comportamento.")

opcoes = {"Nunca":1, "Raras vezes":2, "Às vezes":3, "Quase sempre":4, "Sempre":5}

respostas = {}

for dominio, questoes in perguntas.items():
    st.header(dominio)
    respostas[dominio] = []
    for idx, questao in enumerate(questoes):
        escolha = st.radio(questao, list(opcoes.keys()), key=f"{dominio}-{idx}")
        valor = opcoes[escolha]
        if dominio == "Comer Desorganizado" and idx == 0:
            valor = 6 - valor
        respostas[dominio].append(valor)

if st.button("Enviar Respostas"):
    st.subheader("Resultados")
    for dominio, valores in respostas.items():
        total = sum(valores)
        faixa = limites[dominio]
        categoria = classificar(total, faixa)
        st.write(f"**{dominio}:** {total} pontos - {categoria}")
