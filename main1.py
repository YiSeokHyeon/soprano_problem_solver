from music21 import *
from music21.note import Rest
import random

#0 환경 설정에서 기본 악보 보기 프로그램을 Sibelius로 변경
us = environment.UserSettings()
us['musicxmlPath'] = '/Applications/Sibelius.app'  # Sibelius 실행 파일의 경로로 변경

#1 악보 생성
score = stream.Score()

#2 4성부 정의
soprano = stream.Part()
alto = stream.Part()
tenor = stream.Part()
bass = stream.Part()
   
#3 음자리표 입력 
soprano.append(clef.TrebleClef())  # 소프라노는 일반적으로 트레블 클레프 사용
alto.append(clef.AltoClef())
tenor.append(clef.TenorClef())
bass.append(clef.BassClef())

#4 문제 불러오기
def get_key_and_time_signatures(file_path):
    """
    입력된 MIDI 파일에서 조표와 박자표를 골라냅니다.

    Parameters:
    file_path (str): MIDI 파일 경로

    Returns:
    tuple: 조표와 박자표 
    """
    # 파일을 music21 객체로 변환
    score = converter.parse(file_path)
    
    # flatten()을 사용하여 악보를 평면화하여 조표와 박자표 추출
    key_signature = score.flatten().getElementsByClass('KeySignature')[0]
    time_signature = score.flatten().getElementsByClass('TimeSignature')[0]
    
    return key_signature, time_signature

def get_pitches_and_durations(file_path):
    """
    주어진 MIDI 파일에서 음고와 음가를 튜플 형식으로 추출합니다.

    Parameters:
    file_path (str): MIDI 파일 경로

    Returns:
    list: (음고/쉼표, 음가) 튜플의 리스트
    """
    # 파일을 music21 객체로 변환
    score = converter.parse(file_path)
    
    # 모든 음표와 쉼표를 평면화하여 추출
    elements = score.flatten().getElementsByClass(['Note', 'Rest'])
    
    # 음고와 음가 추출하여 튜플 리스트 생성
    pitch_duration_tuples = []
    for elem in elements:
        if isinstance(elem, note.Note):
            pitch = elem.pitch.nameWithOctave
        elif isinstance(elem, note.Rest):
            pitch = 'Rest'
        duration = elem.duration.quarterLength
        pitch_duration_tuples.append((pitch, duration))
    
    return pitch_duration_tuples

file_path = 'soprano problem.mid'  # 실제 MIDI 파일 경로로 변경
key_signature, time_signature = get_key_and_time_signatures(file_path)
pitch_duration_tuples = get_pitches_and_durations(file_path)

#5 조표 입력
for part in [soprano, alto, tenor, bass]:
    part.append(key_signature)
    
#6 박자표 입력
for part in [soprano, alto, tenor, bass]:
    part.append(time_signature)

#7 소프라노 성부에 음표 및 쉼표 입력
for pd in pitch_duration_tuples:
    p, d = pd
    if p == 'Rest':
        n = note.Rest()
    else:
        n = note.Note(p)
    n.quarterLength = d
    soprano.append(n)
    
    
#8 소프라노 음가/쉼표를 단위박으로 다 쪼개기

    # 새로운 스트림 객체 생성
normalized_soprano = stream.Part()
    
    # 단위박 설정 (대부분의 문제들의 단위박은 4분음표 또는 8분음표)
unit_list = {'4': 1.0, '8': 0.5}
unit_duration = duration.Duration(unit_list[list(str(time_signature).split()[1])[2]])
    
    # 각 음표/쉼표를 단위박으로 노멀라이즈
for element in soprano.flat.notesAndRests:
    num_units = int(element.quarterLength / unit_duration.quarterLength)
    for i in range(num_units):
        if isinstance(element, note.Note):
            new_element = note.Note(element.pitch)
        elif isinstance(element, Rest):
            new_element = Rest()
        new_element.duration = unit_duration
        new_element.offset = element.offset + i * unit_duration.quarterLength
        normalized_soprano.append(new_element)
            
    # 음표/쉼표 str만 추출
elements_list = []
for element in normalized_soprano.notesAndRests:
    if isinstance(element, note.Note):
        elements_list.append(element.pitch.name)  # 음고만 추가
    elif isinstance(element, Rest):
        elements_list.append('Rest')

