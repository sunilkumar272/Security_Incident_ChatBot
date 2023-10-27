# Security_Incident_ChatBot

## Description
The is an end to end project on developing a ChatBot which is trained using Dialogflow. The ChatBot is trained on certain training phases which belong to McAfee AV, Defender AV, Symantec DLP and Bitlocker alerts. From the user perspective he is not sure of the alert triggered in his PC and can find it difficult to raise a security incident with correct team. The main aim of this project is to address this challenge and develop a chat bot which can interact with user and create a security incident based on the response provided by the user. The alerts are categorized into low, medium and high priority based on the users conversation. This project includes Dialogflow, MySQL and FasAPI backend.

## Data
Training phases used to train the model is included in Threatresponse_dataset file. All the training phrases are generated using ChatGPT by providing certain inputs. The data includes training phrases which belongs to McAfee AV, Defender AV, Symatec DLP and Bitlocker alert types. All the alerts are categorized into low, high and medium priorites.

## Requirements
pip install mysql-connector
pip install "fastapi[all]"

To test the FastAPI backend connection run the below command
"uvicorn test:app --reload"

As the Dialogflow fullfilment do not accept http URL, Download ngrok for https tunneling
Extract the zip file and copy the ngrok.exe in the destination project folder

Run "ngrok http 8000" for https tunneling

## Results.
Sample Dialogflow chat response provided by the ChatBot.
![image](https://github.com/sunilkumar272/Security_Incident_ChatBot/assets/41378148/14f29c3a-b449-492d-b0f4-7ab5f8137b0e) 
![image](https://github.com/sunilkumar272/Security_Incident_ChatBot/assets/41378148/9e5c5934-ecf4-4061-8057-b93440c0296e) 
![image] ![image](https://github.com/sunilkumar272/Security_Incident_ChatBot/assets/41378148/0178b0e0-57aa-4571-921d-05d213fd52db) 
![image](https://github.com/sunilkumar272/Security_Incident_ChatBot/assets/41378148/e95c12b6-1ec3-4761-ab75-de6c8794dbd4)












