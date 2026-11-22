import mysql.connector

def get_database_connection():
    connection = mysql.connector.connect(
        host='gateway01.ap-northeast-1.prod.aws.tidbcloud.com',
        user='4EncZAzKEVGs9aS.root',
        password='Cwz1vdUrH3Ad8Py3',
        database='u2m7D6FOAiwPq6gP',
        port=4000
    )

    return connection
