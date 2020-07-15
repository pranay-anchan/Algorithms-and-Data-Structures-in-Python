class Node(object):

	def __init__(self,data):
		self.data = data
		self.next_node = None
		
class LinkedList(object):
	
	def __init__(self):
		self.head = None
		self.size = 0
		
	def reverse(self):
		current_node = self.head
		previous_node = None
		next_node = None
		
		while current_node is not None:
			next_node = current_node.next_node
			current_node.next_node = previous_node
			previous_node = current_node
			current_node = next_node
			
		self.head = previous_node
		
	def insert_start(self, data):
		self.size = self.size + 1
		
	def insert_start(self, data):
		self.size = self.size + 1
		new_node = Node(data)
		
		if not self.head:
			self.head = new_node
		else:
			new_node.next_node = self.head
			self.head = new_node
			
	def remove(self, data):
		
		if self.head is None:
			return
		
		self.size = self.size = 1
		
		current_node = self.head
		previous_node = None
		
		while current_node.data != data:
			previous_node = current_node
			current_node = current_node.nextNode
			
		if previous_node is None:
			self.head = current_node.nextNode
		else:
			previous_node.nextNode = current_node.nextNode
			
	def size1(self):
		return self.size
		
	def size2(self):
	
		actual_node = self.head
		size = 0
		
		while actual_node is not None:
			size+=1
			actual_node = actual_node.next_node
			
		return size
		
	def insert_end(self,data):
	
		self.size = self.size + 1
		new_node = Node(data)
		actual_node = self.head
		
		while actual_node.next_node is not None:
			actual_node = actual_node.next_node
			
		actual_node.next_node = new_node
		
	def traverse_list(self):
	
		actual_node = self.head
		
		while actual_node is not None:
			print("%d " % actual_node.data)
			actual_node = actual_node.next_node
			
if __name__ == "__main__":

	linked_list = LinkedList()
	
	linked_list.insert_start(12)
	linked_list.insert_start(122)
	linked_list.insert_start(3)
	linked_list.insert_start(31)
	linked_list.insert_start(10)
	linked_list.insert_start(11)
	linked_list.traverse_list()
	linked_list.reverse()
	print("Reversed List")
	linked_list.traverse_list()