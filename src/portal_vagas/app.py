import streamlit as st
import requests
import textwrap

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Vagas de Tecnologia",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS CSS CUSTOMIZADOS ---
st.markdown("""
<style>
    [data-testid="stVerticalBlock"] .st-emotion-cache-1yyy84j {
        border-radius: 0.5rem;
        padding: 1rem 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: box-shadow 0.3s ease-in-out;
    }
    [data-testid="stVerticalBlock"] .st-emotion-cache-1yyy84j:hover {
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    .label-tag {
        background-color: #E0E0E0;
        color: #333;
        padding: 0.2rem 0.5rem;
        border-radius: 0.3rem;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 0.3rem;
        margin-bottom: 0.3rem;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)

# --- FUNÇÕES PARA BUSCAR DADOS DO GITHUB ---


@st.cache_data(ttl=3600)
def get_github_issues(repo_url):
    api_url = f"https://api.github.com/repos/{repo_url}/issues?state=open&per_page=100"
    headers = {}
    if "GITHUB_TOKEN" in st.secrets:
        headers["Authorization"] = f"token {st.secrets['GITHUB_TOKEN']}"
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao buscar vagas do GitHub: {e}")
        return None


def extract_labels(labels):
    label_html = ""
    for label in labels:
        label_html += f'<span class="label-tag">{label["name"]}</span>'
    return label_html

# --- FUNÇÃO PARA O DIÁLOGO ---


@st.dialog("Detalhes da Vaga")
def show_vaga_dialog(vaga):
    st.header(vaga['title'])
    st.markdown(extract_labels(vaga['labels']), unsafe_allow_html=True)
    st.markdown("---")
    body_snippet = textwrap.shorten(
        vaga['body'] if vaga['body'] else "Nenhuma descrição fornecida.",
        width=400,
        placeholder="..."
    )
    st.markdown(body_snippet)
    st.markdown("---")
    st.link_button("Ir para a vaga no GitHub ↗️", vaga['html_url'])
    if st.button("Fechar", key=f"close_{vaga['id']}"):
        st.session_state["dialog_vaga_id"] = None
        st.rerun()


# --- INTERFACE PRINCIPAL DA APLICAÇÃO ---
st.title("Quadro de Vagas 💼")
st.markdown(
    "Vagas de tecnologia publicadas como issues no GitHub. Fonte: `react-brasil/vagas`")

repo = "react-brasil/vagas"

with st.spinner(f"Buscando vagas mais recentes do repositório {repo}..."):
    vagas = get_github_issues(repo)

if vagas:
    search_query = st.text_input(
        "🔎 Buscar por título, tecnologia ou nível...",
        placeholder="Ex: React, Pleno, Remoto"
    )

    filtered_vagas = []
    if search_query:
        query = search_query.lower()
        for vaga in vagas:
            title_match = query in vaga['title'].lower()
            body_match = query in (
                vaga['body'].lower() if vaga['body'] else "")
            if title_match or body_match:
                filtered_vagas.append(vaga)
    else:
        filtered_vagas = vagas

    if not filtered_vagas:
        st.warning(f"Nenhuma vaga encontrada com o termo '{search_query}'.")
    else:
        st.markdown(f"**{len(filtered_vagas)} vagas encontradas.**")

        num_cols = 3
        cols = st.columns(num_cols)

        for index, vaga in enumerate(filtered_vagas):
            col = cols[index % num_cols]
            with col:
                with st.container(border=True):
                    st.subheader(vaga['title'], anchor=False)
                    labels_html = extract_labels(vaga['labels'])
                    st.markdown(labels_html, unsafe_allow_html=True)
                    st.markdown("---")
                    if st.button("Ver detalhes", key=f"btn_{vaga['id']}"):
                        st.session_state["dialog_vaga_id"] = vaga['id']
                        st.rerun()

        # Exibe o diálogo apenas para a vaga selecionada
        if "dialog_vaga_id" in st.session_state and st.session_state["dialog_vaga_id"] is not None:
            # Encontra a vaga correspondente ao ID armazenado
            selected_vaga = next(
                (vaga for vaga in filtered_vagas if vaga['id'] == st.session_state["dialog_vaga_id"]), None)
            if selected_vaga:
                show_vaga_dialog(selected_vaga)

    if "GITHUB_TOKEN" not in st.secrets:
        st.info(
            "Dica: Para evitar limites de requisição da API do GitHub, configure um "
            "[token de acesso pessoal](https://github.com/settings/tokens) e adicione-o ao "
            "arquivo `.streamlit/secrets.toml` como `GITHUB_TOKEN = 'seu_token_aqui'`."
        )
else:
    st.error("Não foi possível carregar as vagas. Verifique o nome do repositório ou sua conexão com a internet.")
