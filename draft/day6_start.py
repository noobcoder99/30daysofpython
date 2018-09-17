import datetime
default_names = ["justin", "john"]
default_amounts = [123, 94.22]

#message = """Hi! > change to variable name
unf_message = """Hi {name}!


Thanks for yor purchse on {date}.
The purchse total was ${total}.

Team CFE
"""




def make_messages(names, amounts):
    message = []
    if len(names) == len(amounts):
        i = 0
        today = datetime.date.today()
        text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        for name in names:
            new_msg = unf_message.format(
                    name=name,
                    date=text,
                    total=amounts[i]
                )
            i += 1
            print(new_msg)

make_messages(default_names,default_amounts)
