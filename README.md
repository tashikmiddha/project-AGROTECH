# 🌾 ArgoTech

ArgoTech is a smart agriculture project aimed at empowering farmers and agricultural researchers by leveraging data-driven technologies. Sponsored by **IIT Ropar**, this project integrates real-time sensor data with machine learning to provide recommendations for crop selection, fertilizer usage, and irrigation needs — all through a user-friendly Django-based web application.

## 🚀 Project Overview

ArgoTech collects data from various agricultural sensors including:

- **Soil pH**
- **NPK (Nitrogen, Phosphorus, Potassium)**
- **Humidity**
- **Temperature**

Using this data, the platform deploys three custom-trained Machine Learning models to provide intelligent recommendations:

1. **Crop Prediction Model** – Suggests the most suitable crop based on soil and environmental conditions.
2. **Fertilizer Recommendation Model** – Recommends the appropriate type and amount of fertilizer.
3. **Watering Prediction Model** – Advises when and how much to water the crops for optimal growth.

---

## 🖥️ Web Platform (Built with Django)

The ArgoTech website serves as the primary user interface. It includes the following sections:

### 📊 Models Section
Access and interact with the three ML models:
- Crop Prediction
- Fertilizer Recommendation
- Watering Schedule

### 📂 Datasets Section
Explore the datasets used to train our models. Data is primarily collected from sensors and verified for accuracy.

### 📓 My Notebooks Section
Dive into the Jupyter notebooks showcasing the development and training of our ML models.

### 🏠 Home Section
Landing page introducing the purpose and goals of ArgoTech.

### 🧑‍💼 Team Section
Meet the minds behind the project, along with their roles and contributions.

### 📞 Contact Section
Reach out to the ArgoTech team for queries, feedback, or collaboration opportunities.

### 📃 Terms Section
View the terms of use, data policy, and disclaimers related to the ArgoTech platform.

---

## 📡 Sensor Integration

Data is collected through a network of sensors deployed in real agricultural fields. These include:
- Soil pH sensors
- NPK sensors
- DHT sensors for humidity and temperature

---

## 📈 Machine Learning Models

Each model was developed using Python, Scikit-learn, and Pandas, and trained on custom datasets. You can find all model training and evaluation in the `My Notebooks` section.

---

## 🏛️ Sponsored By

This project is proudly **sponsored by IIT Ropar**, supporting innovation in AgriTech and digital transformation in agriculture.

---

## 📬 Contact

For more information, contributions, or feedback, please reach out via the [Contact section](#) on the website.

---

## 🖥️ Project Setup Instructions

Follow the steps below to get the ArgoTech Django web app and machine learning models running.

### 1. 🔁 Clone the Repository

     ```bash
     git clone https://github.com/yourusername/argotech.git
    cd argotech
 2. 🐍 Create & Activate a Virtual Environment
    Windows:

    ```bash

    python -m venv env
    env\Scripts\activate
   macOS/Linux:

    ```bash

     python3 -m venv env
      source env/bin/activate
  3. 📦 Install Project Requirements
Make sure you're in the project directory and your virtual environment is activated:

    ```bash
     pip install -r requirements.txt
   4. ⚙️ Apply Django Migrations
     ```bash

     python manage.py migrate
  5. 👤 Create a Superuser (Optional, for admin panel)
    ```bash

    python manage.py createsuperuser
Follow the prompts to create your admin account.

   6. 🚀 Start the Development Server
      ```bash
     python manage.py runserver
Now open your browser and navigate to:
http://127.0.0.1:8000

## 📌 Future Enhancements

- Integration with live weather APIs
- Mobile-friendly interface
- Multilingual support for rural outreach
- Real-time sensor data streaming

---

## 📜 License

[MIT License](LICENSE) — Feel free to use, modify, and contribute to this project under the terms of the MIT license.

---

### Made with ❤️ for sustainable farming.
