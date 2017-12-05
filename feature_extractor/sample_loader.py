import os.path
from music21 import converter


def convert_to_full_path(lines, dirname):
   #TODO: change to json format
   return list(map(lambda x:os.path.join(dirname, x.strip()), lines))



# def loadGenScore(sample_name):
#    score_name = sample_name + ".score.xml";
#    meta_name = sample_name  + ".meta";
#
#    score = converter.parse(score_name);
#    meta = loadMetadata(meta_name)
#    name = os.path.basename(sample_name)
#    return {'name': name, 'score':score, 'meta':meta}
#

class SampleLoader():
    def __init__(self, base_path):
        self.base_path = base_path

    def _get_score_path(self):
        return self.base_path + ".score.xml"

    def _get_performance_path(self):
        return self.base_path + ".perf.mid"

    def _get_meta_path(self):
        return self.base_path + ".meta"

    def _load_metadata(self):
        try:
            with open(self._get_meta_path()) as f:
                meta = list(map(lambda x: x.strip(), f.readlines()))
        except IOError: #e.g. File not found
            meta = []
        return meta

    # Utility for loading the score, metadata and performance in one go
    def load_training_sample(self):

        try:
            score = converter.parse(self._get_score_path());
            perf = converter.parse(self._get_performance_path());
            meta = self._load_metadata()
            name = os.path.basename(self.base_path)
        except IOError as e:
            raise Exception("The sample has a missing file, abort: " + str(e))

        return {'name': name, 'score':score, 'meta':meta, 'perf':perf}
