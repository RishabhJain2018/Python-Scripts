from twilio.rest import TwilioRestClient

account_sid= "AC862fd8efe5524ed2464e60b064d3f750" 
auth_token= "cd8b6d980a9323c1e5a743f87899be0a"
client = TwilioRestClient(account_sid,auth_token)
body=str(raw_input("Enter the message to be delivered:"))
for i in range(0,1):
	message = client.messages.create(to="+918375867839",from_="+16464938392",body=body)
	mess=client.messages.create(to="+918375867839",from_="+16464938392",body="hello world")
print message.sid