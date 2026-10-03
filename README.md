# RAKSHA 🛡️

RAKSHA is an investor-safety prototype for the SANGYAN Investor Resilience Hackathon.

## What it does

A user can paste a financial message/claim, enter a URL, or upload a screenshot. RAKSHA performs an explainable safety screening for patterns such as:

- guaranteed/fixed returns
- urgency and pressure
- payment-before-verification requests
- Telegram/WhatsApp redirection
- regulatory impersonation/claims
- OTP/password/remote-access requests

It then explains the detected warning signs and provides safe next steps.

> RAKSHA does **not** provide stock tips, buy/sell/hold signals, price predictions, or personalized investment recommendations.

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

### Screenshot OCR

The screenshot feature uses Tesseract OCR. Install Tesseract separately for your operating system if you want OCR enabled. The app still works with pasted text without it.

## Project structure

```text
RAKSHA/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
└── raksha/
    ├── analyzer.py
    ├── ocr.py
    └── ui.py
```

## Roadmap for hackathon MVP

1. Add trusted-source verification adapters.
2. Add multilingual voice input/output.
3. Add evidence extraction and incident/recovery workflow.
4. Add optional LLM explanation layer with strict non-advisory guardrails.
5. Add test cases and evaluation dataset.

## Public-good principle

The system is designed to help investors pause, understand warning signs, verify claims, and act safely rather than tell them what to buy.
