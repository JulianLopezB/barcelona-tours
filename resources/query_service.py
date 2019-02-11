"""
Tours Barcelona Museums

Copyright (C) 2019  Jose Fernando Nuñez, José Miguel Flores, Julián López, Sergi Mas

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

import media_aggregator
import numpy as np
from json import loads as _l
import query_extractor as _qe
from flask_restful import Resource, reqparse
from media_aggregator import (shorten_news, get_gkg, GuardianAggregator as _ga, NYTAggregator as _nyt)
from owlready2 import *

import spacy as _s
_nlp = _s.load('en')

#Input For Query Function
def InputsForQuery(InputQuestion):

    classes = ["artists", "museums", "periods", "pieces", "produced"] # Classes (No produced class but needed)
    datapropertyValues = ["picasso museum", "wax museum", "design museum", "pablo picasso", "mario eskenazi", "las meninas", "what are scientific revolutions and other essays", "prize for economic research book cover page"] # Name: Data Property Value
    dataProperties = ["address", "price", "hours", "neighborhood", "tickets", "name", "year"] # Data Property
    
    _classes = ""
    _datapropertiesValues = ""
    _dataProperties = ""

    for _class in classes:
        if _class in InputQuestion:
            _classes = _class
    
    for _datapropertyValue in datapropertyValues:
        if _datapropertyValue in InputQuestion:
            _datapropertiesValues = _datapropertyValue
    
    for _dataProperty in dataProperties:
        if _dataProperty in InputQuestion:
                _dataProperties = _dataProperty

    return _classes, _datapropertiesValues, _dataProperties

#Query Classes
class SparqlQueriesClasses:
    def __init__(self):
        my_world = World()
        my_world.get_ontology("/Users/josemiguelflorescontro/Desktop/Museums.owl").load() #path to the owl file is given here
        sync_reasoner(my_world)  #reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()
    
    def search(self, Class_):
        #Search query is given here
        #Base URL of your ontology has to be given here
        query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \
        PREFIX owl: <http://www.w3.org/2002/07/owl#> \
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\
        PREFIX uni:<http://www.semanticweb.org/josemiguel/ontologies/2018/11/untitled-ontology-10#>"\
        "SELECT ?class WHERE {?class rdfs:subClassOf uni:"+Class_+"}"
    
        #query is being run
        resultsList = self.graph.query(query)
    
        #creating json object
        response = []
        for item in resultsList:
           s = str(item['class'].toPython())
           s = re.sub(r'.*#',"",s)
           response.append(s)

        print(response) #just to show the output
        return ", ".join(response)

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
        return ", ".join(response)

class SparqlQueriesSpecific:
    def __init__(self):
        my_world = World()
        my_world.get_ontology("/Users/josemiguelflorescontro/Desktop/Museums.owl").load() #path to the owl file is given here
        sync_reasoner(my_world)  #reasoner is started and synchronized here
        self.graph = my_world.as_rdflib_graph()
    
    def search(self,superClass, objectProperty, objectValue):
        #Search query is given here
        #Base URL of your ontology has to be given here
        query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \
        PREFIX owl: <http://www.w3.org/2002/07/owl#> \
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\
        PREFIX uni:<http://www.semanticweb.org/josemiguel/ontologies/2018/11/untitled-ontology-10#>"\
        "SELECT ?rname ?lname \
        WHERE {\
        ?inst a uni:"+superClass+" .\
        ?inst uni:Name "+'"'+objectValue+'"'+"^^xsd:string .\
        ?inst uni:"+objectProperty+" ?lname .\
        }"
    
        #remember to place the filter according to interests of the user. For example, the name of a museum:
        #"MACBA: Museu d'Art Contemporani de Barcelona"^^xsd:string
        #query is being run
        resultsList = self.graph.query(query)
    
        #creating json objectPiece1

        response = []
        for item in resultsList:
           s = str(item['lname'].toPython())
           s = re.sub(r'.*#',"",s)
           response.append(s)
    
        print(response) #just to show the output
        return ", ".join(response).replace("_", " ")

def TemplateGeneratorInformation(Classes, QueryResult):
    Templates = [ "The different type of " + Classes + " that I have available in my database are: " + QueryResult,
                      "If you are interested, I can show you more information about the following types of " + Classes + ": " + QueryResult,
                      "Thanks for booking your journey with Tours Barcelona Museums. We have information about the following types of " + Classes + " : " + QueryResult,
                      "We are very glad to help you! We can give you information about the following types of " + Classes + " : " + QueryResult,
                      "Remember we are here tou help you! These are the different types of " + Classes + " : " + QueryResult]
        
    if QueryResult != "":
        Index = np.random.randint(0, len(Templates))
        ResponseInformation = Templates[Index]
    else:
        ResponseInformation = QueryResult
            
    print(ResponseInformation)
    return ResponseInformation

def TemplateGeneratorList(Classes, DataPropertiesValues, QueryResult):
    
    if Classes == "artists":
        
        Templates = [DataPropertiesValues.title() + " has pieces of art from the following " + Classes + ": " +  QueryResult,
                     Classes.capitalize() + " are building a decisive role within museums. In particular, "+ DataPropertiesValues.title() + " has pieces from the following ones: " +  QueryResult,
                     Classes.capitalize() + " are increasingly seen as creative professionals and influencers. " + DataPropertiesValues.title() + " has multiple pieces from some of them: " +  QueryResult,
                     Classes.capitalize() + " can have many roles in a museum or gallery. Regarding your question, I can tell you that " + DataPropertiesValues.title() + " has multiple pieces from the following " + Classes + ": " +  QueryResult]
    
    if Classes == "pieces":
        
        Templates = [DataPropertiesValues.title() + " has the following " + Classes +" of art: " +  QueryResult,
                     "Inside " + DataPropertiesValues.title() + " you will be able to find some of the following " + Classes + " of art: " + QueryResult,
                     DataPropertiesValues.title() + " is a very diverse museum. In particular, you will be able to see the following " + Classes + ": " +  QueryResult,
                     "Unfortunately, you won't be able to find the Mona Lisa in Barcelona! But you can definitely check the following " + Classes + " inside " + DataPropertiesValues.title() + ": " +  QueryResult]
    
    if Classes == "produced":
        
         Templates = [DataPropertiesValues.title() + " is a very creative artist. He has " + Classes + " the following pieces of art: " +  QueryResult,
                     DataPropertiesValues.title() + " has "+ Classes + " the following pieces of art: " +  QueryResult,
                     "Many art pieces have been " + Classes + " by " + DataPropertiesValues.title() + ". Some of them are the following ones: " +  QueryResult,
                     "Not Leonardo Da Vinci, but also a great artist! Here you have a list of the pieces of art " + DataPropertiesValues.title() + " has " + Classes + ": " + QueryResult]
    
    if Classes == "periods":
        
         Templates = [DataPropertiesValues.title() + " belongs to the following " + Classes + ": " +  QueryResult,
                     "In Barcelona, you can find art from multiple periods. In particular, " + DataPropertiesValues.title() + " belongs to the following " + Classes + ": " +  QueryResult,
                     "Contemporary, Modern, Classic... What " + Classes + " periods do you prefer? Well... In this case " + DataPropertiesValues.title() + " belongs to the following ones: " +  QueryResult]
            
    if QueryResult != "":
        Index = np.random.randint(0, len(Templates))
        ResponseList = Templates[Index]
    else:
        ResponseList = QueryResult
        
    print(ResponseList)
    return ResponseList

def TemplateGeneratorSpecific(dataProperties, DataPropertiesValues, QueryResult):
    
    if dataProperties == "address":
        
        Templates = ["The " + dataProperties + " of " + DataPropertiesValues.title() + " is: " + QueryResult,
                     "You will find " + DataPropertiesValues.title() + " if you go to the following " + dataProperties + ": " + QueryResult,
                     "Here is the " + dataProperties + " for " + DataPropertiesValues.title() + ": " + QueryResult,
                     "Barcelona is not a very big city! I am happy to share the " + dataProperties + " for " + DataPropertiesValues.title() + " with you: " + QueryResult]

    if dataProperties == "price":
        
        Templates = ["The " + dataProperties + " you need to pay for " + DataPropertiesValues.title() + " is: " + QueryResult,
                     "Most of the museums in Barcelona are not very expensive. For you to be able to enter to " + DataPropertiesValues.title() + " you will need to pay " + QueryResult,
                     "Some museums have discounts! Check out if you can have a discount. In the case of " + DataPropertiesValues.title() + " you will need to pay " + QueryResult + " (if no discount is applied)",
                     "It is great to have fun for free! Unfortunately, you will need to pay " + QueryResult + " for you to be able to enter " + DataPropertiesValues.title()]
        
    if dataProperties == "hours":
        
         Templates = [DataPropertiesValues.title() + " has the following " + dataProperties + " schedule: \n" + QueryResult,
                      "Please find the schedule for " + DataPropertiesValues.title() + ": \n" + QueryResult,
                      "Most museums in Barcelona are opened during all the week. But please check below the schedule for " + DataPropertiesValues.title() + " below: \n" + QueryResult,
                      "Check out if " + DataPropertiesValues.title() + " is opened the day you are interested in going. Find the schedule below! \n" + QueryResult]
         
    if dataProperties == "neighborhood":
        
         Templates = [DataPropertiesValues.title() + " is located in the " + dataProperties + " " + QueryResult,
                      "There are too many " + dataProperties + "s" + " in Barcelona! In particular, " + DataPropertiesValues.title() + " is located in "  + QueryResult,
                      DataPropertiesValues.title() + " located in the beatiful " + dataProperties + " of " + QueryResult,
                      "I really love Poblenou! This is the place where I was created! " + DataPropertiesValues.title() + " is located in " + QueryResult]
    
    if dataProperties == "tickets":
        
        Templates = ["You can buy " + dataProperties + " for " + DataPropertiesValues.title() + " if you access to the following link: " + QueryResult,
                     "Follow this link to buy your tickets for " + DataPropertiesValues.title() + ": " + QueryResult,
                     "For more information about " + dataProperties + " please go to " + QueryResult,
                     "The best way to buy " + dataProperties + " is online. Here is the webpage to buy " + dataProperties + " for " + DataPropertiesValues.title() + ": " +  QueryResult]
        
    if dataProperties == "year":
        
        Templates = ["The " + dataProperties + " of " + DataPropertiesValues.title() + " is " + QueryResult,
                     DataPropertiesValues.title() + " was created in " + QueryResult,
                     "Old or New piece of art...? Well... " + DataPropertiesValues.title() + " was created in " + QueryResult,
                     "I am in love with old pieces of art. In this case, " + DataPropertiesValues.title() + " was created in " + QueryResult]
        
    if QueryResult != "":
        Index = np.random.randint(0, len(Templates))
        ResponseSpecific = Templates[Index]
    else:
        ResponseSpecific = QueryResult
        
    print(ResponseSpecific)
    return ResponseSpecific

class QueryService(Resource):
    def post(self):
        args = parser.parse_args()
        result = clf.predict(args["data"])
        return result[0], 200 if result[1] else 400


class QueryAnalyzer(object):
    def __init__(self):
        self._query_extractor = _qe.QueryExtractor()

    def predict(self, data):
        s=_qe.QueryExtractor()
        _classes, _datapropertiesValues, _dataProperties = InputsForQuery(data.lower())
        try:
            if _classes != "" and _datapropertiesValues == "" and _dataProperties == "":
                print("Information Question")
                print(_classes)
                # Query Classes 
                runQuery = SparqlQueriesClasses()
                Queryresponse = runQuery.search(_classes.capitalize())
                response = TemplateGeneratorInformation(_classes, Queryresponse)
                done = response
                if len(response) <= 0:
                    response = "Sorry, no relevant results were returned."
                i, done = 0, response
                while (not done) and ((i + 1) < len(response)):
                    i += 1
                    done = response 
            elif _classes != "" and _datapropertiesValues != "" and _dataProperties == "":
                print("List Question")
                print(_datapropertiesValues)
                print(_classes)
                # Query Names 
                runQuery = SparqlQueriesNames()
                Queryresponse = runQuery.search(_classes.capitalize(),_datapropertiesValues.capitalize())
                response = TemplateGeneratorList(_classes, _datapropertiesValues, Queryresponse)
                if len(response) <= 0:
                    response = "Sorry, no relevant results were returned."
                i, done = 0, response
                while (not done) and ((i + 1) < len(response)):
                    i += 1
                    done = response
            elif _dataProperties != "" and _datapropertiesValues != "" and _classes == "":
                print("Specific Question")
                print(_datapropertiesValues)
                print(_dataProperties)
                print("museums")
                runQuery = SparqlQueriesSpecific()
                Queryresponse = runQuery.search("Museums", _dataProperties.capitalize(), _datapropertiesValues.capitalize())
                response = TemplateGeneratorSpecific(_dataProperties, _datapropertiesValues, Queryresponse)
                if len(response) <= 0:
                    response = "Sorry, no relevant results were returned."
                i, done = 0, response
                while (not done) and ((i + 1) < len(response)):
                    i += 1
                    done = response
            else:
                # Knowledge query
                done = get_gkg(self._query_extractor.get_knowledge_tokens(data))
            ret_val = {"urls": done}
            if not done:
                ret_val["phrase"] = "Sorry, no valid results were returned."
            return ret_val, done
        except Exception as e:
            return {"phrase": "Sorry, something unexpected happened.", "original_exception": e.message}, False

parser = reqparse.RequestParser()
parser.add_argument("data")
clf = QueryAnalyzer()

