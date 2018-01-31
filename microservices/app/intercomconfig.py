from intercom.client import Client

# enter the extended token require for list conversation feature on intercom
def configure_client():
    intercom = Client(personal_access_token='extended_access_token_here')
    return intercom
