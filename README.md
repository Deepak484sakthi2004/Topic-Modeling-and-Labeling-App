# Topic Modeling and Labeling App

## Overview

This repository contains the code for a user-friendly Topic Modeling and Labeling App powered by the Latent Dirichlet Allocation (LDA) algorithm. The app is designed to analyze various types of data, including text, CSV files, and YouTube videos. Leveraging the Whisper speech-to-text model by OpenAI, it extracts transcripts from video data. The integration with Streamlit, a powerful web framework, provides an interactive and customizable user interface.

## Features

- **Topic Modeling:** Apply LDA algorithm to identify topics within the provided data.
- **Whisper Integration:** Utilize Whisper for extracting transcripts from YouTube videos.
- **Streamlit Interface:** Create an interactive and customizable user interface for seamless user experience.
- **Industry Labeling:** Utilize the Heapq algorithm to label topics based on industry, making it valuable for market research and trend analysis.

## Getting Started

### Prerequisites

- Python 3.6+
- Install dependencies by running: `pip install -r requirements.txt`

### Running the App Locally

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Deepak484sakthi2004/Topic-Modeling-and-Labeling-App
    cd Topic-Modeling-and-Labeling-App
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app:**
    ```bash
    streamlit run app.py
    ```

### Live Deployment

The Topic Modeling and Labeling App has been deployed and is accessible online.

- **Live Demo:** [Topic Modeling and Labeling App](https://topic-modeling-and-labeling-app.onrender.com/)
- **GitHub Repository:** [Topic Modeling and Labeling App Repository](https://github.com/Deepak484sakthi2004/Topic-Modeling-and-Labeling-App)

Feel free to explore the live deployment and provide feedback!

## Usage

1. Input your data using the user interface.
2. Select the data type (text, CSV file, or YouTube video).
3. Click on the "Generate Topics" button to perform topic modeling.
4. Explore the labeled topics and industry insights.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or new features to add, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the excellent web framework.
- [OpenAI](https://www.openai.com/) for the Whisper model used in speech-to-text.


For detailed instructions, visit the [GitHub Repository](https://github.com/Deepak484sakthi2004/Topic-Modeling-and-Labeling-App).
