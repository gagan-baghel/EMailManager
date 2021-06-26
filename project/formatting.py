msg_template = """Hello {name},
Thank you for joining {website}. I are very
happy to have you with us.
""" 
def format_msg(my_name="friends", my_website="my project"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg
