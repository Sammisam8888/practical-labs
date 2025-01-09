//insertion into linked list : i-at the beginning, ii-at end, iii-at a given position

#include <stdio.h>
#include <stdlib.h>
struct node{
	int info;
	struct node *next;
};
void insert(struct node *p){
	int n,i=1;
	printf("Enter the index at which you want to insert the element :");
	scanf("%d",&n);
	while (i<=n){
		p=p->next;
		i++;
	}
	struct node* newnode=(struct node*)malloc(sizeof(struct node));
	printf("Enter the element that you want to insert :");
	scanf("%d",&newnode->info);
	if (p->next == NULL)
		newnode->next=NULL;
	else
		newnode->next=p->next;
	p->next=newnode;
}
void main(){
	struct node *head,*temp,*newnode; //temp is the iterating reference node 
	int ch=1,i=1; 
	head=(struct node*)malloc(sizeof(struct node)); //declaration of head to point the adress of 1st element
	while(ch!=0){
		newnode=(struct node*)malloc(sizeof(struct node)); //declaration of new node for inserting new element
		printf("Enter the data of linked list elements :");
		scanf("%d",&newnode->info);
		newnode->next=NULL;
		if (i==1){
			head->next=temp=newnode; //insertion of first element
		}
		else{
			temp->next=newnode; //insertion of further elements
			temp=temp->next;
		}
	printf("Do you want to continue? (1-yes,0-no) :");
	scanf("%d",&ch);
	} free (newnode);
	insert(head);
	printf("The elements of the linked list are :");
	temp=head->next;
	while(temp->next!=NULL){
		printf("%d",temp->info);
		temp=temp->next;
	}
	free(temp);
	
}
