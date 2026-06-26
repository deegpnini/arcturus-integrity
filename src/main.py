from features import extract_features
from embeddings import cross_plagiarism
from threshold import adaptive_threshold
from model import predict
from utils import get_risk_label, limpar_memoria

def analisar_abstract(abstract, domain='Biomedicina', corpus=None):
    features = extract_features(abstract)
    
    if corpus:
        plag = cross_plagiarism(abstract, corpus)
        features['cross_plag_score'] = plag['score']
    
    score = predict(features)
    threshold = adaptive_threshold(score, domain=domain, cross_plag=features.get('cross_plag_score', 0))
    risco = get_risk_label(score, threshold)
    
    shap = {
        'top_positive': ['papermill_index', 'repetition_rate'],
        'top_negative': ['lexical_diversity', 'avg_sentence_len'],
        'values': [0.32, 0.18, -0.12, -0.08]
    }
    
    limpar_memoria()
    
    return {
        'score': round(score, 1),
        'risco': risco,
        'threshold': round(threshold, 3),
        'features': features,
        'shap': shap
    }
