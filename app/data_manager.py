import os
import json
import pandas as pd

class DataManager:
    def __init__(self, data_file='data/trades_data.json'):
        self.data_file = data_file
        
        # Cria diretório de dados se não existir
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        
        # Inicializa o arquivo se não existir
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w') as f:
                json.dump([], f)
    
    def carregar_trades(self):
        """Carrega os trades do arquivo"""
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def salvar_trades(self, trades):
        """Salva os trades no arquivo"""
        with open(self.data_file, 'w') as f:
            json.dump(trades, f)
    
    def adicionar_trade(self, trade):
        """Adiciona um novo trade"""
        trades = self.carregar_trades()
        trades.append(trade)
        self.salvar_trades(trades)
    
    def excluir_trade(self, index):
        """Exclui um trade pelo índice"""
        trades = self.carregar_trades()
        if 0 <= index < len(trades):
            del trades[index]
            self.salvar_trades(trades)
            return True
        return False
    
    def obter_dataframe(self):
        """Retorna os trades como um DataFrame pandas"""
        trades = self.carregar_trades()
        if not trades:
            return pd.DataFrame()
        return pd.DataFrame(trades)