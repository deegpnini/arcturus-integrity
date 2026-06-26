import gc

def limpar_memoria():
    gc.collect()

def get_risk_label(score, threshold):
    if score/100 > threshold:
        return '🔴 ALTO'
    elif score/100 > threshold * 0.85:
        return '🟡 MÉDIO'
    else:
        return '🟢 BAIXO'
