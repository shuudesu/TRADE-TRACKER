import datetime
import pandas as pd

def calcular_resultado(quantidade, valor_entrada, valor_saida, taxas):
    """Calcula o resultado de uma operação"""
    valor_total_entrada = quantidade * valor_entrada
    valor_total_saida = quantidade * valor_saida
    resultado = valor_total_saida - valor_total_entrada - taxas
    
    return {
        'valor_total_entrada': valor_total_entrada,
        'valor_total_saida': valor_total_saida,
        'resultado': resultado,
        'resultado_percentual': (resultado / valor_total_entrada) * 100 if valor_total_entrada > 0 else 0
    }

def formatar_moeda(valor):
    """Formata um valor para exibição em moeda brasileira"""
    return f"R$ {valor:.2f}"

def calcular_estatisticas(df):
    """Calcula as estatísticas para o dashboard"""
    if df.empty:
        return {
            'resultado_total': 0,
            'trades_lucrativos': 0,
            'trades_perdedores': 0,
            'taxa_acerto': 0,
            'media_ganhos': 0,
            'media_perdas': 0,
            'maior_ganho': 0,
            'maior_perda': 0,
            'fator_lucro': 0,
            'expectativa': 0
        }
    
    resultado_total = df['resultado'].sum()
    trades_lucrativos = len(df[df['resultado'] > 0])
    trades_perdedores = len(df[df['resultado'] <= 0])
    taxa_acerto = trades_lucrativos / len(df) * 100 if len(df) > 0 else 0
    
    media_ganhos = df[df['resultado'] > 0]['resultado'].mean() if len(df[df['resultado'] > 0]) > 0 else 0
    media_perdas = df[df['resultado'] < 0]['resultado'].mean() if len(df[df['resultado'] < 0]) > 0 else 0
    
    maior_ganho = df['resultado'].max() if not df.empty else 0
    maior_perda = df['resultado'].min() if not df.empty else 0
    
    if media_perdas != 0:
        fator_lucro = abs(media_ganhos / media_perdas) if media_perdas != 0 else 0
    else:
        fator_lucro = float('inf') if media_ganhos > 0 else 0
    
    expectativa = (media_ganhos * taxa_acerto/100) + (media_perdas * (100-taxa_acerto)/100)
    
    return {
        'resultado_total': resultado_total,
        'trades_lucrativos': trades_lucrativos,
        'trades_perdedores': trades_perdedores,
        'taxa_acerto': taxa_acerto,
        'media_ganhos': media_ganhos,
        'media_perdas': media_perdas,
        'maior_ganho': maior_ganho,
        'maior_perda': maior_perda,
        'fator_lucro': fator_lucro,
        'expectativa': expectativa
    }