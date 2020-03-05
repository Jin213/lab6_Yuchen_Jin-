


class Node:
	def __init__(self,data,nextPointer = None):
		self.data = data
		self.nextPointer = nextPointer
	

	def getData (self):
		return(self.data)

	def setData(self,newData):
		self.data = newData

	def getNextPointer (self):
		return(self.nextPointer)

	def setNextPointer (self,newNextPointer):
		self.nextPointer = newNextPointer



class linkList:
	def __init__ (self, size= 0, head = None, tail = None):
		self.size = size
		self.head = head
		self.tail = tail

	def getSize (self):
		return(self.size)

	def setSize(self,newSize):
		self.size = newSize

	def getHead (self):
		return(self.head)

	def setHead(self,newHead):
		self.head = newHead

	def getTail (self):
		return(self.tail)

	def setTail(self,newTail):
		self.tail = newTail

	def isEmpty(self):
		if(self.size == 0):
			return(True)
		else:
			return(False)	

	def addNode(self,d):
		newNode = Node(data = d)

		if (self.isEmpty()):
			self.setHead(newNode)
		else:
			self.getTail().setNextPointer(newNode)
			
		self.setTail(newNode)
		self.setSize(self.size +1)
		
 


def main():


	a = linkList()
	print(a.isEmpty())
	a.addNode(20)        
	a.addNode(40)
	a.addNode("AU")
	print(a.isEmpty())
	print(a.getSize())



if __name__ == "__main__":
	main()
