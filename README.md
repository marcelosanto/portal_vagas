
# 🚀 Portal Vagas

**Portal Vagas** é uma aplicação web moderna construída com **Streamlit** que agrega vagas de tecnologia de repositórios GitHub, como `react-brasil/vagas`, `backend-br/vagas`, e outros. Com uma interface amigável, filtros avançados e visualização detalhada, o Portal Vagas facilita a busca por oportunidades em tecnologia no Brasil. Explore vagas recentes, filtre por palavras-chave ou repositórios, e acesse detalhes diretamente do GitHub!

![Portal Vagas Link](https://via.placeholder.com/800x400.png?text=Portal+Vagas+Screenshot)  
- [Acessar o Link](https://app-vagas-do-git.streamlit.app/)

----------

## 📋 Índice

-   [Sobre o Projeto](https://grok.com/chat/261432da-ba66-4b60-89f3-fb270fcd09a3#sobre-o-projeto)
-   [Funcionalidades](https://grok.com/chat/261432da-ba66-4b60-89f3-fb270fcd09a3#funcionalidades)
-   [Tecnologias Utilizadas](https://grok.com/chat/261432da-ba66-4b60-89f3-fb270fcd09a3#tecnologias-utilizadas)
-   [Como Usar](https://grok.com/chat/261432da-ba66-4b60-89f3-fb270fcd09a3#como-usar)
    -   [Pré-requisitos](https://grok.com/chat/261432da-ba66-4b60-89f3-fb270fcd09a3#pr%C3%A9-requisitos)
    -   [Instalação](https://grok.com/chat/261432da-ba66-4b60-89f3-fb270fcd09a3#instala%C3%A7%C3%A3o)
    -   [Execução](https://grok.com/chat/261432da-ba66-4b60-89f3-fb270fcd09a3#execu%C3%A7%C3%A3o)
-   [Estrutura do Projeto](https://grok.com/chat/261432da-ba66-4b60-89f3-fb270fcd09a3#estrutura-do-projeto)
-   [Contribuindo](https://grok.com/chat/261432da-ba66-4b60-89f3-fb270fcd09a3#contribuindo)
-   [Licença](https://grok.com/chat/261432da-ba66-4b60-89f3-fb270fcd09a3#licen%C3%A7a)
-   [Contato](https://grok.com/chat/261432da-ba66-4b60-89f3-fb270fcd09a3#contato)

----------

## 📖 Sobre o Projeto

O **Portal Vagas** foi criado para centralizar e facilitar o acesso a vagas de tecnologia publicadas como issues em repositórios GitHub, como `react-brasil/vagas` e `backend-br/vagas`. A aplicação permite buscar, filtrar e visualizar vagas de forma intuitiva, com suporte a filtros por repositório, data de publicação (últimos 30 dias), e descrição detalhada. É ideal para desenvolvedores que desejam encontrar oportunidades no mercado brasileiro de tecnologia.

**Objetivo**: Tornar a busca por vagas mais eficiente, com uma interface moderna e filtros úteis, enquanto aproveita a transparência das issues do GitHub.

----------

## ✨ Funcionalidades

-   **Busca por palavras-chave**: Pesquise vagas por cargo, empresa, tecnologia ou nível (ex.: "React", "Pleno", "Remoto").
-   **Filtros avançados**:
    -   Mostrar apenas vagas dos últimos 30 dias.
    -   Exibir vagas com descrições detalhadas.
    -   Filtrar por repositórios específicos (ex.: `react-brasil/vagas`, `backend-br/vagas`).
-   **Visualização de vagas**: Cards modernos com título, empresa, descrição resumida, data de publicação, autor e repositório de origem.
-   **Detalhes em modal**: Visualize informações completas de uma vaga em um diálogo interativo.
-   **Integração com GitHub**: Links diretos para as issues originais no GitHub.
-   **Design responsivo**: Interface adaptável para desktop e mobile.
-   **Cache de dados**: Usa `@st.cache_data` para otimizar a performance ao buscar vagas.

----------

## 🛠 Tecnologias Utilizadas

-   **Python 3.8+**: Linguagem principal do projeto.
-   **Streamlit**: Framework para a interface web interativa.
-   **Requests**: Para chamadas à API do GitHub.
-   **Pytz**: Para manipulação de fusos horários.
-   **Markdown/HTML/CSS**: Para estilização e formatação dos cards e interface.
-   **GitHub API**: Para buscar issues de vagas dos repositórios.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red) ![GitHub](https://img.shields.io/badge/GitHub-API-lightgrey)

----------

## 🚀 Como Usar

### Pré-requisitos

-   **Python 3.8+**: Certifique-se de ter o Python instalado. [Baixe aqui](https://www.python.org/downloads/).
-   **Pip**: Gerenciador de pacotes do Python.
-   **Git**: Para clonar o repositório. [Baixe aqui](https://git-scm.com/downloads).
-   Conexão com a internet para acessar a API do GitHub.

### Instalação

1.  Clone o repositório:
    
    ```bash
    git clone https://github.com/marcelosanto/portal_vagas.git
    cd portal_vagas
    
    ```
    
2.  Crie um ambiente virtual (opcional, mas recomendado):
    
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    
    ```
    
3.  Instale as dependências:
    
    ```bash
    pip install streamlit requests pytz
    
    ```
    

### Execução

1.  Execute a aplicação com Streamlit:
    
    ```bash
    streamlit run src/portal_vagas/app.py
    
    ```
    
2.  Abra o navegador em `http://localhost:8501` para acessar o Portal Vagas.
    
3.  Explore as vagas, use os filtros e clique em "Detalhes" ou "GitHub" para mais informações.
    

----------

## 📂 Estrutura do Projeto

```plaintext
portal_vagas/
├── src/
│   └── portal_vagas/
│       └── app.py         # Código principal da aplicação
├── README.md             # Documentação do projeto
├── requirements.txt      # Dependências do projeto
└── .gitignore            # Arquivos ignorados pelo Git

```

-   **`app.py`**: Contém a lógica da aplicação, incluindo busca de vagas, filtros e renderização da interface.
-   **`requirements.txt`**: Lista de dependências para facilitar a instalação.

----------

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir com o **Portal Vagas**, siga os passos abaixo:

1.  Faça um fork do repositório.
2.  Crie uma branch para sua feature:
    
    ```bash
    git checkout -b feature/nova-funcionalidade
    
    ```
    
3.  Commit suas alterações:
    
    ```bash
    git commit -m "Adiciona nova funcionalidade"
    
    ```
    
4.  Envie para o repositório remoto:
    
    ```bash
    git push origin feature/nova-funcionalidade
    
    ```
    
5.  Abra um Pull Request no GitHub.

Por favor, leia o [CONTRIBUTING.md](https://grok.com/chat/CONTRIBUTING.md) (em breve) para diretrizes detalhadas. Sugestões de melhorias:

-   Adicionar novos repositórios de vagas.
-   Melhorar os filtros ou a interface.
-   Otimizar a performance da busca.

----------

## 📜 Licença

Este projeto está licenciado sob a [MIT License](https://grok.com/chat/LICENSE). Veja o arquivo `LICENSE` para mais detalhes.

----------

## 📬 Contato

Desenvolvido por **Marcelo Santo**

-   GitHub: [marcelosanto](https://github.com/marcelosanto)
-   Email: rocha.mer21@gmail.com
-    LinkedIn: https://www.linkedin.com/in/marcelo-rochaa

Se você gostou do projeto, deixe uma ⭐ no repositório! Para sugestões ou problemas, abra uma [issue](https://github.com/marcelosanto/portal_vagas/issues).

----------

💼 **Fontes de Vagas**:

-   [react-brasil/vagas](https://github.com/react-brasil/vagas)
-   [backend-br/vagas](https://github.com/backend-br/vagas)
-   [frontendbr/vagas](https://github.com/frontendbr/vagas)
