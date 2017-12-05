# import config
# import score_features
# import perf_features
# import json
# import logging


# def formatFeatFile(name, scoreFeats, perfFeats):
#    #reused in model.py gen()
#    return {'name':name, 'scoreFeats':scoreFeats, 'perfFeats':perfFeats}
#
# def extractTrainFeat(sample):
#    name = sample['name']
#    scoreFeats = extractFeats(sample, 'score')
#    perfFeats = extractFeats(sample, 'perf')
#    #return {'name':name, 'scoreFeats':scoreFeats, 'perfFeats':perfFeats}
#    return formatFeatFile(name, scoreFeats, perfFeats)

# def extractGenFeat(sample):
#    name = sample['name']
#    scoreFeats = extractFeats(sample, 'score')
#    #return {'name':name, 'scoreFeats':scoreFeats}
#    return formatFeatFile(name, scoreFeats, {})
#
def extract_features(sample, features_list, extractor_module):
    feats = {}
    for feature_name in features_list:
        module = __import__(extractor_module)
        feature_extraction_function = getattr(module, 'extract_' + feature_name)
        feats[feature_name] = (feature_extraction_function(sample))
    return feats

# def applyFeats(inScore, perfFeats):
#    outScore = inScore
#    for featName , featValue in perfFeats.items():
#       applyFunc = getattr(perfFeature, 'apply'+featName)
#       outScore = applyFunc(outScore, perfFeats)
#       #logging.printDebug(applyFunc)
#    ##logging.printDebug(outScore)
#    #if config.DEBUG: outScore['score'].show('text')
#    return outScore
#
# TODO: deprecate this!
# def saveJson(featList, filename):
#    with open(filename, 'w') as f:
#      json.dump(featList, f, indent=3)
##
## def loadJson(filename):
##    with open(filename, 'r') as f:
##       return json.load(f, encoding='utf-8')
#
