import streamlit as st

# Configuração da página (título da aba do navegador e layout)
st.set_page_config(page_title="Calculadora Streamlit", page_icon="🧮")

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora Interativa")
st.write("Selecione os números, escolha a operação e clique em **Calcular**.")

st.divider()

# Criação de duas colunas para organizar os campos numéricos lado a lado
col1, col2 = st.columns(2)

# 2. Dois campos de entrada numérica com valor padrão 0.0
with col1:
    numero_1 = st.number_input("Primeiro número:", value=0.0, step=1.0, format="%.2f")

with col2:
    numero_2 = st.number_input("Segundo número:", value=0.0, step=1.0, format="%.2f")

# 3. Componente de seleção para escolher a operação
operacao = st.radio(
    "Escolha a operação desejada:",
    options=["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"],
    horizontal=True
)

# 4. Botão de ação "Calcular"
if st.button("Calcular", type="primary", use_container_width=True):
    # 5. Lógica das operações, balões e tratamento de erro
    if operacao == "Soma (+)":
        resultado = numero_1 + numero_2
        st.balloons()  # Solta os balões na tela
        st.metric(label="Resultado da Soma", value=f"{resultado:.2f}")

    elif operacao == "Subtração (-)":
        resultado = numero_1 - numero_2
        st.balloons()  # Solta os balões na tela
        st.metric(label="Resultado da Subtração", value=f"{resultado:.2f}")

    elif operacao == "Multiplicação (*)":
        resultado = numero_1 * numero_2
        st.balloons()  # Solta os balões na tela
        st.metric(label="Resultado da Multiplicação", value=f"{resultado:.2f}")

    elif operacao == "Divisão (/)":
        if numero_2 == 0:
            st.error("⚠️ Ops! Não é possível realizar divisão por zero. Escolha outro valor para o segundo número.")
        else:
            resultado = numero_1 / numero_2
            st.balloons()  # Solta os balões na tela
            st.metric(label="Resultado da Divisão", value=f"{resultado:.2f}