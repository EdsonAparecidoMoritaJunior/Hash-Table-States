# 🧠 Tabela Hash com Listas Encadeadas
[![Licença: MIT](https://img.shields.io/badge/Licença-MIT-amarelo.svg)](LICENSE)

[🇺🇸 Read in English](README.md)

Este projeto demonstra uma **Tabela Hash com Endereçamento em Cadeia**, onde cada posição da tabela é uma **lista encadeada simples**.  
Foi originalmente criado para registrar estados brasileiros com base em suas siglas (2 letras), mas pode ser facilmente adaptado para outras finalidades como regiões, departamentos ou códigos de produtos.

---

## 📌 Funcionalidades

- Tabela hash com 10 posições (índices de 0 a 9)
- Lista encadeada simples em cada posição para tratar colisões
- Função hash personalizada:
  - `"DF"` (Distrito Federal) sempre retorna a posição 7
  - Outras siglas: `(ASCII(letra1) + ASCII(letra2)) % 10`
- Inserção manual via menu no terminal
- Exibição completa da tabela por posição

---

## ⚙️ Exemplos de Uso

Apesar de ter sido criado para estados brasileiros, o sistema pode ser facilmente adaptado para:
- Estados ou províncias de outros países
- Departamentos em empresas
- Classificação de produtos ou usuários por código
