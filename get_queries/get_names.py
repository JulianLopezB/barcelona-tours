from owlready2 import *


class SparqlQueriesNames:
    def __init__(self):
        my_world = World()
        my_world.get_ontology("/Users/josemiguelflorescontro/Desktop/Museums.owl").load() #path to the owl file is given here
        sync_reasoner(my_world)  #reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()
    
    def search(self,objectProperty,objectValue):
        #Search query is given here
        #Base URL of your ontology has to be given here
        query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \
        PREFIX owl: <http://www.w3.org/2002/07/owl#> \
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\
        PREFIX uni:<http://www.semanticweb.org/josemiguel/ontologies/2018/11/untitled-ontology-10#>"\
        "SELECT DISTINCT ?aname ?bname  \
        WHERE {\
          ?a uni:has"+objectProperty+" ?b .\
          ?a uni:Name "+'"'+objectValue+'"'+"^^xsd:string .\
          ?b uni:Name ?bname .}"
    
        #remember to place the filter according to interests of the user. For example, the name of a museum:
        #"MACBA: Museu d'Art Contemporani de Barcelona"^^xsd:string
        #query is being run
        resultsList = self.graph.query(query)
    
        #creating json object
        response = []
        for item in resultsList:
           s = str(item['bname'].toPython())
           s = re.sub(r'.*#',"",s)
           response.append(s)
    
        print(response) #just to show the output
        return ", ".join(response).replace("_", " ")

runQuery = SparqlQueriesNames()
QueryResponse = runQuery.search("Produced","Pablo picasso")

