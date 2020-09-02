# Singly Linked List written in Python (TDD)

Quick implementation of a **singly linked list** written in python using test-driven development (pytest).

## What are Linked Lists

Similar to array, but element position is stored along-side the value. You append to the start (called HEAD) rather than end.

### Advantages

- Appending to the start of the list is much faster
- Changing the position of an element is much faster with large data sets. In a normal array, all elements after the position change would also need to change.

### Disadvantages

Retrieving a position from a linked list is much slower, as the chain has to be followed from the start to find the nth element.

### Types

- Singly Linked List: Linear, relationships in one-direction
- Doubly Linked List: Relationships in two directions
- Circular Linked List: Like singly but last+1 is first element

[How To Implement Linked Lists With Test Driven Development In JavaScript](https://youtu.be/gJjPWA8wpQg)
