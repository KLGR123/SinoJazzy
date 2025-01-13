import os
import requests
from pathlib import Path
import tarfile
import io
import sys

def get_default_soundfont():
    """获取默认的音色库文件路径，如果不存在则下载"""
    # 创建音色库目录
    soundfont_dir = Path("soundfonts")
    soundfont_dir.mkdir(exist_ok=True)
    
    # 默认音色库文件路径
    soundfont_path = soundfont_dir / "default.sf2"
    
    # 如果音色库文件不存在，则下载
    if not soundfont_path.exists():
        print("下载默认音色库...", file=sys.stderr)
        try:
            # 使用 Fluid R3 音色库
            url = "https://archive.org/download/fluid-soundfont/fluid-soundfont_R3.tar.gz"
            
            # 下载文件
            response = requests.get(url)
            response.rais