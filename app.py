import os
import torch
import torchaudio
import numpy as np
import base64
import streamlit as st
from audiocraft.models import MusicGen

# Utility functions
def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href

# Load the model with caching
@st.cache_resource
def load_model():
    try:
        model = MusicGen.get_pretrained('facebook/musicgen-small')
        return model
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        return None

# Generate music tensors
def generate_music_tensors(model, description, duration: int):
    try:
        model.set_generation_params(use_sampling=True, top_k=250, duration=duration)
        output = model.generate(descriptions=[description], progress=True, return_tokens=True)
        return output[0]
    except Exception as e:
        st.error(f"Music generation failed: {e}")
        return None

# Save the generated audio
def save_audio(samples: torch.Tensor, save_path="audio_output/"):
    try:
        sample_rate = 32000
        ensure_dir_exists(save_path)
        samples = samples.detach().cpu()

        if samples.dim() == 2:
            samples = samples[None, ...]

        audio_paths = []
        for idx, audio in enumerate(samples):
            audio_path = os.path.join(save_path, f"audio_{idx}.wav")
            torchaudio.save(audio_path, audio, sample_rate)
            audio_paths.append(audio_path)
        
        return audio_paths

    except Exception as e:
        st.error(f"Failed to save audio: {e}")
        return []

# Streamlit App
def main():
    # Set up the page configuration with a custom icon and title
    st.set_page_config(
        page_icon="🎵",
        page_title="Text-to-Music Generator",
        layout="centered"
    )

    # Title with custom styling
    st.markdown(
        "<h1 style='text-align: center; color: #FF4B4B;'>🎶 Text-to-Music Generator 🎶</h1>",
        unsafe_allow_html=True
    )

    # A brief explanation in an expander
    with st.expander("What does this app do?"):
        st.markdown(
            """
            This app generates music based on a textual description using Meta's Audiocraft library and the MusicGen model. 
            Just enter a description, select the duration, and enjoy the music created just for you!
            """
        )

    # Create a form for user input
    with st.form("input_form"):
        text_area = st.text_area("Describe your music idea:", placeholder="e.g., A calm and soothing melody...")
        time_slider = st.slider("Select duration (seconds):", 0, 20, 10)
        
        # Submit button
        submitted = st.form_submit_button("Generate Music 🎵")

    # Process the input after submission
    if submitted and text_area:
        st.markdown("### Your Input")
        st.json({
            'Description': text_area,
            'Duration (in seconds)': time_slider
        })

        st.markdown("### Generating Music...")
        model = load_model()
        if model:
            music_tensors = generate_music_tensors(model, text_area, time_slider)
            if music_tensors is not None:
                audio_paths = save_audio(music_tensors)
                
                # Display the generated audio files
                st.markdown("### Enjoy Your Music")
                for idx, audio_filepath in enumerate(audio_paths):
                    st.audio(audio_filepath)
                    st.markdown(get_binary_file_downloader_html(audio_filepath, f'Audio {idx + 1}'), unsafe_allow_html=True)
            else:
                st.error("Error in generating music.")
        else:
            st.error("Failed to load the MusicGen model.")

if __name__ == "__main__":
    main()