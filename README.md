1) Design and Procedure
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


2)Setup Instructions

Follow these steps to run the project locally:

#Clone the repository

git clone https://github.com/AkashManda854/frontdesk-assignment.git


#Navigate into the project directory

cd frontdesk-assignment/frontdesk-hilt


#Create a virtual environment

python -m venv .venv


Activate the virtual environment

On Windows:

.venv\Scripts\activate


On macOS / Linux:

source .venv/bin/activate


#Install dependencies

pip install -r requirements.txt


#Run the application

uvicorn app.main:app --reload


#The API will start on: http://127.0.0.1:8000
3)Demo Video Link:https://drive.google.com/file/d/1MXaRuqQkWCbV53St6u22nvW31a7w8Del/view?usp=drive_link
