# About

   ![image](https://user-images.githubusercontent.com/2658126/94922899-60754800-0491-11eb-8763-573a408fd630.png)
    
   Web application created to help to track expeses and plain personal finances 

# Setup

   ## Create the virtualenv
     
         virtualenv -p 3.8 venv
     
   ## Install requirements
        
        pip install -r requirements.txt
  
   ## Run migrations
        
        flask db init
        flask db migrate
        flask db update

   ## Seed database
        
   In the `config.py` change seed to true and run the project

        SEED = True

   ## Run
            
        python run.py


