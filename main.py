from madmom.features import *


def get_notes():
    proc = CNNPianoNoteProcessor()
    adsr = ADSRNoteTrackingProcessor(pitch_offset=21, onset_threshold=0.9)

    audio_file = 'data/youngPlane.m4a'
    act = proc(audio_file)
    MIDI_notes = adsr(act)

    print("get")
    print(MIDI_notes)

    return MIDI_notes


def post_notes(file):
    proc = CNNPianoNoteProcessor()
    adsr = ADSRNoteTrackingProcessor(pitch_offset=21, onset_threshold=0.9)

    audio_file = file
    act = proc(audio_file)
    MIDI_notes = adsr(act)

    print("post")
    print(MIDI_notes)

    return MIDI_notes
