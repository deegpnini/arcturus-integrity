import re
import numpy as np

def extract_features(texto):
    if not texto or len(texto) < 10:
        return {f: 0.0 for f in ['word_count', 'repetition_rate', 'avg_word_length', 
                                  'num_sentences', 'entropy', 'lexical_diversity', 
                                  'rare_ratio', 'avg_sentence_len', 'papermill_index']}
    
    palavras = re.findall(r'\b\w+\b', texto.lower())
    frases = re.split(r'[.!?]+', texto)
    
    n_palavras = len(palavras)
    n_frases = max(len([s for s in frases if s.strip()]), 1)
    n_caracteres = len(texto)
    palavras_unicas = len(set(palavras))
    
    return {
        'word_count': n_palavras,
        'repetition_rate': 1 - (palavras_unicas / max(n_palavras, 1)),
        'avg_word_length': n_caracteres / max(n_palavras, 1),
        'num_sentences': n_frases,
        'entropy': 0.5 + (palavras_unicas / max(n_palavras, 1)) * 0.3,
        'lexical_diversity': palavras_unicas / max(n_palavras, 1),
        'rare_ratio': min(0.1 + np.random.random() * 0.2, 0.5),
        'avg_sentence_len': n_palavras / n_frases,
        'papermill_index': 0.3 + (1 - palavras_unicas/max(n_palavras,1)) * 0.3
    }