#9 소프라노 문제의 각각의 음에 대한 음도(scale degree)구하는 함수 정의
def get_scale_degrees(pitch_duration_tuples):
    # 초기값 설정
    scale_degrees = []
    
    # key.Key만 가지고는 조성이 관계조의 장조/단조인지 파악할수가 없기 때문에 최종음은 무조건 tonic임을 이용해서 조성을 파악
    x = str(key_signature).split()[0]
    for n in range(len(pitch_duration_tuples)-1, -1, -1):
        if pitch_duration_tuples[n][0] == 'Rest':
            continue
        else:
            y = list(pitch_duration_tuples[n][0])[0]
            break
    # 이제 진짜 scale degree 알아내는 작업    
    if x == y:
       for pitch in pitch_duration_tuples:
           if pitch == 'Rest':
               scale_degrees.append((None, None))
           else:
               note_pitch = note.Note(pitch)
               scale_degree = key_signature.getScaleDegreeAndAccidentalFromPitch(note_pitch.pitch)
               scale_degrees.append(scale_degree)
    else:
       relative_key = key_signature.relative
       for pitch in pitch_duration_tuples:
           if pitch == 'Rest':
               scale_degrees.append((None, None))
           else:
               note_pitch = note.Note(pitch)
               scale_degree = relative_key.getScaleDegreeAndAccidentalFromPitch(note_pitch.pitch)
               scale_degrees.append(scale_degree)
   
    return scale_degrees

#10 각각의 음도에 따른 배치가능한 화성리스트 추출
    
    # 첫 번째 원소들만 추출한 리스트
first_elements = [t[0] for t in list(get_scale_degrees(elements_list))]

    # (Z7, modulo7 addtion)을 정의
class Z7:
    def __init__(self, value):
        self.value = value % 7

    def __add__(self, other):
        if isinstance(other, Z7):
            return Z7((self.value + other.value) % 7)
        else:
            return NotImplemented

    def __repr__(self):
        return f"{self.value}"

    # 어떤 한 음도를 x라고 하면, 배치가능한 화음의 로마숫자들은 x, x-2, x-4, x-6(-는 Z7에 modulo7 addition의 역연산)이다.
    # 이 경우의 수들을 각각의 음도순서에 맞게 저장한다.
    
lists_of_Harmony=[]
for deg in first_elements:
    if deg is not None:
        c = (Z7(deg), Z7(deg - 2), Z7(deg - 4), Z7(deg - 6))
        case = tuple(7 if x.value == 0 else x.value for x in c) # Z7 객체의 value가 0인 경우 7로 바꾸기
        lists_of_Harmony.append(case)
    else:
        lists_of_Harmony.append(deg)

#11 화성 결정 (이 부분에서 딥러닝이 필요함. 알고리즘만으로 계속 어떤 패턴들을 입력하는 것은 이 프로그램을 발전시키기 힘듬.)

    # 문제에 못갖춤마디가 있는지 없는지 확인하기 
    
def detect_anacrusis(score, time_signature):
    try:
        first_measure = score.parts[0].measure(1)
        measure_length = first_measure.duration.quarterLength
        full_measure_length = time_signature.barDuration.quarterLength
        
        if measure_length < full_measure_length:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error in detecting anacrusis: {e}")
        return False

    # 원래 맨 처음의 화음은 I이 와야 하나, 못갖춤마디로 문제가 시작되는 경우는 V가 와서 I으로 진행할 수 있다. 
    # 이때 못갖춤마디가 와서 V를 뽑았으면 바로 그다음에는 I를 뽑아야 한다. 
    # 어떠한 진행이 되었든 V에서 IV로, VII에서 IV로 가는 진행은 하지 않는다.
    # 마디 길이 이상으로 화성이 머무르지 않도록 한다.
    # 맨 마지막에는 완전 정격종지(V-I)로 끝내는 것이 원칙이다.
    # 문제 중간에 마디길이 만큼의 음가가 있고, 여기에서 I,V,VI를 선택할 수 있으면 이 3개중 하나만을 선택한다. (종지)
    # 만약 I,VI를 고를 거라면, 바로 그 전에 5가 등장해야한다.
    # 7음은 해결이 되어야 하므로, 7화음을 무조건적으로 선택해야 하는 7화음의 3전위를 선택한 경우, 그 다음의 화음은 7음이 해결된 화성만이 올수 있다.
    # 랜덤보다 더 세련된 방법은 딥러닝을 통해 선택을 더 신중하게 하는 것이다.
    # 이 8개의 최소한의 규칙을 적용해서 숫자들을 고르는 함수를 정의, 그리고 이 규칙을 적용했을때 고를 수 있는 숫자가 여러개라면 랜덤으로 숫자를 선택한다.


