from intercom.client import Client

def getconversations(intercom, open_time):
    filtered_convo = []
	for convo in intercom.conversations.find_all(type='conversation_message', open= True):
        	convo_dict = convo.to_dict()
        	if(int(convo_dict['created_at']) > int(open_time)):
                filtered_convo.append(convo_dict)
    return filtered_convo
