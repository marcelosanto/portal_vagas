import streamlit as st

# Função que define o conteúdo do diálogo


@st.dialog("Meu Dialog de Teste")
def show_dialog():
    st.write("Este é um diálogo de teste!")
    if st.button("Fechar"):
        st.session_state.dialog_open = False
        st.rerun()


# Botão para abrir o diálogo
if st.button("Abrir Diálogo"):
    st.session_state.dialog_open = True

# Verifica se o diálogo deve ser exibido
if st.session_state.get("dialog_open", False):
    show_dialog()
