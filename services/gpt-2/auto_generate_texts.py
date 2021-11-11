import datetime as DT
import os
import time

from sqlalchemy import create_engine

from src.generate_unconditional_samples import sample_model

# give time to the backend to initialize the db
time.sleep(180)

# Establishing connection with the postgre db

POSTGRES_USER = os.environ["BACKEND_USER"]
POSTGRES_PASSWORD = os.environ["BACKEND_PASSWORD"]
POSTGRES_DB = os.environ["BACKEND_DB"]
BACKEND_DB = os.environ["BACKEND_DB"]

SQLALCHEMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres/{BACKEND_DB}'
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password@localhost/postgres'

cursor = create_engine(SQLALCHEMY_DATABASE_URL).connect()

waiting_time = 10 # wait time in minutes 
delta_time = DT.timedelta(minutes = waiting_time)

def update_db():
    files = [os.path.join("output",file) for file in os.listdir("./output")]
    for file in files:
        with open(file,'r') as f : body = f.read()
        os.remove(file)

        if body.find("<|endoftext|>") > 0:
            body = body[:body.find("<|endoftext|>")] # discarding what is after an endoftext token
        body = body[:body.rfind('.')+1] # discarding last words that are not in a sentence

        body = body.replace("'","''")
        body = body.replace("%","%%")

        owner_id = 0
        is_human_count = 0
        is_ai_count = 0

        q = f"INSERT INTO texts (body,owner_id,is_human_count,is_ai_count)\
                VALUES ('{body}',{owner_id},{is_human_count},{is_ai_count})"
        try : cursor.execute(q)
        except Exception as e: print(e)
    print("DB UPDATED !\n")


while True:
    print("\n"+"_"*20 + " STARTING " + "_"*20)
    next_start = DT.datetime.now() + delta_time
    print("we are the " + str(DT.datetime.now()))
    print("next start : " + str(next_start))

    res = cursor.execute("SELECT * FROM texts WHERE NOT owner_id=0").all()
    n_human_texts = len(res)
    res = cursor.execute("SELECT * FROM texts WHERE owner_id=0").all()
    n_ai_texts = len(res)
    delta = n_human_texts - n_ai_texts

    if delta > 0 :
        sample_model(nsamples=delta,top_k=40)
        update_db()

    while DT.datetime.now() < next_start : time.sleep(waiting_time*60 / 10)
