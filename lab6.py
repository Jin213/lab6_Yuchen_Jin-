class Node:
	def __init__(self,data):
		self.data = data
		self.nextPointer = None 


	def getData(self):
		return(self.data)
	def setData(Data):
		self.Data = data
	def getnextPointer(self):
		return(self.nextPointer)
	def setnextPointer(nextPointer):
		self.nextPointer = nextPointer

		
	class LinkedList:
		def __init__(self,head,size,tail):
			self.head  = head
			self.size = size 
			self.tail = tail
		def isEmpty():
			if(size == 0):
				return True
			return False 
		def addNode(newnode):
			if(isEmpty()):
				setHead(newnode)
			setTail(newnode)


		def setHead(newnode):
			self.head = newnode

		def setTail(newnode):
			self.tail.nextPointer = newnode
			self.tail = newnode 

		def interate(self):
			currentNode = seld.head
			while(currentNode != None):
				print(currentNode.getData())
				currentNode = currentNode.getnextPointer()



		def getHead():
			return self.head
		def getTail():
			return self.tail 

	def main():
			123 = LinkedList()
			123.addNode("20")
			123.addNode("40")
			123.addNode("Au")

	if __name__ == '__main__':
		main()



