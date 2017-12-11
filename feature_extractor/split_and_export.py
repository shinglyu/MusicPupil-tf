from sklearn.model_selection import KFold
import pandas as pd;

def split_train_test(samples, n_splits):
    kf = KFold(n_splits=n_splits)

    output = []
    for train, test in kf.split(samples):
        output.append({
            "training": [samples[idx] for idx in train],
            "testing": [samples[idx] for idx in test],
        })
    return output

def export_to_csv(samples, filename):
    # Sample format:
    # [{"score_features": {"name":[...]}, "perf_features":{...}}]

    if len(samples) == 0:
        raise Exception("Empty sample, nothing to export to CSV")


    score_features_dfs = []
    perf_features_dfs = []
    for sample in samples:
        score_features_dfs.append(pd.DataFrame(data=sample['score_features']))
        perf_features_dfs.append(pd.DataFrame(data=sample['perf_features']))
    all_score_features_df = pd.concat(score_features_dfs)
    all_perf_features_df = pd.concat(perf_features_dfs)

    all_data = pd.concat([all_score_features_df, all_perf_features_df], axis=1)

    all_data.to_csv(filename, index=False)

def export_all_to_csv(splits, filename_base):
    for idx, split in enumerate(splits):
        export_to_csv(split['training'], "{base}_{idx}_{usage}.csv".format(base=filename_base, idx=idx, usage="training"))
        export_to_csv(split['testing'], "{base}_{idx}_{usage}.csv".format(base=filename_base, idx=idx, usage="training"))

def main():
    raise NotImplementedError

if __name__ == "__main__":
    main()
