import config
import os.path
from music21 import converter

def load_file_list(input_list):
   with open(inputList) as f:
       return parse_file_list(f.readlines(), os.path.dirname(inputList))

def convert_to_full_path(lines, dirname):
   #TODO: change to json format
   return list(map(lambda x:os.path.join(dirname, x.strip()), lines))


# Utility for loading the score, metadata and performance in one go
def load_training_sample(sample_name):

   score_name = sample_name+ ".score.xml";
   meta_name  = sample_name+ ".meta";
   perf_name  = sample_name+ ".perf.mid";

   score = converter.parse(score_name);
   meta = load_metadata(meta_name)
   perf = converter.parse(perf_name);
   name = os.path.basename(sample_name)
   return {'name': name, 'score':score, 'meta':meta, 'perf':perf}

# def loadGenScore(sample_name):
#    score_name = sample_name + ".score.xml";
#    meta_name = sample_name  + ".meta";
#
#    score = converter.parse(score_name);
#    meta = loadMetadata(meta_name)
#    name = os.path.basename(sample_name)
#    return {'name': name, 'score':score, 'meta':meta}
#
def load_metadata(meta_name):
   try:
      with open(meta_name) as f:
          meta = list(map(lambda x: x.strip(), f.readlines()))
   except IOError: #e.g. File not found
      meta = []
   return meta
