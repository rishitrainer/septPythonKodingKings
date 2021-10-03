class Message:

    def __init__(self, txt):
        self.text = txt
        print("Message is", txt)

    def sample_message_method(self):
        print("Sample Message Method")

    def delivery(self):
        print("Delivered One to One in Person")


class SMS(Message):

    def __init__(self, txt, cell_num):
        Message.__init__(self,txt)
        self.cellNumb = cell_num
        print("SMS is :: ", self.text, self.cellNumb)

    def simple_sms_method(self):
        print(self.text, "Simple SMS Method")

    # Overriding
    def delivery(self):
        print("Delivered by Mobile Device")

    def test_parent(self):
        print(self.text, "Sent by SMS")


class WhatsApp(Message):

    def __init__(self, txt, cell_num):
        Message.__init__(self,txt)
        self.cellNumb = cell_num
        print("WhatsApp is :: ", self.text, self.cellNumb)


    def create_groups(self):
        print("Create Groups", self.cellNumb)


    def test_parent(self):
        print(self.text, "Sent by WhatsApp")


class iMessage(SMS, WhatsApp):

    def __init__(self, txt, cell_num):
        self.phone_model = "iPhone"
        SMS.__init__(self, txt, cell_num)
        WhatsApp.__init__(self, txt, cell_num)

    # Overriding
    def delivery(self):
        print("Delivered by Mobile Device Using iPhone internet")

'''
sms1 = SMS("Hi, Meet me asap", "039821903821")
sms1.delivery()
sms1.sample_message_method()
sms1.simple_sms_method()
'''



imsg = iMessage("Hi, Meet me asap", "039821903821")
imsg.delivery()
imsg.create_groups()
imsg.test_parent()
