#!/usr/bin/env python
import config
import csv
import feature_manager
import json
import os
import sample_loader
import pandas as pd

def main():
    # FIXME: hardcoded input/output path
    inputlist = "../data/corpus/split/test.list"
    input_path = os.path.dirname(inputlist)
    training_features_filename = "./test_training_features.json"
    output_dir = "../data/extracted_features/"  # TODO: Split by runs
    # training_features_filename = "./test_training_features.csv"
    # We should probably extract all features, and let training script split it

    # TODO: maybe auto-search the folder?
    print("Loading files specified in {}".format(inputlist))
    with open(inputlist, 'r') as f:
        sample_pathes = map(lambda x: x.strip(), f.readlines())

    # TODO: move this path appending logic to sample_loader
    sample_loaders = [sample_loader.SampleLoader(os.path.join(input_path, path)) for path in sample_pathes]

    samples = [loader.load_training_sample() for loader in sample_loaders]
    # TODO: move this to a yaml config file
    features = {
        "score_features": ["pitch_midi_num"],
        "perf_features": ["midi_velocity"]
    }

    # TODO: extract features

    extractor = feature_manager.FeatureManager(features)

    training_features = [extractor.extract_all(sample) for sample in samples]

    # JSON output
    # with open(training_features_filename, 'w') as f:
    #   json.dump(training_features, f, indent=3)
    # print("Features saved to {}".format(training_features_filename))
    # Individual file output
    for sample in training_features:
        feature_filename = os.path.join(output_dir, sample['name'] + ".feature.csv")
        score_features_df = pd.DataFrame(data = sample['score_features'])
        score_features_df = score_features_df.add_prefix('score_')
        perf_features_df = pd.DataFrame(data = sample['perf_features'])
        perf_features_df = perf_features_df.add_prefix('perf_')
        output_df = pd.concat([score_features_df, perf_features_df], axis=1)
        output_df.to_csv(feature_filename, index=False)
        if score_features_df.empty or perf_features_df.empty or output_df.empty:
            print("WARNING: You have at least one empty feature in feature_filename")
        print("Features saved to {}".format(feature_filename))

if __name__ == "__main__":
    main()
