from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import database_helper
import session_helper

app = FastAPI()

inprogress_incidents = {}

@app.post("/")
async def handle_request(request: Request):
    # Get the JSON data from the request
    payload = await request.json()

    """Extract the necessary information from the payload using 
    the structure of the WebhookRequest from Dialogflow"""
    
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    session_id = session_helper.extract_session_id(output_contexts[0]["name"])

    intent_handler_dict = {
        'incident.add-contex:ongoing-incident-low': add_to_low,
        'incident.add-contex:ongoing-incident-medium': add_to_medium,
        'incident.add-contex:ongoing-incident-high': add_to_high,
        'track.incident-context:ongoing incident': track_incident
    }

    return intent_handler_dict[intent](parameters, session_id)

# Defining a function to save and insert the incident details to the database
def save_to_db(incident: str):
    next_incident_id = database_helper.get_next_incident_id()
    
    # Inserting the incident tracking status
    database_helper.insert_incident_tracking(next_incident_id, "in progress")

    return next_incident_id

# Defining a function to create a low priority incident
def add_to_low(parameters: dict, session_id: str):
    alert_name = parameters["Alert-name"][0]

    inprogress_incidents[session_id] = alert_name
    
    incident = inprogress_incidents[session_id]
    
    incident_id = save_to_db(incident)
    
    if incident_id == -1:
        fulfillment_text = "Sorry, I couldn't process yourincident due to a backend error. " \
                               "Please place a new incident again"
    else:
        fulfillment_text = f"A Security incident under {alert_name} category  with low priority has been created. " \
                           f"Here is your incident id # {incident_id}. " 
                           
    del inprogress_incidents[session_id]


    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

# Defining a function to create a medium priority incident
def add_to_medium(parameters: dict, session_id: str):
    alert_name = parameters["Alert-name"][0]
    
    inprogress_incidents[session_id] = alert_name
    
    incident = inprogress_incidents[session_id]
    incident_id = save_to_db(incident)
    if incident_id == -1:
        fulfillment_text = "Sorry, I couldn't process yourincident due to a backend error. " \
                               "Please place a newincident again"
    else:
        fulfillment_text = f"A Security incident under {alert_name} category  with medium priority has been created. " \
                           f"Here is your incident id # {incident_id}. " 
                           
    del inprogress_incidents[session_id]


    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })

# Defining a function to create a high priority incident
def add_to_high(parameters: dict, session_id: str):
    alert_name = parameters["Alert-name"][0]

    inprogress_incidents[session_id] = alert_name
    
    incident = inprogress_incidents[session_id]
    incident_id = save_to_db(incident)
    if incident_id == -1:
        fulfillment_text = "Sorry, I couldn't process yourincident due to a backend error. " \
                               "Please place a newincident again"
    else:
        fulfillment_text = f"A Security incident under {alert_name} category  with high priority has been created. " \
                           f"Here is your incident id # {incident_id}. " 
                           
    del inprogress_incidents[session_id]


    return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })


def track_incident(parameters: dict, session_id: str):
   incident_id = int(parameters['number'])
   incident_status = database_helper.get_incident_status(incident_id)
   if incident_status:
       fulfillment_text = f"The incident status for incident id: {incident_id} is: {incident_status}"
   else:
       fulfillment_text = f"Noincident found with incident id: {incident_id}"

   return JSONResponse(content={
        "fulfillmentText": fulfillment_text
    })