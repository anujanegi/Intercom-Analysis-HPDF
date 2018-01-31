from intercom.client import Client

def getconversations(intercom, open_time):
    open_convo = []
	for convo in intercom.conversations.find_all(type='conversation_message', open= True):
            #appendinf list of open converstions with dictionary of convo object of intercom.conversation.Conversation
            open_convo.append(convo.to_dict())
    return open_convo

def filterconversations(conversationlist, open_time):
    filtered _convo = []
    for convo in conversationlist:
        if(int(convo['created_at']) > int(open_time)):
            # append to filtered_convo if open for greater than open_time
            filtered_convo.append(convo)
    return filtered_convo
