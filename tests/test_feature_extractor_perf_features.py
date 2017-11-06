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
import perf_features

def test_extract_midi_velocity():
    sample = MagicMock()
    sample['score'].flat.notes= [
        music21.note.Note() for i in range(3)
    ]
    for i in range(3):
        sample['score'].flat.notes[i].volume.velocity = 90 + i

    expected = [90, 91, 92]
    actual = perf_features.extract_midi_velocity(sample)
    assert expected == actual
