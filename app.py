from __future__ import absolute_import
from google.oauth2 import service_account
import googleapiclient.discovery


import os
if __name__ == '__main__':

    SCOPES = ['https://www.googleapis.com/auth/cloud-translation']

    '''
    This script needs google-api-python-client (already listed  in the Pipfile)


    1. Create your Google Service Account (https://developers.google.com/identity/protocols/OAuth2ServiceAccount)
    2. Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to the file path of the JSON file that contains 
    your service account key. (https://cloud.google.com/translate/docs/quickstart?csw=1)
    '''
    SERVICE_ACCOUNT_FILE = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    translation = googleapiclient.discovery.build('translate', 'v2', credentials=credentials)

    # Language source, target configuration (https://cloud.google.com/translate/docs/languages)
    SOURCE_LANGUAGE = 'en'
    TARGET_LANGUAGE = 'es'

    print(translation.translations().list(
        source=SOURCE_LANGUAGE,
        target=TARGET_LANGUAGE,
        q=['How are you?', """Let's meet tomorrow at the office"""]
    ).execute())
    print('Finished')
