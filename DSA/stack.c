// Dynamic implementation of the stack data structure in C
#include <stdio.h>
#include <stdlib.h> 
#include <stdbool.h> 

typedef struct 
{
	int *collection; // dynamically allocated array
	int capacity; // size of *collection
	int size; // number of elements stored in *collection
} Stack;

// declare functions for working with Stack data structure
Stack *create_stack(int capacity);
void destroy_stack(Stack *stack);
bool is_full(Stack *stack);
bool is_empty(Stack *stack);
bool pop(Stack *stack, int *item);
bool push(Stack *stack, int item);
bool peek(Stack *stack, int *item);

int main (void) 
{ 

	Stack *stack = create_stack(3);

	// if failed to create stack then exit program
	if (stack == NULL) return 1;

  // stack should be empty initially
	if (is_empty(stack)) printf("Stack is empty\n");

	push(stack, 1);
  push(stack, 7);

	printf("Stack size: %d\n", stack->size);
	
	push(stack, 5);
  
  // stack should be full
	if (is_full(stack)) printf("Stack is full.\n");
  printf("Stack size: %d\n", stack->size);

  // if we try to push another item onto the stack, it should fail
  bool try_push = push(stack, 9);
  if (try_push == false) printf("Push failed.\n");
  
  // if we peek at the top item in the stack, the value should be 5
  int peek_val = 0;
  peek(stack, &peek_val);
  printf("Peek Val: %d\n", peek_val);

	// pop off the 3 items on the stack, notice the "last in, first out" order
  int pop_val = 0;
  for (int i = 0; i < 3; i++)
  {
    // pop each item and print it
    pop(stack, &pop_val);
    printf("Popped Value: %d\n", pop_val);
  }

	// if we try to pop an item off an empty stack, it will fail
  bool try_pop = pop(stack, &pop_val);
  if (try_pop == false) printf("Pop Failed.\n");
  
  // if we try to peek at an item on an empty stack, it will fail
  bool try_peek = peek(stack, &peek_val);
  if (try_peek == false) printf("Peek Failed.\n");
  
  // destroy the stack since we are done working with it
  destroy_stack(stack);

	return 0 ;
}

Stack *create_stack(int capacity) 
{
	if (capacity <= 0) return NULL;

	Stack *stack = malloc(sizeof(Stack));

	// check if malloc worked, if it failed it will rerturn null
	if (stack == NULL) return NULL; 

	// allocate space to store a collection with the specified capacity
	stack -> collection = malloc(sizeof(int) * capacity);

	if (stack -> collection == NULL) 
	{
		free(stack); // if malloc failed, free the memory
		return NULL;
	}

	stack -> capacity = capacity;
	stack -> size = 0; // initially there are 0 elements
	
	return stack;
}

void destroy_stack(Stack *stack) 
{
  // free the dynamically allocated memory for collection array 
	// and then the stack itself
	free(stack -> collection);
	free(stack);
}

bool is_full(Stack *stack) 
{
	return stack -> capacity == stack -> size;
}

bool is_empty(Stack *stack) 
{
	return stack -> size == 0;
}

bool push(Stack *stack, int item)
{
	if (is_full(stack)) return false;

	// set the element of collection array at index of size to item
	stack -> collection[stack -> size] = item;
	stack -> size ++;

	return true;
}

bool peek(Stack *stack, int *item) 
{
	if (is_empty(stack)) return false;

	// store the value using pass by pointer (deferencing item)
	*item = stack -> collection[stack -> size - 1];

	return true;
}

bool pop(Stack *stack, int *item)
{
	if (is_empty(stack)) return false;

	// decrease stack size and dereference item
	stack -> size --;
	*item = stack -> collection[stack -> size];

	return true;
}
