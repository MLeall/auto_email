import independentsoft.msg as imsg

def to_msg(email_body=str):
    to_address = str(input("\nEnter the recipient's email address:\n> ")) 
    msg = imsg.Message()
    
    # Default recipient's info
    recipient1 = imsg.Recipient()
    recipient1.address_type = "SMTP"
    recipient1.display_type = imsg.DisplayType.MAIL_USER
    recipient1.object_type = imsg.ObjectType.MAIL_USER
    recipient1.display_name = to_address
    recipient1.recipient_type = imsg.RecipientType.TO

    msg.subject = "RFC review"
    msg.body = email_body
    msg.display_to = recipient1.display_name
    msg.recipients.append(recipient1)
    msg.message_flags.append(imsg.MessageFlag.UNSENT)
    msg.store_support_masks.append(imsg.StoreSupportMask.CREATE)

    msg.save('email_template.msg')
