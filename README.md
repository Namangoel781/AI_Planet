# 🌟 [AI_Planet]


![Project Banner or Screenshot](https://www.cityincubator.lu/wp-content/uploads/2024/10/lci-1694619486267.png)

---

## 📝 Table of Contents

1. [About the Project](#about-the-project)  
2. [Key Features](#key-features)  
3. [Tech Stack](#tech-stack)  
4. [Setup and Installation](#setup-and-installation)  
5. [Usage](#usage)  
6. [API Documentation](#api-documentation)  
7. [Screenshots](#screenshots)  
8. [Contributing](#contributing)  
9. [License](#license)  
10. [Contact](#contact)  

---

## 🧐 About the Project

[AI_Planet] simplifies [problem statement, e.g., "content exploration from large PDF documents"] by leveraging [key technologies]. The application is designed to deliver [value proposition, e.g., "quick and accurate responses"] through [methodology or unique approach].  

**Why this project?**  
- [Reason 1: e.g., "Eliminate the hassle of manually searching through lengthy PDFs."]
- [Reason 2: e.g., "Provide an intuitive user experience with AI-powered insights."]

---

## ✨ Key Features

- **PDF Uploading**: Seamlessly upload and parse PDFs.  
- **AI-Driven Q&A**: Ask natural language questions and get precise answers.  
- **Responsive Design**: Fully optimized for desktop and mobile.  
- **Efficient Storage**: Leverages [ PostgreSQL] for robust data handling.  

---

## 🛠️ Tech Stack

| **Category**   | **Technology**      |
|-----------------|---------------------|
| **Frontend**   | React.js, Tailwind CSS |
| **Backend**    | FastAPI, Python      |
| **Database**   | PostgreSQL   |
| **AI/NLP**     | LangChain, LLamaIndex |

---


## ⚙️ Setup and Installation

### Prerequisites
- **Python 3.9+**: [Install Python](https://www.python.org/downloads/)  
- **PostgreSQL**: [Setup Instructions](https://www.postgresql.org/)  

### Installation Steps
1. **Clone the Repository**:  
    ```bash
    git clone https://github.com/Namangoel781/AI_Planet.git
    cd project-name
    ```

2. **Frontend Setup**:  
    ```bash
    cd frontend
    npm install
    npm start
    ```

3. **Backend Setup**:  
    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```

4. **Database Setup**:  
    ```bash
    python backend/manage.py migrate
    ```

5. **Environment Variables**:  
   Create `.env` files for both frontend and backend with the following keys:  
   - `DB_URL`  
   - `SECRET_KEY`  


---

## 🖥️ Usage

1. Navigate to the frontend app at `http://localhost:3000`.  
2. Upload a PDF and start asking questions about its content!  

---

## 📄 API Documentation

The backend provides an interactive API documentation interface.  

- **Swagger UI**: Visit `/docs`.  
- **ReDoc**: Visit `/redoc`.  

### Sample Endpoints
1. **Upload Document**:  
    ```http
    POST /api/upload
    Body: { file: PDF file }
    ```

2. **Ask a Question**:  
    ```http
    POST /api/question
    Body: { question: "Your question here" }
    ```

---


---

## 🤝 Contributing

We welcome contributions to enhance [Project Name]!  

### How to Contribute
1. Fork the project.  
2. Create a new branch:  
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:  
    ```bash
    git commit -m "Add new feature"
    ```
4. Push to the branch:  
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.  

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 💬 Contact

Created by [Naman Goel](https://dev-naman-portfolio.netlify.app/) - feel free to reach out!

- Email: [dev.naman555@gmail.com](mailto:dev.naman555@gmail.com)  
- LinkedIn: [your-linkedin-profile](https://www.linkedin.com/in/naman-goel-6a6b621b6/)  
