# ARCTURUS — Scientific Integrity Screening

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21015524.svg)](https://doi.org/10.5281/zenodo.21015524)
[![Status](https://img.shields.io/badge/Status-v10.0%20(Ativo)-brightgreen)](https://github.com/deegpnini/arcturus-integrity)
[![License](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)

**ARCTURUS** é um sistema de triagem de integridade científica que detecta padrões de papermills em abstracts biomédicos com explicabilidade SHAP.

> "Tecnologia com alma, dados com propósito, código com coração."

---

## 📊 Resultados

| Métrica | Valor |
|---------|-------|
| AUC-ROC | 91.84% |
| Recall (Classe 1) | 87.21% |
| F1-Score | 84.81% |
| Threshold | 0.533 |
| Dataset | 699 artigos biomédicos |

### Validação com 8 casos controlados

| Abstract | Score | Classificação | Status |
|----------|-------|---------------|--------|
| Curcumina RCT | 22 | BAIXO RISCO | ✅ |
| Treino HF RCT | 18 | BAIXO RISCO | ✅ |
| Hidroxicloroquina | 82 | ALTO RISCO | ✅ |
| miR-21 Câncer | 52 | ZONA CINZENTA | ✅ |
| Quercetina | 72 | ALTO RISCO | ✅ |
| Probiótico SII | 22 | BAIXO RISCO | ✅ |
| HOTAIR Cólon | 52 | ZONA CINZENTA | ✅ |
| Bamlanivimab | 28 | BAIXO RISCO | ✅ |

**Acertos: 8/8 (100%)**

---

## 🚀 Como usar

### Demo online
https://deegpnini.github.io/arcturus-integrity/

---

## 📄 Publicação

- **DOI:** [10.5281/zenodo.21015524](https://doi.org/10.5281/zenodo.21015524)
- **Data:** 29 de Junho de 2026

---

## 📌 Limitações

- Modelo treinado apenas para biomedicina em inglês
- Viés conservador em subdomínios específicos (lncRNA/miRNA + tumor)
- Dataset de 699 artigos

---

## 👤 Autor

**Hebron (Helyton Renato Gonçalves Ronchi)**  
Balneário Rincão, SC — Brasil
