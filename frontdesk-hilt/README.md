# Frontdesk Project

## Overview
It demonstrates my approach to building clean, efficient, and scalable software.
## Setup Instructions
1. Clone the repo:git clone https://github.com/AkashManda854/frontdesk-assignment.git
   
2.Demo video link:https://drive.google.com/file/d/1MXaRuqQkWCbV53St6u22nvW31a7w8Del/view?usp=drive_link

 3.Project design & Architecture
   frontdesk-hilt/
    │
    ├── app/
    │   ├── __init__.py                 
    │   ├── main.py                     
    │   ├── models.py                 
│   ├── schemas.py                 
│   ├── notify.py                   
│   ├── services/                 
│   │   ├── __init__.py
│   │   ├── agent.py                
│   │   ├── help_request.py         
│   │   ├── knowledge_base.py       
│   │   └── notify.py              
│   ├── static/                   
│   ├── templates/                  
│   └── tests/                    
│
├── Frontdesk.db                  
├── requirements.txt               
├── .env                         
└── .venv/                          
4.Setup Instructions
Follow these steps to run the project locally:

#Navigate into the project directory
cd frontdesk-assignment/frontdesk-hilt

#Create a virtual environment
python -m venv .venv

#Activate the virtual environment
On Windows:
.venv\Scripts\activate
On macOS / Linux:
source .venv/bin/activate

#Install dependencies
pip install -r requirements.txt

#Run the application
uvicorn app.main:app --reload
The API will start on: http://127.0.0.1:8000

