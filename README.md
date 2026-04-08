# 📧 Email Triage Environment

**Team:** IgniteX  
**Hackathon:** Meta PyTorch OpenEnv Hackathon x SST 2026

---

## 🌍 What is this?

An OpenEnv-compliant environment where an AI agent learns
to triage (sort and categorize) emails — just like a real
company employee would do every day.

The agent reads emails and must correctly classify them by:
- **Category** → spam / urgent / normal / support
- **Urgency** → low / medium / high
- **Department** → technical / finance / hr / admin / operations / management / none

---

## 🎯 Tasks

### 🟢 Easy — Spam Detection
- **Goal:** Classify emails as spam or not spam
- **Emails:** 4 emails
- **Scoring:** 1.0 = correct, 0.0 = wrong
- **Expected Score:** 0.7 – 1.0

### 🟡 Medium — Category + Urgency
- **Goal:** Classify category AND judge urgency level
- **Emails:** 5 emails
- **Scoring:** 0.6 (category) + 0.2 (urgency) = max 0.8
- **Expected Score:** 0.4 – 0.7

### 🔴 Hard — Category + Urgency + Department
- **Goal:** Classify category, urgency AND assign department
- **Emails:** 6 emails
- **Scoring:** 0.6 + 0.2 + 0.2 = max 1.0
- **Expected Score:** 0.3 – 0.6

---

## 👁️ Observation Space

What the AI sees for each email:

| Field | Type | Description |
|---|---|---|
| email_id | int | Unique email number |
| subject | str | Email subject line |
| body | str | Email content |
| sender | str | Who sent it |
| task_level | str | easy / medium / hard |
| emails_remaining | int | How many emails left |

---

## 🎮 Action Space

What the AI can do:

| Field | Type | Description |
|---|---|---|
| email_id | int | Which email it's answering |
| category | str | spam / urgent / normal / support |
| urgency | str (optional) | low / medium / high |
| department | str (optional) | technical / finance / hr / admin / operations / management / none |

---

## 🏆 Reward Function

| Correct | Score |
|---|---|
| Category correct | +0.6 |
| Urgency correct | +0.2 |
| Department correct | +0.2 |
| Everything wrong | 0.0 |

---

## 📊 Baseline Scores

Scores achieved by GPT-3.5-turbo baseline agent:

| Task | Score |
|---|---|
| 🟢 Easy | ~0.75 |
| 🟡 Medium | ~0.50 |
| 🔴 Hard | ~0.35 |

---

## 🚀 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/email-triage-env
cd email-triage-env
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the environment
```bash
python app.py
```

### 4. Run baseline inference
```bash
export OPENAI_API_KEY=your_key_here
export API_BASE_URL=https://api.openai.com/v1
export MODEL_NAME=gpt-3.5-turbo
python inference.py
```

### 5. Run with Docker
```bash
docker build -t email-triage-env .
docker run -p 7860:7860 email-triage-env
```

---

## 📁 Project Structure
