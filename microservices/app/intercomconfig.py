from intercom.client import Client

# enter the extended token require for list conversation feature on intercom
def configure_client():
    intercom = Client(personal_access_token='dG9rOjFlNWVlMjFjX2E4ZDNfNDY2MV9iNzFmX2VmMTMxYTU2OTUxYToxOjA=')
    return intercom
