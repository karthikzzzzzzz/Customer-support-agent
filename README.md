# Customer Support Agent

## 📌 Overview
Customer Support Agent is an AI-powered chatbot designed to handle customer inquiries efficiently. It integrates natural language processing (NLP) and a backend system to provide automated responses, improving customer service experiences.



## <img width="1440" alt="Screenshot 2025-03-28 at 3 36 23 PM" src="https://github.com/user-attachments/assets/9a333040-48b8-45cb-b5c3-50319186cffa" />



✨ Features
- AI-driven chatbot for customer support
- Backend powered by FastAPI
- Frontend built with React and Vite
- Docker support for easy deployment
- Database integration for storing chat history
- Secure authentication and API handling

## 🛠️ Tech Stack
- **Frontend:** React, Vite
- **Backend:** FastAPI, Python
- **Database:** PostgreSQL / MongoDB
- **AI Model:** GPT-based chatbot
- **Deployment:** Docker, GitHub Actions

## 🚀 Installation & Setup
### **1. Clone the Repository**
```bash
git clone https://github.com/karthikzzzzzzz/Customer-support-agent.git
cd Customer-support-agent
```

### **2. Backend Setup**
```bash
cd Backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
uvicorn main:app --reload
```

### **3. Frontend Setup**
```bash
cd Frontend
npm install
npm run dev
```

### **4. Run with Docker (Optional)**
```bash
docker-compose up --build
```

## 📜 Environment Variables
Create a `.env` file and configure the required API keys(OpenAI KEY).

## 📖 Usage
- Open `http://localhost:3000` to access the chatbot UI.
- The chatbot responds to customer queries using AI.
- Chat history is stored in the database.




