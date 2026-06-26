import numpy as np

def adaptive_threshold(score, domain='Biomedicina', cross_plag=0, journal_impact=0):
    base = 0.68
    domain_adj = {'Biomedicina': 0.08, 'default': 0.03}.get(domain, 0.03)
    plag_penalty = 0.05 if cross_plag > 75 else 0
    journal_bonus = -0.05 if journal_impact > 3.0 else 0.05 if journal_impact < 1.0 else 0
    
    final = base + domain_adj - plag_penalty + journal_bonus
    return np.clip(final, 0.55, 0.85)
