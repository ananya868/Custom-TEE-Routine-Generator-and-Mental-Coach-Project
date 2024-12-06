# ⚾ Custom TEE Generator & Mental Coach for Baseball/Softball 

Welcome to the **Custom TEE Generator & Mental Coach** project! This exciting tool is designed to take your baseball or softball game to the next level, leveraging the latest in AI and data management technologies. Built using RAG, Pinecone, and OpenAI, our tool provides personalized training and mental coaching to help you excel on the field.

<p align="center">
  <img src="trg.png" width="650" />
</p>
<p align="center">
  <img src="mqa.png" width="650" />
</p>

## Project Overview

This project utilize RAG using pinecone query database to retrieve data which is collected over many youtube video transcriptions of top baseball/softball coaches. This ll not only help with creating personalized TEE routine and answers related to mental problems faced by players but also provide accurate result leveraging lessons from the top coachs. Whether you're a beginner or a pro, this custom TEE generator and mental coach will help you improve your skills and mental toughness.

### Key Features

- **Custom TEE Routine Generator**: Create personalized TEE routines to enhance your hitting accuracy and power.
- **Mental Coaching**: Receive tailored mental strategies to boost your confidence and focus during games.
- **RAG Integration**: Utilize advanced AI research to provide the latest training techniques.
- **Youtube Learnings**: The data is leveraged from youtube videos of top baseball/softball coaches.
- **Pinecone for Data Management**: Uses Pinecone to store the queries and routines.
- **OpenAI for Intelligence**: OpenAi for formulating concise and accurate answers to provide quality answers.

## 🚀 Getting Started

Follow these steps to set up the project on your local machine.

### Prerequisites

- Git
- Python 3.x
- Pip
- Virtual environment tools (e.g., virtualenv, conda)
- Streamlit
- OpenAi API

## Installation

**Note**: You must have an OpenAi Api key to use this project!

1. **Clone the repository:**
  ```bash
  git clone https://github.com/ananya868/Custom-TEE-Routine-Generator-and-Mental-Coach-Project.git
  cd Custom-TEE-Routine-Generator-and-Mental-Coach-Project
  ```
2. **Create and activate a virtual environment:**
  
3. **Install the dependencies:**
```bash
pip install -r requirements.txt
```
4. **Set up environment variables:**

Create a `.env` file in the root directory and add your openai api key.

The pinecone api key is already given, just update the openai api key!
```bash
OPENAI_API_KEY = "#your key here"
PINECONE_API_KEY = "105107c0-a54b-4c2c-8581-a818f0bd5b06"
```
## ⚙️ Usage

Run the application with:
```bash
streamlit run main.py
```

## 🤝 Contributing

We welcome contributions! Feel free to open an issue or submit a pull request.

## 📧 Contact

Have questions or feedback? Reach out to us at [your-ananya8154@gmail.com](mailto:ananya8154@gmail.com).

---

Thank you for checking out our project! We hope it helps you hit home runs both on and off the field! 🏆🌟
