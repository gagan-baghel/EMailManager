import imaplib   
import email 
host ='imap.gmail.com'  
username = 'mail'
password = 'password'
def get_inbox():
    mail = imaplib.IMAP4_SSL(host)       
    mail.login(username, password)   
    mail.select("inbox")    
    _ , search_data = mail.search(None , 'UNSEEN')     
    my_message = []
    i=0
    for num in search_data[0].split(): 
        i+=1
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')   
        _, b = data[0]
        email_message = email.message_from_bytes(b)  
        for header in ['subject', 'to', 'from', 'date']:
            print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        print("mail number",i)    
        for part in email_message.walk():  
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
                if 0<email_data['body'].find("earn") or 0<email_data['body'].find("money") or 0<email_data['body'].find("affiliate"):
	                print("spam mail on ",i)
                elif 0<email_data['body'].find("examination") or 0<email_data['body'].find("result") or 0<email_data['body'].find("project"):
	                print ("important mail on ",i)
                print("="*30)
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
                print("="*30)
                if 0<email_data['html_body'].find("earn") or 0<email_data['html_body'].find("money") or 0<email_data['html_body'].find("affiliate"):
	                print ("spam mail on ",i)
                elif 0<email_data['html_body'].find("Examination") or 0<email_data['html_body'].find("result") or 0<email_data['html_body'].find("project"):
	                print ("important mail on ",i)
                print("="*30) 
        my_message.append(email_data)
    return my_message
if __name__ == "__main__":
    my_inbox = get_inbox()
    print(my_inbox)