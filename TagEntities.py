import spotlight as sp
from Video import Entity
 
def tag_video(video):
    #Future work that would give improvement would be to rank entities in the title higher than the description
    #For the assessment we have to have the length above a cut off before querying spotlight since an exception will
    #be thrown if we get no response    
    #if len(video.title.split(" ")) > 7:
    result = run_query(video.title)
    process_result(video,result)
    #if len(video.description.split(" ")) > 6:    
    result = run_query(video.description)
    process_result(video,result)
    return video

def run_query(query):
     #Use a low confidence in order to esure we get a response
    confidence = 0.2
    support = 10 
    try:
        annotations = sp.annotate('http://spotlight.dbpedia.org/rest/annotate',query,confidence,support)
    except:
        print "No resources returned"
        annotations = []
    return annotations
   

def process_result(video,annotations):
    results = annotations   
    for r in results:
        score = r.get('similarityScore',0)
        if score > .18:
            entity = Entity()                  
            entity.set_surface_name(r.get('surfaceForm',""))
            entity.extract_type(r.get('types',""))               
            entity.set_score(score)
            video.append_entity(entity)
    
            

