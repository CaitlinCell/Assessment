from operator import itemgetter

#Create a Content-based recommendation system
#Extensions:  We want to always return at least three recommendations,
    #Since we have no data on the user's preference, let's return a wider range of recommendations          
        #Try to match person entities/Try to match show entities
            #Beyond assessment, these could be split up
                #fans of a person can see more of the person/fans of a show see more of the show
        #Use Jaccard Distance to find similar set of features  
        #Fall back to at least match category tags 
    #Since we have a cold start situation where we don't know any user preferences, we can increase the chance that
    #they'll find what they're interested in 
 
def calculate_jaccard(profile1,profile2):
    similar = float(len(set(profile1).intersection(set(profile2))))
    together= float(len(set(profile1).union(set(profile2))))
    return similar/together
    
    
def find_related(profile,video_set):
    #In a real setting, these related videos could be indexed in case of calculating rankings each time   
    scored_profiles = {}
    entity_scored_profiles = {}    
    for comparing_profile in video_set:       
        if(profile == comparing_profile):
            pass
        entity_score = calculate_jaccard(profile.entities,comparing_profile.entities)
        entity_scored_profiles[comparing_profile] = entity_score
        #Normally this approach would require stop words but for the sake of the assignment this part is left out
        #Find close matching people entities         
        score = calculate_jaccard(profile.description.split(" "),comparing_profile.description.split(" "))
        score += calculate_jaccard(profile.title.split(" "),comparing_profile.title.split(" "))
       
        scored_profiles[comparing_profile] = score
    top_score_profiles = scored_profiles.items()
    top_entity_profiles = entity_scored_profiles.items()
    #Sort to get the best matching entities/tags we got from dbpedia  
    top_score_profiles.sort(key=itemgetter(1),reverse=True)
    top_entity_profiles.sort(key=itemgetter(1),reverse=True)
    
    return_profiles = []
    #Return the profile best matching the entities if there is one
    if top_entity_profiles[0][1] > 0.0:
        return_profiles.append(top_entity_profiles[0])
    else:
        return_profiles.append(top_score_profiles[2]) 
    #Add top two profiles from all features
    return_profiles.append(top_score_profiles[0])
    return_profiles.append(top_score_profiles[1])
    return return_profiles
    