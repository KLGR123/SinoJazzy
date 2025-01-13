import pretty_midi
import numpy as np

# C大调五声音阶中，12 半音内的相对音名
PENTATONIC_NOTES = [0, 2, 4, 7, 9]  # 对应 C, D, E, G, A

def nearest_pentatonic_pitch(original_pitch, pentatonic_notes=PENTATONIC_NOTES, prefer_higher=True):
    """将原始MIDI音高吸附到最近的五声音阶音高上"""
    octave = original_pitch // 12
    note_in_octave = original_pitch % 12
    
    min_dist = 12
    best_note = note_in_octave
    equal_dist_notes = []
    
    for pn in pentatonic_notes:
        dist = abs(note_in_octave - pn)
        dist = min(dist, 12 - dist)
        
        if dist < min_dist:
            min_dist = dist
            best_note = pn
            equal_dist_notes = [pn]
        elif dist == min_dist:
            equal_dist_notes.append(pn)
    
    if len(equal_dist_notes) > 1:
        best_note = max(equal_dist_notes) if prefer_higher else min(equal_dist_notes)
    
    return octave * 12 + best_note

def create_midi_program_change(program_number):
    """创建程序改变事件"""
    return pretty_midi.ControlChange(
        number=0,  # Program change
        value=program_number,
        time=0
    )

def pentatonify_midi(input_midi_path, output_midi_path, pentatonic_notes=PENTATONIC_NOTES, prefer_higher=True, instrument_program=0):
    """将MIDI文件转换为五声音阶版本，并设置指定的乐器音色"""
    # 创建新的MIDI文件
    new_midi = pretty_midi.PrettyMIDI()
    
    # 创建新的乐器轨道
    program = instrument_program
    instrument = pretty_midi.Instrument(program=program)
    
    # 读取原始MIDI文件
    midi_data = pretty_midi.PrettyMIDI(input_midi_path)
    
    # 收集所有音符
    all_notes = []
    for orig_instrument in midi_data.instruments:
        for note in orig_instrument.notes:
            # 转换音高到五声音阶
            new_pitch = nearest_pentatonic_pitch(
                note.pitch,
                pentatonic_notes,
                prefer_higher
            )
            
            # 创建新音符
            new_note = pretty_midi.Note(
                velocity=note.velocity,
                pitch=new_pitch,
                start=note.start,
                end=note.end
            )
            all_notes.append(new_note)
    
    # 将所有音符添加到新乐器轨道
    instrument.notes = all_notes
    
    # 添加程序改变事件
    instrument.control_changes.append(
        create_midi_program_change(program)
    )
    
    # 将乐器轨道添加到MIDI文件
    new_midi.instruments.append(instrument)
    
    # 保存新的MIDI文件
    new_midi.write(output_midi_path)
    
    return new_midi