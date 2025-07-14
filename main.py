import streamlit as st
from app.data_manager import DataManager
import pages.cadastro as cadastro
import pages.historico as historico
import pages.dashboard as dashboard
import os

# Configuração da página
st.set_page_config(
    page_title="Trade Tracker",
    page_icon="📊",
    layout="wide"
)

# Carregar estilos customizados
def load_css():
    css_file = os.path.join(os.path.dirname(__file__), "assets", "styles.css")
    if os.path.exists(css_file):
        with open(css_file, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Inicializar gerenciador de dados
data_manager = DataManager()

def main():
    st.title("📈 Trade Tracker")
    
    # Menu de navegação
    menu = st.sidebar.selectbox(
        "Menu", 
        ["Cadastrar Trade", "Histórico de Trades", "Dashboard de Análise"]
    )
    
    # Informações na barra lateral
    st.sidebar.info("""
    **Trade Tracker**
    
    Controle seus trades e analise o desempenho.
    
    Versão 1.0.0
    """)
    
    # Renderizar página correspondente
    if menu == "Cadastrar Trade":
        cadastro.render(data_manager)
    elif menu == "Histórico de Trades":
        historico.render(data_manager)
    elif menu == "Dashboard de Análise":
        dashboard.render(data_manager)

if __name__ == "__main__":
    main()