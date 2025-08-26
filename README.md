# 🌍 EcoProphet : Intelligent CO2 Forecasting

EcoProphet is a machine learning-powered web application designed to **predict CO2 emissions** based on inputs such as engine size, fuel type, and other relevant parameters. Alongside predictions, it provides **AI-generated recommendations** to promote sustainable practices.

---

## 📌 Key Highlights

- Developed using **Flask** for backend logic and UI rendering.  
- Employs a **Multiple Linear Regression** model to forecast CO2 emissions.  
- Incorporates the **Gemini API** for personalized eco-friendly recommendations.  
- Features a responsive interface built with **HTML + CSS**.  
- Lightweight and can be deployed locally with minimal setup.  

---

## 📊 Tech Stack

- **Backend:** Python, Flask  
- **Machine Learning:** Scikit-Learn, NumPy, Pandas  
- **Frontend:** HTML5, CSS3  
- **AI Integration:** Gemini API (for sustainability tips)  
- **Tools:** Jupyter Notebook, VS Code  

---

## 📂 Project Structure

CO2-Emission-Predictor/
│
├── static/ # CSS stylesheets
│ └── style.css
│
├── templates/ # HTML templates
│ ├── index.html
│ ├── results.html
│
├── app.py # Main Flask application
├── model.pkl # Pre-trained regression model
├── recommendations.py # Gemini API integration logic
├── requirements.txt # Python dependencies
└── README.md # Documentation


---

## 🧠 Model Workflow

- **Inputs:** Engine size, cylinders, fuel type, and related attributes.  
- **Output:** Predicted CO2 emissions (in grams/km).  
- Model trained on labeled datasets and validated for performance.  
- **Gemini API** generates tailored recommendations for reducing emissions.  

---

## 🚀 How to Run Locally

1. **Clone this Repository**
   ```bash
   git clone https://github.com/yourusername/CO2-Emission-Predictor.git
   cd CO2-Emission-Predictor
2.**Install Required Packages**
   pip install -r requirements.txt


3.**Start the Application**
   python app.py


4.**Open in Browser**
   Go to: http://127.0.0.1:5000

## 💡 Features

- 🔍 Real-time CO2 prediction  
- 📢 AI-powered green recommendations  
- 🔐 Secure and efficient local deployment  
- 📊 Scalable for integration with real-world sensors or data streams  

---

## 🧪 Accuracy and Performance

- The model achieved an improved prediction accuracy of **98%** on test data.
- Optimized for fast response and lightweight deployment.

---

## 📈 Future Enhancements

- Deploy on cloud (Heroku/AWS)  
- Add support for multiple ML models  
- Real-time sensor data integration  
- User dashboard for emission history tracking  

---

## 📬 Contact

Feel free to connect for contributions, questions, or suggestions:

- Email: [work.abhiinavv@gmail.com]  