def select_numbers(data, anacrusis, measure_length):
    selected_numbers = []
    last_selected = None
    must_select_1 = False
    must_select_1_or_none = False
    last_5_or_7_index = -1

    for i in range(len(data)):
        if data[i] is not None and (5 in data[i] or 7 in data[i]):
            last_5_or_7_index = i

    for index, item in enumerate(data):
        if item is None:
            selected_numbers.append(None)
            continue

        possible_choices = []

        if must_select_1_or_none:
            possible_choices = [1]
        elif must_select_1:
            possible_choices = [1]
            must_select_1 = False
        elif anacrusis and last_selected is None:
            possible_choices = [x for x in item if x in {5, 1}]
            if 5 in possible_choices:
                must_select_1 = True
        elif not anacrusis and last_selected is None:
            possible_choices = [1]
        elif last_selected in {5, 7}:
            possible_choices = [x for x in item if x != 4]
        else:
            if index > 0 and index < len(data) - 1 and all(data[index + offset] == item for offset in range(-measure_length // 2 + 1, measure_length // 2)):
                if last_selected == 5:
                    possible_choices = [1, 6] if 1 in item and 6 in item else [1] if 1 in item else [6] if 6 in item else [5]
                else:
                    possible_choices = [5, 1, 6]
                    possible_choices = [x for x in possible_choices if x in item]
            else:
                possible_choices = [x for x in item if selected_numbers[-measure_length:].count(x) < measure_length]

        if index == last_5_or_7_index:
            possible_choices = [5] if 5 in item else [7]
            must_select_1_or_none = True

        if len(possible_choices) > 1:
            selected = random.choice(possible_choices)
        else:
            selected = possible_choices[0]

        selected_numbers.append(selected)
        last_selected = selected

    return selected_numbers


pre_chord_progreesion = select_numbers(lists_of_Harmony, detect_anacrusis(soprano, time_signature), time_signature.numerator)



#12 성부 음역제한 함수 정의


def voice_range_restriction(lowest_pitch, highest_pitch):
    voice_range = {}
    
    # 시작 옥타브와 끝 옥타브 추출
    start_octave = int(lowest_pitch[-1])
    end_octave = int(highest_pitch[-1])
    start_pitch = lowest_pitch[:-1]
    end_pitch = highest_pitch[:-1]

    pitch_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    for octave in range(start_octave, end_octave + 1):
        for pitch_name in pitch_names:
            if (octave == start_octave and pitch_names.index(pitch_name) < pitch_names.index(start_pitch)) or (octave == end_octave and pitch_names.index(pitch_name) > pitch_names.index(end_pitch)):
                continue
            pitch_name_full = f'{pitch_name}{octave}'
            voice_range[pitch_name_full] = note.Note(pitch.Pitch(pitch_name_full))
            if pitch_name_full[1] != '#':
                voice_range[f'{pitch_name}#{octave}'] = note.Note(pitch.Pitch(f'{pitch_name}{octave}', accidental='sharp'))
            if pitch_name_full[1] != 'b':
                voice_range[f'{pitch_name}b{octave}'] = note.Note(pitch.Pitch(f'{pitch_name}{octave}', accidental='flat'))
            voice_range[f'{pitch_name}##{octave}'] = note.Note(pitch.Pitch(f'{pitch_name}{octave}', accidental='double-sharp'))
            voice_range[f'{pitch_name}bb{octave}'] = note.Note(pitch.Pitch(f'{pitch_name}{octave}', accidental='double-flat'))

    # 성부음역이외의 딕셔너리 원소 제거
    keys_to_remove = [f'{start_pitch}bb{start_octave}', f'{start_pitch}b{start_octave}', f'{end_pitch}#{end_octave}', f'{end_pitch}##{end_octave}']

    for key in keys_to_remove:
        if key in voice_range:
            del voice_range[key]
            
    return voice_range


    # 성부 음역에 맞는 모든 음들의 set을 추출하여 각 성부의 _range에 저장.

soprano_range = voice_range_restriction('C4','A5')
alto_range = voice_range_restriction('G3','E5')
tenor_range = voice_range_restriction('C3', 'A4')
base_range=voice_range_restriction('E2', 'E4')



#12 앞으로 각 성부에 입력될 음들이 주어진 음역에 맞는지 확인하는 함수정의 

    # 한 음이 음역안에 들어오는지 확인하는 함수 
def is_in_range(pitch, voice_range):
    """
    주어진 음(pitch)이 주어진 성부 음역(voice_range)에 있는지 확인하는 함수
    """
    return pitch in voice_range


    # 그 성부의 모든 음들이 음역안에 들어와있는지 확인하는 함수 

def check_voice_ranges(part, voice_range):
    """
    주어진 성부(part)의 모든 음이 지정된 음역(voice_range)에 있는지 확인하는 함수
    """
    for n in part.notes:
        if not is_in_range(n.pitch.nameWithOctave, voice_range):
            print(f"Note {n.pitch} in part {part.id} is out of range {voice_range}")
            return False
    return True

soprano_range = voice_range_restriction('C4','A5')
alto_range = voice_range_restriction('G3','E5')
tenor_range = voice_range_restriction('C3', 'A4')
base_range=voice_range_restriction('E2', 'E4')


#13 화음들 4성부배치를 위한 음도로 정의


print(lists_of_Harmony)
print(pre_chord_progreesion)


# 4성부를 하나의 악보로 모으기
score.append([soprano, alto, tenor, bass])

# 악보 출력
# score.show()
