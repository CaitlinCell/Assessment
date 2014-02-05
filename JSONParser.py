import json
from Video import VideoProfile

def read_dataset(filename):
        dataset = []
        json_input = json.loads(open(filename).read())
        for entry in json_input:
            dataset.append(entry)
        return dataset
        
def process_dataset(dataset):
    videos = []
    for entry in dataset:
        video = VideoProfile(entry)
        videos.append(video)
    return videos
        