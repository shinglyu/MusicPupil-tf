import os
import sys
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..',
        'feature_extractor'
    )
)

from unittest.mock import patch, MagicMock
import music21
import csv

import split_and_export

def test_split_train_test():
    samples = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    # Split in 2 as a group
    splitted = split_and_export.split_train_test(samples, int(len(samples)/2))

    assert len(splitted) > 1  # More then one way to split
    assert len(splitted[0]['training']) > 0
    assert len(splitted[0]['testing']) > 0
    assert len(splitted[0]['training']) > len(splitted[0]['testing'])
    for elem in splitted[0]['testing']:
        assert elem not in splitted[0]['training']

def test_export_to_csv():
    samples = [
        {
            "score_features": {
                "foo": [1, 2, 3]
            },
            "perf_features": {
                "bar": [7, 8, 9]
            }
        },
        {
            "score_features": {
                "foo": [4, 5, 6]
            },
            "perf_features": {
                "bar": [10, 11, 12]
            }
        }
    ]

    split_and_export.export_to_csv(samples, "tests/test_export_training.csv")

    with open('tests/test_export_training.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        rows = list(reader)
        assert rows[0] == ["foo", "bar"]
        assert rows[1] == ["1", "7"]

def test_export_all_to_csv():
    splits = [
        {"training": "training_0", "testing": "testing_0"},
        {"training": "training_1", "testing": "testing_1"},
        {"training": "training_2", "testing": "testing_2"},
    ]

    with patch("split_and_export.export_to_csv") as mock_export:
        split_and_export.export_all_to_csv(splits, "tests/test_export")
        mock_export.assert_any_call("testing_0", "tests/test_export_0_testing.csv")
        mock_export.assert_any_call("training_0", "tests/test_export_0_training.csv")
        mock_export.assert_any_call("testing_1", "tests/test_export_1_testing.csv")
        mock_export.assert_any_call("training_1", "tests/test_export_1_training.csv")
        mock_export.assert_any_call("testing_2", "tests/test_export_2_testing.csv")
        mock_export.assert_any_call("training_2", "tests/test_export_2_training.csv")

