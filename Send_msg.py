from twilio.rest import TwilioRestClient

account_sid= "AC862fd8efe5524ed2464e60b064d3f750" 
auth_token= "cd8b6d980a9323c1e5a743f87899be0a"
client = TwilioRestClient(account_sid,auth_token)
body=str(raw_input("Enter the message to be delivered:"))
message = client.messages.create(to="+919958195031",from_="+12013409940",body=body)
print "Message 1 send"
# message = client.messages.create(to="+919717435664",from_="+12013409940",body=body)
# print "Message 2 send"
# message = client.messages.create(to="+917065206762",from_="+12013409940",body=body)
# print "Message 3 send"
# message = client.messages.create(to="+918882759955",from_="+12013409940",body=body)
# print "Message 4 send"

print "All messages send"
print message.sid