import numpy as np

split_input = "information"

# split1 = "list"
# split2 = "information"

topic = "Epochs"

result =["Appplyes, Contemporary, Automatic"]
# result =[""]

templates = [ "The "+ split_input +" of "+ topic +" that I have available in my database are: " + result[0],
             "If you are interested, I can show you more information about the following "+ topic+ ":"+ result[0]]

if result[0] != "":
    index = np.random.randint(0, len(templates))
    print(templates[index])



    def TemplateGen(self, QuestionType, Topic, QueryResult):
        Templates = [ "The " + QuestionType + " of " + Topic + " that I have available in my database are: " + QueryResult,
                "If you are interested, I can show you more information about the following " + Topic + ":" + QueryResult]
        if QueryResult[0] != "":
            Index = np.random.randint(0, len(Templates))
            Response = Templates[Index]
        else:
            Response = QueryResult
        return Response
    
        