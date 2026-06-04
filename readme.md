# 🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using Python, Machine Learning, and Streamlit. The application recommends movies similar to a selected movie by analyzing movie metadata and calculating similarity scores.

## 🌐 Live Demo

Add your deployed Streamlit link here: 

```
https://your-app-name.streamlit.app](https://movie-recommendation-systeem.streamlit.app/)
```

---

## 📌 Project Overview

Choosing a movie from thousands of available options can be overwhelming. This project helps users discover movies similar to their favorites using a content-based recommendation approach.

The system analyzes movie features such as genres, keywords, cast, crew, and overview, then computes similarity scores to recommend the most relevant movies.

---

## ✨ Features

* Movie recommendation based on content similarity
* Interactive and user-friendly Streamlit interface
* Movie poster display using TMDB API
* Fast recommendation generation
* Responsive dark-themed UI
* Deployed on Streamlit Cloud

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Pickle
* Requests
* Streamlit
* Gdown

### APIs

* TMDB (The Movie Database) API

---

## 📂 Project Structure

```text
movie-recommendation-system/
│
├── main.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md

```

---

## ⚙️ Working Principle

### Data Collection

Movie metadata is collected from the TMDB dataset.

### Feature Engineering

The following movie attributes are combined:

* Genres
* Keywords
* Cast
* Crew
* Overview

### Text Vectorization

The combined textual data is transformed into vectors using:

```python
CountVectorizer
```

### Similarity Computation

Cosine Similarity is calculated between movie vectors:

```python
cosine_similarity()
```

Movies with the highest similarity scores are recommended to the user.

---

## 🚀 Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git

cd movie-recommendation-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run main.py
```

---

## ☁️ Deployment

The application is deployed using Streamlit Community Cloud.

### Steps

1. Push the project to GitHub.
2. Upload large model files externally (Google Drive/Hugging Face).
3. Connect the repository to Streamlit Cloud.
4. Deploy the application.

---

## 📊 Recommendation Workflow

```text
User Selects Movie
          │
          ▼
Retrieve Movie Index
          │
          ▼
Find Similarity Scores
          │
          ▼
Sort Movies by Similarity
          │
          ▼
Fetch Posters via TMDB API
          │
          ▼
Display Top Recommendations
```

---

## 🖼️ Screenshots

### Home Page

Add screenshot here.

### Recommendations


<img width="1920" height="996" alt="image" src="https://github.com/user-attachments/assets/eb0308ea-1088-4c98-a302-8aba5a2a04da" />

---

## 🔮 Future Enhancements

* Hybrid recommendation system
* User authentication
* Movie search functionality
* Genre-based filtering
* Watchlist feature
* Rating prediction
* Collaborative filtering integration
* Personalized recommendations

---

## 👨‍💻 Author

**Saksham Raj**

* LinkedIn: https://www.linkedin.com/in/sakshamraj1/
* GitHub: https://github.com/your-github-username

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
