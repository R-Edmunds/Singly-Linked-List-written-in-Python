import random
from string import ascii_lowercase, ascii_letters, digits
from linkedlist import LinkedList


ll = LinkedList()
ll.insertMultipleValues(*[ascii_lowercase[i] for i in range(9)])
ll.print()
