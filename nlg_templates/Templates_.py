import numpy as np

Classes = "Pieces"
QueryResult= "Applied, Athlete, Decorative, Fine, Performance, Photographer, Plastic, Visual"
ResponseInformation =""

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

ResponseInformation = TemplateGeneratorInformation(Classes, QueryResult)

Classes = "periods"
DataPropertiesValues = "Las meninas"
QueryResult= "Contemporary"
ResponseList =""

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
        
         Templates = [DataPropertiesValues.title() + " belongs to the " + Classes + ": " +  QueryResult,
                     "In Barcelona, you can find art from multiple periods. In particular, " + DataPropertiesValues.title() + " belongs to " + Classes + " :" +  QueryResult,
                     "Contemporary, Modern, Classic... What " + Classes + " periods do you prefer? Well... In this case " + DataPropertiesValues.title() + " belongs to the following ones: " +  QueryResult]
            
    if QueryResult != "":
        Index = np.random.randint(0, len(Templates))
        ResponseList = Templates[Index]
    else:
        ResponseList = QueryResult
        
    print(ResponseList)
    return ResponseList

ResponseList = TemplateGeneratorList(Classes, DataPropertiesValues, QueryResult)

dataProperties = "tickets"
DataPropertiesValues = "Design Museum"
QueryResult= "street whatever"
ResponseSpecific =""

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
        
         Templates = [DataPropertiesValues.title() + " has the following " + dataProperties + " schedule: " + QueryResult,
                      "Please find the schedule for " + DataPropertiesValues.title() + ": " + QueryResult,
                      "Most museums in Barcelona are opened during all the week. But please check below the schedule for " + DataPropertiesValues.title() + ": " + QueryResult,
                      "Check out if " + DataPropertiesValues.title() + " is opened the day you are interested in going. Find the schedule below! " + QueryResult]
         
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

ResponseSpecific = TemplateGeneratorSpecific(dataProperties, DataPropertiesValues, QueryResult)