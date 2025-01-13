import streamlit as st
import os
from sino import pentatonify_midi
import tempfile
import base64
import pretty_midi
import numpy as np
import io
from scipy.io import wavfile
from midi2audio import FluidSynth
import sf2_loader


def get_default_soundfont():
    """获取默认的内置音色库"""
    return sf2_loader.get_default_soundfont()

def midi_to_audio(midi_path):
    """将MIDI文件转换为音频数据"""
    # 加载MIDI文件
    pm = pretty_midi.PrettyMIDI(midi_path)
    
    # 将 MIDI 写入临时文件
    with tempfile.NamedTemporaryFile(suffix='.mid', delete=False) as temp_midi:
        pm.write(temp_midi.name)
        
        # 使用 FluidSynth 合成音频
        soundfont_path = sf2_loader.get_piano_soundfont()
        fs = FluidSynth(sound_font=soundfont_path)
        
        # 合成音频
        wav_path = temp_midi.name.replace('.mid', '.wav')
        fs.midi_to_audio(temp_midi.name, wav_path)
        
        # 读取生成的WAV文件
        with open(wav_path, 'rb') as wav_file:
            audio_data = wav_file.read()
            
        # 清理临时文件
        os.unlink(temp_midi.name)
        os.unlink(wav_path)
        
    return audio_data

def get_audio_player(midi_path):
    """Create audio player"""
    audio_bytes = midi_to_audio(midi_path)
    return st.audio(audio_bytes, format='audio/wav')

# Set page config
st.set_page_config(
    page_title="SinoJazzy - Jazz Pentatonic Scale Converter",
    page_icon="🪭",
    layout="wide"
)

# Custom CSS styles
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
        font-family: 'Code', monospace;
    }
    .stButton>button {
        background-color: #6c5ce7;
        color: white;
        border-radius: 8px;
        padding: 8px 20px;
        font-family: 'Code', monospace;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #5b4cc4;
        transform: translateY(-2px);
    }
    .stSelectbox {
        font-family: 'Code', monospace;
    }
    h1, h2, h3, h4 {
        font-family: 'Code', monospace;
        color: #2d3436;
    }
    .stAudio {
        width: 100%;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("🪭 SinoJazzy - Jazz Pentatonic Scale Converter")

# Create two-column layout
col1, col2 = st.columns([1, 1])

# File upload section
with col1:
    st.markdown("##### 📤 Upload Your MIDI File")
    uploaded_file = st.file_uploader("Choose MIDI file", type=['mid', 'midi'])
    
    if uploaded_file is not None:
        # Create temporary file to save uploaded MIDI
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mid') as tmp_input:
            tmp_input.write(uploaded_file.getvalue())
            input_path = tmp_input.name
            
        # Create output temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mid') as tmp_output:
            output_path = tmp_output.name
            
        # Process MIDI file
        pentatonify_midi(input_path, output_path)
        
        # Create audio player
        st.markdown("##### 🎧 Listen to the Converted Version")
        # Use selected instrument
        audio_bytes = midi_to_audio(output_path)
        st.audio(audio_bytes, format='audio/wav')
        
        # Create download link
        with open(output_path, "rb") as f:
            bytes_data = f.read()
            b64 = base64.b64encode(bytes_data).decode()
            href = f'<a href="data:audio/midi;base64,{b64}" download="converted_music.mid">Click to Download Converted MIDI File</a>'
            st.markdown(href, unsafe_allow_html=True)
            
        # Clean up temporary files
        os.unlink(input_path)
        os.unlink(output_path)

# Sample tracks section
with col2:
    st.markdown("##### 🎼 Sample Tracks")
    
    # Sample tracks data
    sample_songs = {
        "Autumn Leaves": "samples/autumn_leaves.mid",
        "Take Five": "samples/take_five.mid",
        "Moanin": "samples/moanin.mid",
        "But Not for Me": "samples/but_not_for_me.mid",
        "Like Someone in Love": "samples/like_someone_in_love.mid",
        "Misty": "samples/misty.mid"
    }
    
    # Create 3x2 grid layout for sample tracks
    cols = st.columns(2)
    for idx, (song_name, song_path) in enumerate(sample_songs.items()):
        with cols[idx % 2]:
            # st.write(f"#### {song_name}")
            
            if st.button(f"Convert {song_name}", key=f"btn_{idx}"):
                output_path = f"temp_{song_name.lower().replace(' ', '_')}.mid"
                pentatonify_midi(song_path, output_path)
                
                # Use selected instrument
                audio_bytes = midi_to_audio(output_path)
                st.audio(audio_bytes, format='audio/wav')
                
                # Create download link
                with open(output_path, "rb") as f:
                    bytes_data = f.read()
                    b64 = base64.b64encode(bytes_data).decode()
                    href = f'<a href="data:audio/midi;base64,{b64}" download="{song_name}_converted.mid">Download Converted {song_name}</a>'
                    st.markdown(href, unsafe_allow_html=True)
                
                os.unlink(output_path)

# Footer
st.markdown("##### 🎹 Where Jazz Meets Chinese Style")
st.code("This project is for educational and entertainment purposes only. Please ensure you have the appropriate rights to use any uploaded MIDI files.")
