from madmom.features import *


def audio_to_MIDI_notes(file):
    proc = CNNPianoNoteProcessor()
    adsr = ADSRNoteTrackingProcessor(pitch_offset=21, onset_threshold=0.9)

    audio_file = file
    act = proc(audio_file)
    MIDI_notes = adsr(act)

    print("post")
    print(MIDI_notes)

    return MIDI_notes
