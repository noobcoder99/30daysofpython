import datetime


class MessageUser():
    user_details = []
    messages = []
    base_message = """Hi {name}! 

Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!

Team CFE
"""
    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower() 
        amount = "%.2f" %(amount)
        detail = {
            "name": name,
            "amount": amount,
        } 
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        detail['date'] = date_text
        if email is not None: # if email != None
            detail["email"] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                self.messages.append(new_msg)
            return self.messages
        return []


def some_rando():
    print("yehahahsdfa")



unf_message = """Hi {name}! 

Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!

Team CFE
"""


def make_messages(names, amounts):
    messages = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()
        text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            """
            Here's a simple solution to capitalize 
            everyone's name prior to sending
            """
            name = name[0].upper() + name[1:].lower() 
            """
            Did you get the bonus??
            """
            new_amount = "%.2f" %(amounts[i])
            new_msg = unf_message.format(
                    name=name,
                    date=text,
                    total=new_amount
                )
            i += 1
            print(new_msg)


