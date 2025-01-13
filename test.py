import pygame

def play_midi(midi_file):
    """播放MIDI文件"""
    pygame.mixer.init()
    pygame.mixer.music.load(midi_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(1000)
    pygame.mixer.quit()

if __name__ == "__main__":
    midi_file = "Moanin_converted.mid"
    play_midi(midi_file)
