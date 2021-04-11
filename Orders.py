

class orderBook():
	def __init__(self):
		while True:
    			sleep(1 - time() % 1)
			self.stopOrder(self,sharePrice)

	def buy(self,shareName,sharePrice,limit):
		if userBalance<=self.allowedBudget:

			userBalance- = sharePrice
			user[shareName] = [sharePrice,limit]
	
	def sell(self,shareName,sharePrice):
		userBalance+ = sharePrice
		user.pop(shareName)

	def stopOrder(self,shareName,sharePrice):
		if sharePrice <= user[shareName][1]:
			self.sell(shareName,sharePrice)
	
	def limitOrder(self,allowedlimit):
		self.allowedBudget = allowedlimit
		

userBalance = 0
share = {"Tata": 1200; "Reliance": 1000;}

user = {}

a    =	orderBook()

budget = a.limitOrder(200)


