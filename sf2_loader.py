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
            response.raise_for_status()  # 检查下载是否成功
            
            # 解压缩
            tar = tarfile.open(fileobj=io.BytesIO(response.content), mode='r:gz')
            
            # 提取 .sf2 文件
            sf2_files = [f for f in tar.getnames() if f.endswith('.sf2')]
            if not sf2_files:
                raise Exception("在下载的文件中未找到.sf2文件")
                
            sf2_file = sf2_files[0]
            tar.extract(sf2_file, soundfont_dir)
            
            # 重命名为 default.sf2
            extracted_path = soundfont_dir / sf2_file
            if extracted_path.exists():
                os.rename(extracted_path, soundfont_path)
            
            print("音色库下载完成！", file=sys.stderr)
            
        except Exception as e:
            print(f"下载音色库时出错: {str(e)}", file=sys.stderr)
            # 如果下载失败，使用备用链接
            try:
                backup_url = "https://github.com/FluidSynth/fluidsynth/raw/master/sf2/VintageDreamsWaves-v2.sf2"
                print("尝试备用音色库...", file=sys.stderr)
                response = requests.get(backup_url)
                response.raise_for_status()
                soundfont_path.write_bytes(response.content)
                print("备用音色库下载完成！", file=sys.stderr)
            except Exception as e:
                print(f"备用音色库下载也失败: {str(e)}", file=sys.stderr)
                raise
    
    return str(soundfont_path)
