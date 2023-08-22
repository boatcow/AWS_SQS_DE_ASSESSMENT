from flask import Flask, request, jsonify , render_template
import psycopg2
import sys
sys.path.append('..')
from commons.masking import encrypt,decrypt
from configuration import db_configuration,sqs_configuration,aws_configuration
from main.etl_main import ETL

app = Flask(__name__)



def get_db_connection():
    return psycopg2.connect(
            dbname=db_configuration["POSTGRES_DATABASE"],
            user=db_configuration["POSTGRES_USER_NAME"],
            password=db_configuration["POSTGRES_PASSWORD"],
            host=db_configuration["POSTGRES_HOST"],
            port=5432,
    )

@app.route('/load-events', methods=['POST'])
def load_events():
    number_of_events = request.json.get('number_of_events')
    print("number_of_events: ",number_of_events)
    # Here, you would write your code to load events to the database
    # After successfully loading the events:
    etl = ETL(sqs_configuration= sqs_configuration, db_configuration=db_configuration,aws_configuration=aws_configuration)
    etl.process(int(number_of_events))
    etl.close()
    return jsonify({"status": "success", "message": "Successfully Added"})

@app.route('/get-records')
def get_records():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM user_logins;")
            records = cur.fetchall()
    print("records: ",records)
    return jsonify(records)

@app.route('/get-unmasked-records')
def get_unmasked_records():
    print("unmasked")
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM user_logins;")
            records = cur.fetchall()
    unmasked_records=[]
    for rec in records:
        unmasked_record=list(rec)
        for rec in range(len(unmasked_record)):
            try:
                unmasked_record[rec]=decrypt(unmasked_record[rec])
            except:
                pass
        unmasked_records.append(tuple(unmasked_record))
    print("unmasked_records: ",unmasked_records)
    return jsonify(unmasked_records)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
