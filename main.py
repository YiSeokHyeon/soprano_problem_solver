from music21 import *

def input_for_problem(S_or_B, midi_file):
    if S_or_B == 'soprano':
        soprano.append(converter.parse(midi_file));
    elif S_or_B == 'bass':
        bass.append(converter.parse(midi_file));

while 1:
    print('''===Study Classic Harmony with Computer! 1.0===
                           coded by Yi Seok-Hyeon (in 2024)
          
            
          
    
          
            
          To start, press any key...                 ''' )
    in_1=input()
    
    
    # Create a score
    score = stream.Score()

    # Create parts for Soprano, Alto, Tenor, and Bass
    soprano = stream.Part()
    alto = stream.Part()
    tenor = stream.Part()
    bass = stream.Part()
    
    # Add clefs 
    soprano.append(clef.SopranoClef())
    alto.append(clef.AltoClef())
    tenor.append(clef.TenorClef())
    bass.append(clef.BassClef())
    
    while(in_1):
        print('''Hello! I am Yi Seok-Hyeon. I currently study math and music.
              If you want to get explanation of this program, press \'e'\,
              If you want to start, press \'s'\.
              ''')
        in_2=input('>>>')
        if in_2=='e':
            print('''
                  ------------------------------------------------------------------------------------------------------
                  1. Motivation of the programming.
                  
                      This program is coded for students who study Classic Harmony including myself!
                  This program gives a solution of 4-voices choral problems satisfying all \'rules'\ in Classic Harmony.
                  As you know, it is quite difficult to \'solve'\ this kind of problems, 
                  because the \'rules'\ restrict some path of voices.
                  But, it is important to train the ability to write notes with reasonable restrictions.
                  What I want to do is to know how far the area of composition can be 'calculated'.
                  During the solving so-called \'soprano problem'\ and \'bass problem'\,
                  I felt what I am doing is similar to solve a sudoku.
                  Actually, I don't like this kind of problems because there's no my \'things'\ in the problems.
                  Problem orders, fill the blank.
                  I think this is not quite suitable training to find my music.
                  So, I decided to code the algorithm to fill the remain voices based on given soprano or bass melodies.
                  This is like sort of rebellion toward the major pedagogics of harmony.
                  
                  2. How to use this program?
                  
                      First, you need to give a problem in computer language form.
                  That is, you need a midi file.
                  This program demand your midi file, so you just input the file name in this program.
                  And lastly, you need to notify whether your given melody is for soprano or bass.
                  Then computer work for the solution , and gives a new midi file with complete 4-voice choral.
                  I hope this helps you to study the voice leading excercises.
                  
                  ------------------------------------------------------------------------------------------------------
                  
                  To initiate the program, press \'s'\
                      ''')
            in_3=input('>>>')
            while(in_3):
                if in_3='s':
                    break
                else:
                    print('Try again, you pressed other key...')
                    
                    
                    
                    
                    
        elif in_2=='s':
            
        S_or_B=input('>>> The type of the problem : ')
        midi_file=input('>>> Give me the midi file directory of the problem. : ')
        
        [key_signature, time_signature] = get_key_and_time_signatures(file_path) 

        # Add key signatures
        for part in [soprano, alto, tenor, bass]:
            part.append(key.Key(key_signature.split()))
            
        # Add time signatures **string input임에 주의**
        for part in [soprano, alto, tenor, bass]:
            part.append(meter.TimeSignature(time_signature))






#
##
### 여기 이후로 건들 필요 없음.
##
#


# Final process, assemble 4 all voices.
for part in [soprano, alto, tenor, bass]:
    score.append(part)

# Print the complete score.
score.show()