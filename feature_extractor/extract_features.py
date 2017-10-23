#!/usr/bin/env python
import config
import featureManager
import sampleLoader

def main():
# FIXME: hardcoded input path
   inputlist = "../data/corpus/split/test.list"
   # We should probably extract all features, and let training script split it

   # TODO: maybe auto-search the folder?
   trainSampList = sampleLoader.parseFileList(inputlist)

   trainFeatsList = []
   for trainSampFilename in trainSampList:
      trainSamp = sampleLoader.loadTrainSample(trainSampFilename)
      trainFeat = featureManager.extractTrainFeat(trainSamp)
      trainFeatsList.append(trainFeat)

   # trainFeatFilename = config.getTrainInFeatFilename(args)
   trainFeatFilename = "./test_features.json"
   # TODO: just use json here
   featureManager.saveJson(trainFeatsList, trainFeatFilename);

if __name__ == "__main__":
    main()
