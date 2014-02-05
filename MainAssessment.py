from JSONParser import read_dataset, process_dataset 
import TagEntities
import Recommender
    
if __name__ == '__main__':
    #Read in DataSet
    dataset = read_dataset("Resources/DataSet.json")
    #Turn dataset into video elements
    video_set = process_dataset(dataset) 
    #Tag Entities to video profiles using spotlight
    for video in video_set:
        TagEntities.tag_video(video)
    #Print video profiles and related videos to output file    
    with open("output.txt", "wb") as fo:
        for video in video_set:
            fo.write("__________________________________________________\n")
            related_list = Recommender.find_related(video_set[0],video_set)
            video.print_video(fo)
            fo.write("\n-------------------------")
            fo.write("\nRelated Videos: ")
            i=0
            for (match,score) in related_list:
                i += 1
                fo.write("\n\t"+i+": " )           
                match.print_video(fo)
                fo.write("\n------------\n")