import os
import sys
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        '..',
        'feature_extractor'
    )
)
from unittest.mock import patch, mock_open
import pytest

import sample_loader

def test_convert_to_full_path():
    dirname = "foo"
    lines = ["bar1.txt", "bar2.txt"]
    expected = ["foo/bar1.txt", "foo/bar2.txt"]
    actual = sample_loader.convert_to_full_path(lines, dirname)
    assert expected == actual

def test_load_metadata_success():
    testfile = "testfile"
    lines = "foo\nbar"
    expected = ["foo", "bar"]
    with patch("builtins.open", mock_open(read_data=lines)) as mock_file:
        sample = sample_loader.SampleLoader(testfile)
        actual = sample._load_metadata()

        mock_file.assert_called_with(testfile + ".meta")
    assert expected == actual

def test_load_metasdata_fail():
    testfile = "testfile"
    expected = []
    with patch("builtins.open") as mock_file:
        mock_file.side_effect  = IOError
        sample = sample_loader.SampleLoader(testfile)
        actual = sample._load_metadata()
        mock_file.assert_called_with(testfile + ".meta")
    assert expected == actual

def mock_ok():
    return "OK"

def test_load_training_sample():
    testfile = "folder/testfile"
    expected_name = "testfile"
    with patch("sample_loader.SampleLoader._load_metadata", return_value="OKmeta") as mock_load_metadata:
        with patch("music21.converter.parse", return_value="OK") as mock_converter:
            loader = sample_loader.SampleLoader(testfile)
            actual = loader.load_training_sample()
            # TODO: check the call
            mock_converter.assert_any_call(testfile + ".score.xml")
            mock_converter.assert_any_call(testfile + ".perf.mid")
    assert expected_name == actual['name']
    assert "OK" == actual['score']
    assert "OK" == actual['perf']
    assert "OKmeta" == actual['meta']

def test_load_training_sample_fail():
    testfile = "folder/testfile"
    with patch("music21.converter.parse") as mock_converter:
        with pytest.raises(Exception):
            mock_converter.side_effect  = IOError
            loader = sample_loader.SampleLoader(testfile)
            loader.load_training_sample()

def test_create_sample():
    test_file = "folder/testfile"

    sample = sample_loader.SampleLoader(test_file)

    expected_score_path = test_file + ".score.xml"
    expected_performance_path = test_file + ".perf.mid"
    expected_meta_path = test_file + ".meta"

    assert expected_score_path == sample._get_score_path()
    assert expected_performance_path == sample._get_performance_path()
    assert expected_meta_path == sample._get_meta_path()

