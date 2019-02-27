#include<stdio.h>
#include<stdlib.h>

struct Node 
{
	int data;
	struct node *next;
};

void INSERTEND(struct Node **head,struct Node **end,int a);
void PRINT(struct Node *head);
void PRINTNEW(struct Node **head,int n);
void DELETE(struct Node **head,int a);

int main()
{
    int t;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        struct Node *head=NULL;
        struct Node *end=NULL;
        for(int i=0;i<n;i++)
        {
            int a;
            scanf("%d",&a);
            INSERTEND(&head,&end,a);
        }
        // PRINT(head);
        PRINTNEW(&head,n);
  
    }
    return 0;
}




void PRINTNEW(struct Node **head,int n)
{
    struct Node *large=(*head);
    struct Node *small=(*head);
    struct Node *temp=(*head);
    while(temp!=NULL)
    {
        if((temp->data)>(large->data))
        {
            large=temp;
        }
        if((temp->data)<(small->data))
        {
            small=temp;
        }
        temp=temp->next;
    }
    // printf("%d %d \n",large->data,small->data);
    if (n==1)
    {
        DELETE(&(*head),large->data);
    }
    else
    {
        DELETE(&(*head),large->data);
        DELETE(&(*head),small->data);
    }
    
    PRINT(*head);
}


void DELETE(struct Node **head,int data)
{
    struct Node *temp=*head;
    struct Node *prev=NULL;

    if (temp != NULL && temp->data == data) 
    { 
        *head=temp->next;    
        free(temp);  
        // PRINT(*head) ; 
        return;           
    } 

    while(temp!=NULL && (temp->data)!=data)
    {
        prev=temp;
        temp=temp->next;
    }
    prev->next=temp->next;

    free(temp);
     // PRINT(*head);
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

void PRINT(struct Node *head)
{
	struct Node *temp=head;
	while(temp!=NULL)
	{
		printf("%d ",temp->data);
		temp=temp->next;
	}
    printf("\n");
}