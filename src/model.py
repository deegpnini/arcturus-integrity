def predict(features):
    """Simula predição — substitua pelo seu modelo real"""
    score = (features.get('papermill_index', 0) * 60 + 
             features.get('repetition_rate', 0) * 30 + 
             (1 - features.get('lexical_diversity', 0.5)) * 10)
    return min(max(score, 5), 95)
