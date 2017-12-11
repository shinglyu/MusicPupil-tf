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

import feature_manager

def test_extract_feature():
    sample = { "test": "foo" }
    feature_list = ['a', 'b', 'c']
    extractor_module = "extractor_test"

    expected = {'a': 1, 'b': 2, 'c': 3}

    actual = feature_manager.extract_features(sample, feature_list, extractor_module)
    assert expected == actual

def test_extract_all():
    sample = { "name": "foo" }  # Dummy
    feature_list = {
        "extractor_test": ["a", "b"]
    }
    extractor_modules = ["extractor_test"]

    expected = {"name": "foo", "extractor_test": {'a': 1, 'b': 2}}

    mgr = feature_manager.FeatureManager(feature_list)
    actual = mgr.extract_all(sample)
    assert expected == actual
