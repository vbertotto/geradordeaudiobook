# Audiobook Generator with Streamlit

This project is a simple web application built using [Streamlit](https://streamlit.io/) that converts text into audiobooks using different voice options. The user can either input text manually or upload a `.txt` file, and then choose from at least 3 different voices to generate the audiobook. The generated audio can be played directly on the webpage or downloaded as an MP3 file.

## Features

- 📖 **Text Input:** Type text or upload a `.txt` file.
- 🎤 **Voice Selection:** Choose from 3 different voices.
- 🔊 **Audio Playback:** Listen to the generated audiobook directly on the web page.
- 📥 **Download Option:** Download the generated audiobook as an MP3 file.

## How to Run Locally

### Prerequisites

Make sure you have the following installed:

- Python 3.8 or higher
- Streamlit (`pip install streamlit`)
- pyttsx3 (`pip install pyttsx3`)

### Installation Steps

1. Clone this repository:

    ```bash
    git clone https://github.com/vbertotto/geradordeaudiobook.git
    ```

2. Navigate to the project directory:

    ```bash
    cd audiobook-generator
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

5. Open your browser and navigate to `http://localhost:8501` to interact with the app.

## Project Structure

```plaintext
.
├── app.py              # Main Streamlit application
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
