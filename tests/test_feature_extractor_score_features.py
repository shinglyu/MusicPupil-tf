import os
import sys
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..',
        'feature_extractor'
    )
)

from unittest.mock import MagicMock
import music21
import score_features

def test_extract_pitch_midi_num():
    sample = MagicMock()
    sample['score'].flat.notes.pitches = [
        music21.pitch.Pitch('C5'),
        music21.pitch.Pitch('D5'),
        music21.pitch.Pitch('E5'),
    ]

    # Ref:
    # http://www.electronics.dit.ie/staff/tscarff/Music_technology/midi/midi_note_numbers_for_octaves.htm
    expected = [72, 74, 76]
    actual = score_features.extract_pitch_midi_num(sample)
    assert expected == actual

