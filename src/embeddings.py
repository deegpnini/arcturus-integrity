from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

MODEL = None

def get_model():
    global MODEL
    if MODEL is None:
        MODEL = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    return MODEL

def cross_plagiarism(abstract, corpus, batch_size=32):
    if not corpus:
        return {'score': 0, 'risk': 'Baixo'}
    
    model = get_model()
    new_emb = model.encode([abstract], convert_to_numpy=True)
    
    scores = []
    for i in range(0, len(corpus), batch_size):
        batch = corpus[i:i+batch_size]
        batch_embs = model.encode(batch, convert_to_numpy=True)
        sim = cosine_similarity(new_emb, batch_embs)[0]
        scores.extend(sim)
    
    max_score = max(scores) * 100
    risk = 'Alto' if max_score > 75 else 'Médio' if max_score > 55 else 'Baixo'
    
    return {'score': round(max_score, 1), 'risk': risk}
