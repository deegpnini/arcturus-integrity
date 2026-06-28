# arcturus-integrity
Sistema de Detecção de Integridade Científica — UMAP + XGBoost + SHAP
# ARCTURUS — Scientific Integrity Screening

![Status](https://img.shields.io/badge/Status-v8.0%20(Ativo)-brightgreen)
![AUC](https://img.shields.io/badge/AUC-90.88%25-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

**ARCTURUS** é um sistema de triagem e detecção de anomalias em artigos científicos, focado em identificar padrões característicos de *papermills* e má conduta acadêmica. Desenvolvido com transparência radical, features interpretáveis e explicabilidade via SHAP.

> "Tecnologia com alma, dados com propósito, código com coração."

---

## 🎯 Sobre o Projeto

**ARCTURUS** combina engenharia de features manuais, embeddings multilíngues, UMAP e XGBoost para oferecer uma ferramenta acessível, auditável e de alto recall para editores, revisores e instituições.

- **Versão atual**: v8.0
- **Dataset**: 497 amostras (100 casos suspeitos + 397 controles)
- **AUC-ROC**: **90.88%**
- **Recall (Classe 1)**: **75%**
- **Acurácia**: **88%**
- **Threshold**: **0.35**

---

## ✨ Principais Funcionalidades

- Interface HTML com **7 domínios** (Biomedicina validada + 6 demos)
- **Radar giratório** animado
- Detecção baseada em 9 features estruturais e semânticas
- **Explicabilidade SHAP** completa (contribuição por feature)
- Threshold adaptativo por domínio
- Totalmente executável no Google Colab
- Código aberto e replicável

---

## 🏗️ Arquitetura

### Features (9)
1. `word_count`
2. `repetition_rate`
3. `avg_word_length`
4. `num_sentences`
5. `entropy`
6. `lexical_diversity`
7. `rare_ratio`
8. `avg_sentence_len`
9. `papermill_index` (feature central)

### Modelo
- **Embeddings**: Sentence-Transformers (multilíngue)
- **Redução**: UMAP (384 → 32)
- **Classificação**: XGBoost com `scale_pos_weight`
- **Balanceamento**: BorderlineSMOTE
- **Explicabilidade**: SHAP (TreeExplainer)

### Fontes de Dados
- OpenAlex, Crossref, PubMed
- SciELO / BDTD (em expansão para português)

---

## 📊 Resultados Atuais

| Métrica              | Valor                  |
|----------------------|------------------------|
| AUC-ROC              | 90.88%                 |
| Acurácia             | 88%                    |
| Recall (Classe 1)    | 75%                    |
| Threshold            | 0.35                   |
| Dataset              | 497 amostras           |

### Validação Externa

| Abstract | Score | Classificação |
|----------|-------|---------------|
| USP (legítimo) | 1.3/100 | 🟢 BAIXO |
| COVID-19 (legítimo) | 14.8/100 | 🟢 BAIXO |
| Câncer (legítimo) | 1.3/100 | 🟢 BAIXO |
| Papermill (simulado) | 72.6/100 | 🔴 ALTO |

**Separação de +66 pontos** entre legítimos e suspeitos.

---

## 🚀 Como Usar

### 1. Demo Interativa (recomendado)

Abra o HTML diretamente:
🔗 [ARCTURUS v8.0 — Demo](https://deegpnini.github.io/arcturus-integrity/ARCTURUS_v70_multi_dominio.html)

### 2. Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deegpnini/arcturus-integrity)

### 3. Instalação Local

```bash
git clone https://github.com/deegpnini/arcturus-integrity.git
cd arcturus-integrity
pip install -r requirements.txt
