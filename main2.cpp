#include<stdio.h>

//-------NODE_STRUCTURE-------//
struct Node {
    int data;
    Node *pNext;
}; //----------------------------//


//-------CREATE_A_EMPTY_LIST-------//
struct List {
    Node *pHead;
    Node *pTail;
};

void init(List &l) {
    l.pHead = l.pTail = NULL;
}; //----------------------------//


//-------CHECK_IF_THE_LIST_IS_EMPTY-------//
void checkEmptyList(List &l, Node *p) {
    if (l.pHead == NULL && l.pTail == NULL)
        l.pHead = l.pTail = p;
}; //----------------------------//


//-------CREATE_A_NEW_NODE-------//
Node * createNode() {
    printf("Nhap gia tri: ");
	int data;
	scanf("%d", &data);

	Node *p = new Node;
	p->data = data;
	p->pNext = NULL;
	return p;
};

void toTail(List &l, Node *p) {
    l.pTail->pNext = p;
    l.pTail = p;
}; //----------------------------//


//-------INSERT_A_NODE_TO_AN_INPUTTED_INDEX-------//
void insertNode(List &l, int n) {
    printf("Nhap vi tri can chen: ");
    int index;
    scanf("%d", &index);

    Node *p = createNode();
    Node *t = l.pHead;

    if (index == 1) {
        p->pNext = l.pHead;
        l.pHead = p;
        return;
    }

    if (index > n) {
        l.pTail->pNext = p;
        l.pTail = p;
        return;
    }

    int i = 2;
    for (Node *q=l.pHead->pNext; q!=NULL; q=q->pNext) {
        if (index == i) {
            t->pNext = p;
            p->pNext = q;
        }
        t = q;
        i++;
    }
}; //----------------------------//


//-------DELETE_A_TAIL_NODE-------//
void deleteTail(List &l) {
    for (Node *q=l.pHead; q!=NULL; q=q->pNext) {
        if (q->pNext == l.pTail) {
            l.pTail = q;
            l.pTail->pNext = NULL;
        }
    }
}; //----------------------------//


//-------MAIN_PROGRAM-------//
int main()
{
    List l;
    init(l);

    printf("Nhap so lan can nhap: ");
    int n;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        Node *p = createNode();
        checkEmptyList(l, p);
        toTail(l, p);
    }

    //deleteTail(l);

    insertNode(l, n);

    for (Node *q=l.pHead; q!=NULL; q=q->pNext)
        if (q->pNext != NULL)
            printf("%d, ", q->data);
        else printf("%d", q->data);

    return 0;
}
