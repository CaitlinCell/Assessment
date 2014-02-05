import re
import unicodedata

class VideoProfile:   
    def __init__(self,data):
            self.title = self.strip_normalize_text(data['title'])             
            self.description = self.strip_normalize_text(data['description'])
            self.entities = []
            self.categories = [] 
    
    def append_entity(self,entity):
        self.entities.append(entity)
    
    def strip_normalize_text(self,text):
        stripped_text = re.sub(r'[-+\\\[\]()?><=*\:\"]'," ",text)
        normalized_text = unicodedata.normalize('NFKD', stripped_text).encode('ascii','ignore').strip()
        return normalized_text
    
    def print_video(self,fo):
        fo.write("Video Title: "+ self.title)
        fo.write("\nDescription: "+ self.description)
        fo.write("\nTags")
        for entity in self.entities:
             fo.write("\nName: "+ entity.surface_form+ " Type: "+ entity.get_head_type())

  
class Entity:
    def __init__(self):
        self.type = []
        self.surface_form = ""
        self.score = 0
    
    def extract_type(self,types):
        extracted_types = re.findall(":([A-Za-z\d\s]+),", types)
        self.type = extracted_types
    
    def set_type(self,types):        
        for entityType in types.split(','):
            self.type.append(entityType)            
    
    def set_surface_name(self,name):
        self.surface_form = name
    
    def set_score(self,score):
        self.score = score
    
    def get_head_type(self):
        if(len(self.type)> 0):
            return self.type[0]
        else:
            return "No Type"
