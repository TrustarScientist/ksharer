# 🌐 KSHARER

KSHARER is a knowledge-sharing platform that enables users to express ideas, ask questions, and share helpful content in a social, structured, and rewarding environment.

## 🚀 Features 

- 🧠 **Thoughts**: Short-form post system (like tweets) for sharing quick insights or questions.
- 🔗 **PostChain**: Posts can be connected in a logical chain like a conversation or topic tree.
- 💬 **Niches**: Topic-specific communities, both public and private.
- 💰 **ZiniCoin Wallet**: Users earn and spend virtual coins to unlock premium resources.
- 🔒 **Access Control**: Resources and niche access can be gated with one-time or recurring payments.
- 🌍 **AJAX-Driven UI**: Fast, dynamic interface without full page reloads.
- 🛠️ **Admin Panel**: Custom Django admin for managing users, content, and more.

## 🛠️ Tech Stack 

- Backend: Django + MySQL (for now...designed to be ported to PostgreSQL)
- Frontend: HTML + JavaScript (AJAX)
- Authentication: Email/Username/Phone login
- Deployment-ready: Git & GitHub version control

## 🌟 Vision

> Making education and useful knowledge as open, accessible, and rewarding as possible, especially in Africa and beyond.

## 📁 Project Structure

```text
ksharer/
├── accounts/         # User auth & profiles
├── thoughts/         # Posting and PostChain logic
├── niches/           # Community feature
├── resources/        # Paid/free educational content
├── templates/        # Frontend templates
├── static/           # CSS/JS assets
├── core/          # Django core config
├── README.md
├── .gitignore
└── manage.py

