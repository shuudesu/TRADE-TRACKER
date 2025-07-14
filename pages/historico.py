import streamlit as st
import pandas as pd
from app.corretoras import Corretoras
from app.utils import formatar_moeda

def render(data_manager):
    """Renderiza a página de histórico de trades"""
    st.header("📋 Histórico de Trades")
    
    df = data_manager.obter_dataframe()
    
    if df.empty:
        st.warning("Nenhum trade cadastrado ainda.")
        return
    
    # Filtros
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filtro_ativo = st.text_input("Filtrar por ativo")
    
    with col2:
        opcoes_corretora = ["Todas"] + Corretoras.listar()
        filtro_corretora = st.selectbox("Filtrar por corretora", opcoes_corretora)
    
    with col3:
        todos_mercados = ["Todos"]
        if not df.empty and 'mercado' in df.columns:
            todos_mercados += df['mercado'].unique().tolist()
        filtro_mercado = st.selectbox("Filtrar por mercado", todos_mercados)
    
    # Aplicar filtros
    df_filtrado = df.copy() if not df.empty else pd.DataFrame()
    
    if not df.empty:
        if filtro_ativo:
            df_filtrado = df_filtrado[df_filtrado['ativo'].str.contains(filtro_ativo, case=False)]
        
        if filtro_corretora != "Todas" and 'corretora' in df_filtrado.columns:
            df_filtrado = df_filtrado[df_filtrado['corretora'] == filtro_corretora]
        
        if filtro_mercado != "Todos" and 'mercado' in df_filtrado.columns:
            df_filtrado = df_filtrado[df_filtrado['mercado'] == filtro_mercado]
    
    # Formatar colunas monetárias
    if not df_filtrado.empty:
        # Colunas para exibir
        colunas_display = ['ativo', 'data', 'direcao', 'quantidade', 
                           'valor_entrada', 'valor_saida', 'resultado', 
                           'corretora', 'tipo_operacao', 'mercado']
        
        df_display = df_filtrado[colunas_display].copy()
        
        # Estilizar com cores
        def highlight_resultado(val):
            if isinstance(val, (int, float)):
                return 'color: green' if val > 0 else 'color: red'
            return ''
        
        # Mostrar tabela formatada
        st.dataframe(
            df_display.style.applymap(
                highlight_resultado, 
                subset=['resultado']
            ),
            height=400
        )
    
        # Adicionar opção de exclusão
        st.subheader("Excluir Trade")
        
        indices = list(range(len(df)))
        indice_exclusao = st.selectbox("Selecione o índice do trade a ser excluído", indices)
        
        if st.button("Excluir Trade Selecionado"):
            if data_manager.excluir_trade(indice_exclusao):
                st.success(f"Trade {indice_exclusao} excluído com sucesso!")
                st.rerun()
            else:
                st.error("Erro ao excluir o trade.")