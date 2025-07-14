class Corretoras:
    # Lista de corretoras com suas taxas
    corretoras = {
        'Clear': {
            'taxa_acoes': 0.0, 
            'taxa_day_trade': 0.0, 
            'taxa_emolumentos': 0.03/100
        },
        'XP': {
            'taxa_acoes': 0.0099/100, 
            'taxa_day_trade': 0.0099/100, 
            'taxa_emolumentos': 0.03/100
        },
        'Rico': {
            'taxa_acoes': 0.005/100, 
            'taxa_day_trade': 0.005/100, 
            'taxa_emolumentos': 0.03/100
        },
        'Nuinvest': {
            'taxa_acoes': 0.0, 
            'taxa_day_trade': 0.0, 
            'taxa_emolumentos': 0.03/100
        },
        'BTG Pactual': {
            'taxa_acoes': 0.0, 
            'taxa_day_trade': 0.0, 
            'taxa_emolumentos': 0.03/100
        },
        'Modal Mais': {
            'taxa_acoes': 0.0, 
            'taxa_day_trade': 0.0, 
            'taxa_emolumentos': 0.03/100
        },
    }
    
    @classmethod
    def listar(cls):
        """Retorna a lista de nomes de corretoras"""
        return list(cls.corretoras.keys())
    
    @classmethod
    def calcular_taxa(cls, corretora, tipo_operacao, valor_operacao):
        """Calcula a taxa conforme a corretora e o tipo de operação"""
        if corretora not in cls.corretoras:
            return 0.0
        
        if tipo_operacao == 'Day Trade':
            return valor_operacao * cls.corretoras[corretora]['taxa_day_trade'] + valor_operacao * cls.corretoras[corretora]['taxa_emolumentos']
        else:  # Swing Trade
            return valor_operacao * cls.corretoras[corretora]['taxa_acoes'] + valor_operacao * cls.corretoras[corretora]['taxa_emolumentos']