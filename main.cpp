#include <stdio.h>
#include <iostream>

using namespace std;

//------------DEFINE_A_NODE-------------//
struct Node {
	int data;
	struct Node *pNext;
};

//------------DEFINE_A_EMPTY_LIST-------------//
struct List {
	Node *pHead;
	Node *pTail;
};

void init(List &l) {
	l.pHead = l.pTail = NULL;
};

//------------CREATE_A_NEW_NODE-------------//
Node* createNode() {
	printf("Nhap gia tri: ");
	int data;
	scanf("%d", &data);

	// Append data to new node
	Node *p = new Node;
	p->data = data;
	p->pNext = NULL;
	return p;
}

//------------CHECK_THE_LIST_IS_EMPTY-------------//
void checkListIsEmpty(List &l, Node *p) {
	if (l.pHead == NULL && l.pTail == NULL) {
		l.pHead = l.pTail = p;
	}
}

//------------APPEND_TO_THE_HEAD_OR_TAIL-------------//
void toHead(List &l, Node *p) {
	p->pNext = l.pHead;
	l.pHead = p;
}

void toTail(List &l, Node *p) {
	l.pTail->pNext = p;
	l.pTail = p;
}

//------------DELETE_HEAD_OR_TAIL-------------//
void deleteHead(List &l) {
	Node *t = l.pHead;
	l.pHead = t->pNext;
	t->pNext = NULL;
	delete t;
}

void deleteTail(List &l) {
	for (Node *q=l.pHead; q!=NULL; q=q->pNext) {
		if (q->pNext == l.pTail) {
			l.pTail = q;
			q->pNext = NULL;
		}
	}
}

//------------FIND_A_NODE'S_VALUE-------------//
void findNode(List &l) {
	printf("Nhap gia tri can tim: ");
	int find;
	scanf("%d", &find);

	for (Node *q=l.pHead; q!=NULL; q=q->pNext)
		if (q->data == find){
			printf("Gia tri %d co trong List", find);
			return;
		}
	printf("Gia tri %d khong co trong List", find);
}

//------------DELETE_A_NODE-------------//
void deleteNode(List &l) {
	printf("Nhap gia tri can xoa: ");
	int value;
	scanf("%d", &value);

	Node *t;
	int count = 0;
	for (Node *q=l.pHead; q!=NULL; q=q->pNext) {
		printf("%d__", q->data);
		if (count == 1) {
			t->pNext = NULL;
			count = 0;
		}
		if (q->pNext->data == value) {
			t = q->pNext;
			q->pNext = t->pNext;
			q = t;
			count = 1;
		}
	}
	delete t;
}

//------------MAIN-------------//
int main() {
	// Make a List
	List l;
	init(l);

	// Get 'num' for loop
	printf("Nhap so lan can nhap: ");
	int num;
	scanf("%d", &num);

	// Create and append new Node for 'num' times
	for (int i=1; i<=num; i++) {
		Node *p = createNode();
		checkListIsEmpty(l, p);
		toTail(l, p);
	}

	deleteTail(l);

	// Print data in each Node of the List
	for (Node *q=l.pHead; q!=NULL; q=q->pNext)
		printf("%d ", q->data);


	return 0;
}
