#include<stdio.h>
#include<stdlib.h>

struct Node 
{
	int data;
	struct node *next;
};

void INSERTEND(struct Node **head,struct Node **end);
void PRINT(struct Node *head);
void PRINTSUM(struct Node *head);


int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        struct Node *head=NULL;
        struct Node *end=NULL;
        int n;
        scanf("%d",&n);
        while(n--)
        {
        	INSERTEND(&head,&end);
        }
   		PRINT(head);
   		PRINTSUM(head);
    }
    return 0;
}

void INSERTEND(struct Node **head,struct Node **end)
{
	if (*head==NULL)
	{
		int a;
        scanf("%d",&a);
        *head=(struct Node *)malloc(sizeof(struct Node));
		(*head)->data=a;
		(*head)->next=NULL;
		(*end)=(*head);
	}
	else 
	{
		struct Node *temp=(struct Node *)malloc(sizeof(struct Node));
		int b;
		scanf("%d",&b);
		temp->data=b;
		temp->next=NULL;
		(*end)->next=temp;
		(*end)=temp;
	}

}



		/*while(temp->next!=NULL)
		{
			temp=temp->next;
		}
		int b;
		scanf("%d",&b);
		struct Node *new=(struct Node *)malloc(sizeof(struct Node));
		new->data=b;
		new->next=NULL;
		temp->next=new;*/

void PRINT(struct Node *head)
{
	struct Node *temp=head;
	while(temp!=NULL)
	{
		printf("%d",temp->data);
		temp=temp->next;
	}
}

void PRINTSUM(struct Node *head)
{
	struct Node *temp=head;
	int sum=0;
	while(temp!=NULL)
	{
		sum=sum+(temp->data);
		temp=(temp->next);
	}
	printf("%d\n",sum);
}