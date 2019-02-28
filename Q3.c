#include<stdio.h>
#include<stdlib.h>

struct Node 
{
	int data;
	struct node *next;
};

void INSERTEND(struct Node **head,struct Node **end,int a);
void SPLITandJOIN(struct Node *head,struct Node **evenhead,struct Node **oddhead,struct Node **evenend,struct Node **oddend);
void PRINT(struct Node *oddhead);

int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        struct Node *head=NULL;
        struct Node *end=NULL;
        struct Node *evenhead=NULL;
		struct Node *oddhead=NULL;
		struct Node *oddend=NULL;
		struct Node *evenend=NULL;
        int n;
        scanf("%d",&n);
        while(n--)
        {
        	int a;
        	scanf("%d",&a);
        	INSERTEND(&head,&end,a);
        }
   		SPLITandJOIN(head,&evenhead,&oddhead,&evenend,&oddend);
   		PRINT(oddhead);
   		printf("\n");
    }
    
    return 0;
}

void INSERTEND(struct Node **head,struct Node **end,int a)
{
	if (*head==NULL)
	{
	
        *head=(struct Node *)malloc(sizeof(struct Node));
		(*head)->data=a;
		(*head)->next=NULL;
		(*end)=(*head);
	}
	else 
	{
		struct Node *temp=(struct Node *)malloc(sizeof(struct Node));
		temp->data=a;
		temp->next=NULL;
		(*end)->next=temp;
		(*end)=temp;
	}
}

void SPLITandJOIN(struct Node *head,struct Node **evenhead,struct Node **oddhead,struct Node **evenend,struct Node **oddend)
{
	struct Node *temp=head;
	
	while(temp!=NULL)
	{
		if((temp->data)%2==0)
		{			
			INSERTEND(&(*evenhead),&(*evenend),temp->data);
		}
		else
		{
			INSERTEND(&(*oddhead),&(*oddend),temp->data);
		}
		temp=temp->next;
	}
	(*oddend)->next=(*evenhead);
}

void PRINT(struct Node *oddhead)
{
	struct Node *temp=oddhead;
	while(temp!=NULL)
	{
		printf("%d ",temp->data);
		temp=temp->next;
	}
}
