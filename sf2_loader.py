from pathlib import Path

def get_piano_soundfont():
    """返回本地钢琴音色文件路径"""
    soundfont_path = Path("soundfonts/piano.sf2")
    
    if not soundfont_path.exists():
        raise FileNotFoundError("钢琴音色文件未找到，请确保 'soundfonts/piano.sf2' 存在。")
    
    return soundfont_path
