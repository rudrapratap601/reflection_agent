# 🧠 Daily Reflection Tree Agent

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Architecture](https://img.shields.io/badge/Architecture-Deterministic-green)
![LLM](https://img.shields.io/badge/LLM-Not%20Used%20at%20Runtime-red)
![Interface](https://img.shields.io/badge/Interface-CLI-lightgrey)
![Status](https://img.shields.io/badge/Status-Complete-success)

---

## 📌 Overview

The **Daily Reflection Tree Agent** is a deterministic system that guides users through structured end-of-day reflection using a decision tree.

Unlike typical AI-based tools, this system:
- does **not rely on LLMs at runtime**
- produces **fully predictable and repeatable outputs**
- encodes psychological insights into a **structured decision tree**

---

## 🎯 Core Idea

Most systems capture *what happened*.

This system focuses on:
> **Why it happened and how the user reflects on it**

It transforms abstract psychological concepts into a **navigable, structured experience**, ensuring:
- consistency  
- clarity  
- zero hallucination  

---

## 🧩 How It Works

The agent walks the user through three psychological axes:

### 1. Axis 1 — Locus (Control)
- Internal vs External vs Mixed  
- Helps users identify where they had control  

### 2. Axis 2 — Orientation
- Contribution vs Entitlement  
- Shifts focus from *what I got* → *what I gave*  

### 3. Axis 3 — Radius
- Self vs Others  
- Expands perspective beyond self  

---

### ⚙️ Under the Hood

- Each answer updates **state signals**
- Signals determine **branching decisions**
- Reflections use **template-based interpolation**
- Same inputs → same outputs (**fully deterministic**)

---

## ⚙️ Key Features

- ✅ Fully deterministic decision tree  
- ✅ No LLM usage at runtime  
- ✅ State-based branching (signals)  
- ✅ Handles ambiguity using **mixed-state logic**  
- ✅ Human-like reflections (non-judgmental)  
- ✅ Input validation (robust CLI experience)  

---

## 🏗️ Project Structure

```
Reflection_Agent/
│
├── agent.py # Main CLI agent
├── reflection-tree.json # Decision tree (core logic)
├── Tree_Diagram.pdf # Visual tree diagram
├── write-up.pdf # Design explanation

```

---

## ▶️ How to Run

Make sure Python is installed, then run:

```bash
python agent.py

```

---

## 🌳 Tree Design
- Uses fixed options only (no free text input)
- Decision nodes:
  - Answer-based branching
  - State-based branching (Axis evaluation)
- Reflection nodes:
  - Use stored answers + signals
- Bridge nodes:
  - Smooth transition between axes
 
---

## 🧠 Design Philosophy
- Deterministic > Generative
- Structure > Guessing
- Reflection > Advice

The system behaves like a:

> **thoughtful colleague, not a chatbot**

---

## 👤 Author

Built as part of a **Decision Tree Knowledge Engineering Assignment**.

---

