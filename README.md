# Crypto API

API en Python avec FastAPI pour récupérer les prix des cryptomonnaies et le top 10 du marché.

## Endpoints

- / : page d'accueil
- /crypto/{coin}` : informations sur une crypto spécifique (ex : bitcoin)
- /top : top 10 des cryptos par capitalisation

## Installation

bash
pip install fastapi uvicorn requests

python -m uvicorn main:app --reload

Exemple

GET /crypto/bitcoin renvoie :


{
  "coin": "bitcoin",
  "price_usd": 67056,
  "price_eur": 58206,
  "market_cap_usd": 1341886945909,
  "change_24h_percent": -0.09
}

3. **Ignorer les fichiers inutiles**  
   - Crée `.gitignore` pour ne pas mettre `__pycache__` ou fichiers `.pyc`  

text
__pycache__/
*.pyc
.env


Initialiser Git et pousser sur GitHub
git init
git add .
git commit -m "Initial commit - API Crypto"
git branch -M main
git remote add origin https://github.com/ton-utilisateur/crypto-api.git
git push -u origin main



