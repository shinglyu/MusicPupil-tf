#!/usr/bin/env python
import config
import feature_manager
import sample_loader
import json

def main():
    # FIXME: hardcoded input/output path
    inputlist = "../data/corpus/split/test.list"
    training_features_filename = "./test_features.json"
    # We should probably extract all features, and let training script split it

    # TODO: maybe auto-search the folder?
    with open(inputlist, 'r') as f:
        sample_pathes = map(lambda x: x.strip(), f.readlines())

    sample_loaders = [sample_loader.SampleLoader(path) for path in sample_pathes]

    samples = [feature_manager.loader.load_training_sample() for loader in sample_loaders]
    training_features = [?]

    # TODO: extract features

    with open(training_features_filename, 'w') as f:
        json.dump(training_features, f, indent=3)

if __name__ == "__main__":
    main()
