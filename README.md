🧠 Resume Generator with AI Integration

A full-stack **Resume Generator Web App** that allows users to create professional resumes using **form inputs** and **AI-powered content suggestions**. Built using Flask and Hugging Face models, it supports multiple resume templates, DOCX/PDF export, and a secure login system.


🚀 Features

- ✍️ User-friendly form to enter resume data
- 🤖 AI-powered resume content suggestions via Hugging Face models
- 🎨 Multiple professionally designed templates to choose from
- 📄 Export resumes as **PDF** or **DOCX**
- 🔐 User authentication with **sign up/login**
- 🗃️ Resume data stored using **SQLite**
- 🌐 Built with Flask, HTML/CSS
- 🔑 Uses environment variables and API keys securely


🌐 Live Demo

 [Coming Soon]

🧠 AI Integration

- Hugging Face models are used to generate and enhance:
  - Resume summaries
  - Role-specific achievements
  - Skill descriptions
- Content generation is prompt-based and customizable to user input

🛠️ Tech Stack

| Layer      | Tech                    
|------------|-------------------------
| Frontend   | HTML, CSS               
| Backend    | Flask (Python)          
| Database   | SQLite                  
| AI/ML      | Hugging Face Transformers 
| Export     | `python-docx`, `pdfkit`
| Auth       | Flask-Login             


⚙️ Installation & Setup

1. Clone the repo
   
  git clone https://github.com/waryix/resume-generator.git
  cd resume-generator

Create and activate virtual environment:

  python -m venv venv
  source venv/bin/activate  
  Windows: venv\Scripts\activate

install dependencies:

  pip install -r requirements.txt

Create a .env file
Add your API keys and config:

  HUGGINGFACE_API_KEY=your_api_key_here
  SECRET_KEY=your_flask_secret_key

Run the app:
  python main.py
