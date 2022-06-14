class Person:
  def __init__(self, clientToken, privateToken):
    self.clientToken = clientToken
    self.privateToken = privateToken

  def myfunc(self):
    print("Client Token {} , Acces Token {} ".format(self.clientToken, self.privateToken))