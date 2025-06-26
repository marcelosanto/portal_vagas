import streamlit as st
import requests
import textwrap
import datetime
import pytz
import re

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Vagas Tech Brasil",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ESTILOS CSS MODERNOS ---
st.markdown("""
<style>
    /* Importar Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Reset e configurações base */
    .main .block-container {
        padding-top: 2rem;
        max-width: 1200px;
    }
    
    /* Título principal */
    .main-title {
        font-family: 'Inter', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-family: 'Inter', sans-serif;
    }
    
    /* Grid de vagas */
    .vagas-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    /* Cards de vagas modernos */
    .vaga-card {
        background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
        height: fit-content;
        display: flex;
        flex-direction: column;
    }
    
    .vaga-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        border-color: #667eea;
    }
    
    .vaga-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #667eea, #764ba2);
    }
    
    /* Título da vaga */
    .vaga-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.25rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 0.75rem;
        line-height: 1.4;
    }
    
    /* Labels modernas */
    .label-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .label-tag {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.25rem 0.75rem;
        border-radius: 50px;
        font-size: 0.75rem;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
        box-shadow: 0 2px 4px rgba(102, 126, 234, 0.3);
        transition: all 0.2s ease;
    }
    
    .label-tag:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(102, 126, 234, 0.4);
    }
    
    /* Botões modernos */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px -1px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 15px -3px rgba(102, 126, 234, 0.4);
    }
    
    /* Input de busca */
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        padding: 0.75rem 1rem;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Stats container */
    .stats-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin: 1rem 0 2rem 0;
        box-shadow: 0 8px 15px -3px rgba(102, 126, 234, 0.4);
    }
    
    .stats-number {
        font-size: 2rem;
        font-weight: 700;
        font-family: 'Inter', sans-serif;
    }
    
    .stats-label {
        font-size: 0.9rem;
        opacity: 0.9;
        font-family: 'Inter', sans-serif;
    }
    
    /* Descrição da vaga */
    .vaga-description {
        color: #64748b;
        font-size: 0.9rem;
        line-height: 1.5;
        margin: 0.75rem 0 1rem 0;
        flex-grow: 1;
        font-family: 'Inter', sans-serif;
    }
    
    /* Container dos botões */
    .vaga-buttons {
        display: flex;
        gap: 0.5rem;
        margin-top: auto;
        padding-top: 1rem;
        border-top: 1px solid #e2e8f0;
    }
    
    .vaga-meta {
        font-size: 0.75rem;
        color: #94a3b8;
        margin-top: 0.5rem;
        font-family: 'Inter', sans-serif;
    }
    
    /* Loading spinner personalizado */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Info box */
    .info-box {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border: 1px solid #0ea5e9;
        border-radius: 12px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Responsividade */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        
        .vagas-grid {
            grid-template-columns: 1fr;
            gap: 1rem;
        }
        
        .vaga-card {
            padding: 1rem;
        }
        
        .vaga-buttons {
            flex-direction: column;
        }
        
        .vaga-buttons .stButton > button,
        .vaga-buttons .stLinkButton > a {
            flex: none;
        }
    }
    
    @media (max-width: 480px) {
        .main .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
        
        .vagas-grid {
            grid-template-columns: 1fr;
            gap: 0.75rem;
        }
        
        .vaga-card {
            padding: 0.75rem;
        }
        
        .label-container {
            gap: 0.25rem;
        }
        
        .label-tag {
            font-size: 0.7rem;
            padding: 0.2rem 0.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- CONFIGURAÇÃO DOS REPOSITÓRIOS ---
repos = [
    "react-brasil/vagas",
    "backend-br/vagas",
    "frontendbr/vagas",
    # Add more repositories as needed
]

# --- FUNÇÕES PARA BUSCAR DADOS DO GITHUB ---


@st.cache_data(ttl=1800)  # Cache de 30 minutos
def get_github_issues_from_repos(repos):
    """Busca issues de múltiplos repositórios do GitHub sem necessidade de token."""
    all_issues = []
    seen = set()  # Track unique (title, created_at) pairs to avoid duplicates
    for repo in repos:
        api_url = f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100"
        try:
            response = requests.get(api_url, timeout=10)
            if response.status_code == 403:
                st.warning(
                    f"⚠️ Limite de requisições atingido para {repo}. Tente novamente em alguns minutos.")
                continue
            response.raise_for_status()
            issues = response.json()
            for issue in issues:
                if 'pull_request' not in issue:
                    key = (issue['title'], issue['created_at'])
                    if key not in seen:
                        seen.add(key)
                        all_issues.append({**issue, "source_repo": repo})
        except requests.exceptions.Timeout:
            st.error(
                f"⏱️ Timeout na requisição para {repo}. Verifique sua conexão.")
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Erro ao buscar vagas de {repo}: {e}")
    return all_issues


def extract_labels(labels):
    """Extrai e formata as labels das vagas."""
    if not labels:
        return '<div class="label-container"><span class="label-tag" style="background: #667eea;">Sem tags</span></div>'
    label_html = '<div class="label-container">'
    for label in labels[:5]:  # Limit to 5 labels
        color = label.get('color', '667eea')
        name = label.get('name', 'Sem nome')
        label_html += f'<span class="label-tag" style="background: #{color};">{name}</span>'
    label_html += '</div>'
    return label_html


def format_date(date_string):
    """Formata a data de criação da vaga."""
    try:
        date_obj = datetime.datetime.fromisoformat(
            date_string.replace('Z', '+00:00'))
        return date_obj.strftime('%d/%m/%Y')
    except:
        return "Data não disponível"


def extract_description(body, max_length=150):
    """Extrai uma breve descrição do início do body da vaga."""
    if not body:
        return "Descrição não disponível."
    clean_text = re.sub(r'https?://\S+', '', body)  # Remove URLs
    clean_text = re.sub(r'[#*`\[\]()]', '', clean_text)  # Remove markdown
    clean_text = re.sub(r'\n+', ' ', clean_text)  # Replace newlines
    clean_text = clean_text.strip()
    if not clean_text:
        return "Descrição não disponível."
    if len(clean_text) <= max_length:
        return clean_text
    truncated = clean_text[:max_length].rsplit(' ', 1)[0]
    return f"{truncated}..."


def extract_company_from_title(title):
    """Extrai o nome da empresa do título da vaga."""
    match = re.match(r'\[(.*?)\]\s*(.*?-)?\s*(.*?)$', title)
    if match:
        prefix, _, company = match.groups()
        return company.strip() if company else prefix.strip()
    return None


def create_vaga_card(vaga):
    """Gera o HTML para o card de uma vaga."""
    title = vaga.get('title', 'Título não disponível')
    description = extract_description(vaga.get('body', ''))
    labels = extract_labels(vaga.get('labels', []))
    created_at = format_date(vaga.get('created_at', ''))
    company = extract_company_from_title(title) or "Empresa não especificada"
    user = vaga.get('user', {}).get('login', 'Usuário não especificado')
    source_repo = vaga.get('source_repo', 'Repositório desconhecido')

    card_html = f"""
    <div class="vaga-card">
        <div class="vaga-title">{title}</div>
        <div class="vaga-meta">🏢 {company}</div>
        <div class="vaga-meta">📂 Repositório: {source_repo}</div>
        {labels}
        <div class="vaga-description">{description}</div>
        <div class="vaga-meta">📅 Publicado em: {created_at}</div>
        <div class="vaga-meta">👤 Por: {user}</div>
    </div>
    """
    return card_html

# --- FUNÇÃO PARA O DIÁLOGO MELHORADO ---


@st.dialog("📋 Detalhes da Vaga")
def show_vaga_dialog(vaga):
    st.markdown('<div class="dialog-content">', unsafe_allow_html=True)
    company = extract_company_from_title(vaga['title'])
    if company:
        st.markdown(f"**🏢 {company}**")
    st.markdown(f"## {vaga['title']}")
    if vaga['labels']:
        st.markdown(extract_labels(vaga['labels']), unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"**📅 Publicada em:** {format_date(vaga['created_at'])}")
    with col2:
        st.markdown(f"**👤 Por:** {vaga['user']['login']}")
    st.markdown("---")
    if vaga['body']:
        description = textwrap.shorten(
            vaga['body'], width=800, placeholder="...")
        st.markdown("**📝 Descrição:**")
        st.markdown(description)
    else:
        st.info("ℹ️ Nenhuma descrição detalhada fornecida.")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🔗 Ver vaga completa no GitHub", vaga['html_url'])
    with col2:
        if st.button("❌ Fechar", key=f"close_{vaga['id']}_{vaga['source_repo']}"):
            st.session_state["dialog_vaga_id"] = None
            st.session_state["dialog_vaga_repo"] = None
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


# --- INTERFACE PRINCIPAL ---
st.markdown('<h1 class="main-title">🚀 Vagas Tech Brasil</h1>',
            unsafe_allow_html=True)
st.markdown('<p class="subtitle">Encontre as melhores oportunidades em tecnologia</p>',
            unsafe_allow_html=True)

# Buscar vagas
with st.spinner("🔍 Buscando as vagas mais recentes..."):
    vagas = get_github_issues_from_repos(repos)

if vagas:
    st.markdown(f'''
    <div class="stats-container">
        <div class="stats-number">{len(vagas)}</div>
        <div class="stats-label">vagas disponíveis</div>
    </div>
    ''', unsafe_allow_html=True)

    # Busca
    search_query = st.text_input(
        "",
        placeholder="🔎 Buscar por cargo, empresa, tecnologia ou nível (ex: React, Pleno, Remoto)...",
        key="search_input"
    )

    # Filtros
    col1, col2, col3 = st.columns(3)
    with col1:
        show_recent = st.checkbox(
            "📅 Apenas vagas recentes (últimos 30 dias)", value=False)
    with col2:
        show_with_description = st.checkbox(
            "📝 Apenas com descrição detalhada", value=False)
    with col3:
        selected_repos = st.multiselect(
            "📂 Filtrar por repositório",
            options=repos,
            default=repos,
            key="repo_filter"
        )

    # Aplicar filtros
    filtered_vagas = vagas.copy()
    if selected_repos:
        filtered_vagas = [
            vaga for vaga in filtered_vagas if vaga["source_repo"] in selected_repos]
    if search_query:
        query = search_query.lower()
        filtered_vagas = [
            vaga for vaga in filtered_vagas
            if (query in vaga['title'].lower() or
                query in (vaga['body'].lower() if vaga['body'] else "") or
                any(query in label['name'].lower() for label in vaga['labels']))
        ]
    if show_recent:
        thirty_days_ago = datetime.datetime.now(
            pytz.UTC) - datetime.timedelta(days=30)
        filtered_vagas = [
            vaga for vaga in filtered_vagas
            if datetime.datetime.fromisoformat(vaga['created_at'].replace('Z', '+00:00')) > thirty_days_ago
        ]
    if show_with_description:
        filtered_vagas = [
            vaga for vaga in filtered_vagas
            if vaga['body'] and len(vaga['body'].strip()) > 50
        ]

    # Resultados
    if not filtered_vagas:
        st.warning("🔍 Nenhuma vaga encontrada com os filtros aplicados.")
        st.info("💡 Tente ajustar os termos de busca ou remover alguns filtros.")
    else:
        st.markdown(f"**✨ {len(filtered_vagas)} vaga(s) encontrada(s)**")
        st.markdown('<div class="vagas-grid">', unsafe_allow_html=True)
        num_cols = 3
        cols = st.columns(num_cols)
        for index, vaga in enumerate(filtered_vagas):
            col = cols[index % num_cols]
            with col:
                card_html = create_vaga_card(vaga)
                st.markdown(card_html, unsafe_allow_html=True)
                st.markdown('<div class="vaga-buttons">',
                            unsafe_allow_html=True)
                button_col1, button_col2 = st.columns(2)
                with button_col1:
                    if st.button("👁️ Detalhes", key=f"btn_{vaga['id']}_{vaga['source_repo']}", use_container_width=True):
                        st.session_state["dialog_vaga_id"] = vaga['id']
                        st.session_state["dialog_vaga_repo"] = vaga['source_repo']
                        st.rerun()
                with button_col2:
                    st.link_button(
                        "🔗 GitHub", vaga['html_url'], use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Diálogo
    if "dialog_vaga_id" in st.session_state and st.session_state["dialog_vaga_id"] is not None:
        selected_vaga = next(
            (vaga for vaga in filtered_vagas if vaga['id'] == st.session_state["dialog_vaga_id"]
             and vaga['source_repo'] == st.session_state["dialog_vaga_repo"]),
            None
        )
        if selected_vaga:
            show_vaga_dialog(selected_vaga)

    # Info sobre limites da API
    st.markdown('''
    <div class="info-box">
        <strong>ℹ️ Informação:</strong> Este app usa a API pública do GitHub sem autenticação. 
        Em caso de muitos acessos simultâneos, pode haver limitação temporária de requisições.
    </div>
    ''', unsafe_allow_html=True)

else:
    st.error(
        "❌ Não foi possível carregar as vagas. Tente novamente em alguns minutos.")
    st.info(
        "💡 Isso pode acontecer devido a limites da API do GitHub ou problemas de conexão.")

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #6b7280; font-family: Inter, sans-serif;">',
    unsafe_allow_html=True
)
repo_links = ", ".join(
    [f'<a href="https://github.com/{repo}">{repo}</a>' for repo in repos])
st.markdown(
    f"💼 Dados atualizados dos repositórios: {repo_links}", unsafe_allow_html=True)
st.markdown("</p>", unsafe_allow_html=True)
