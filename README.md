# 🧠 Hash Table with Linked Lists
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[🇧🇷 Leia em Português](README-pt.md)

This project demonstrates a simple **Hash Table with Separate Chaining**, where each bucket is a **singly linked list**.  
Originally designed to register Brazilian states using their 2-letter abbreviations, the system is fully adaptable to other use cases such as regions, departments, or product codes.

---

## 📌 Key Features

- Hash table with 10 positions (indexes 0–9)
- Singly linked list at each position to handle collisions
- Custom hash function:
  - `"DF"` (Federal District) always returns index 7
  - Other keys: `(ASCII(letter1) + ASCII(letter2)) % 10`
- Manual entry via command-line menu
- Full table display by index

---

## ⚙️ Example Use Cases

Although this project was created for Brazilian states, it can be easily adapted for:
- US states or provinces
- Departments within companies
- Categorizing products or users by code
