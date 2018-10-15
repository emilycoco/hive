import contextio as c
import os

# from instance import config as secret_config
config_name = os.getenv('FLASK_CONFIG')

secret_config = {
    'SECRET_KEY': 'p9Bv<3Eid9%$i01',
    'SQLALCHEMY_DATABASE_URI': 'mysql://hive_admin:hive2018@localhost/hive_db',
    'CONSUMER_KEY': 'bvhda3dn',
    'CONSUMER_SECRET': 'XGToXtDKTHAu5pqy',
    'API_VERSION': '2.0',
    'ACCOUNT_ID': '5bb99129ef673a6473029ce2'
}

context_io = c.ContextIO(
    consumer_key=secret_config['CONSUMER_KEY'],
    consumer_secret=secret_config['CONSUMER_SECRET'],
    api_version="lite",
    debug=True

)


def main():
    user = c.User(context_io, {"id": secret_config['ACCOUNT_ID']})
    print('Creating webhook for user: ', user)
    user.post_webhook(
        callback_url="http://02090c28.ngrok.io/v1/mail/ingest",
        failure_notif_url="http://02090c28.ngrok.io/v1/mail/ingest-errors",
        include_body=1
    )


if __name__ == '__main__':
    main()
