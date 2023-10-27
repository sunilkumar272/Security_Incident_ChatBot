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
![image](https://github.com/sunilkumar272/Security_Incident_ChatBot/assets/41378148/ece14c74-5c67-4e81-95fd-dfb6a2e9d8c5)
![image](https://github.com/sunilkumar272/Security_Incident_ChatBot/assets/41378148/ebdbd82c-d030-4623-90a8-3d0dc96ca824)







