# **TuneText: AI-Powered Music Generation**

**TuneText** is a powerful text-to-music generation app built using Meta's Audiocraft library. This application leverages the MusicGen Small model to create unique musical compositions from simple text descriptions. The app is developed with Streamlit, providing an intuitive and interactive user interface.

## **Features**
- **Text-to-Music Conversion**: Generate music based on textual descriptions.
- **Customizable Duration**: Choose the length of the generated music with a simple slider.
- **Real-time Audio Playback**: Listen to the generated music directly within the app.
- **Download Option**: Easily download the generated music in WAV format.

## **How It Works**
1. **Enter a Description**: Provide a short text description of the type of music you want.
2. **Set the Duration**: Select the desired duration for the music.
3. **Generate**: Click to generate music that matches your description.
4. **Listen and Download**: Play the music directly in the app and download it if you like.

## **Technology Stack**
- **Python**
- **Streamlit** for the user interface.
- **Meta's Audiocraft** for music generation.
- **MusicGen Small Model** for high-quality music output.

## **Installation and Usage**
1. **Clone the repository**:
    ```bash
    git clone https://github.com/gg0099/TuneText.git
    cd TuneText
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv myenv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
      ```bash
      myenv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source myenv/bin/activate
      ```

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the app**:
    ```bash
    streamlit run app.py
    ```

6. **Access the app**: Open your browser and go to `http://localhost:8501` to use the app.

## **Contributing**
Contributions are welcome! Please feel free to submit a Pull Request.

## **License**
This project is licensed under the MIT License.

## **Acknowledgments**
- **Meta** for providing the Audiocraft library and MusicGen model.
- **Streamlit** for making it easy to create interactive web apps in Python.