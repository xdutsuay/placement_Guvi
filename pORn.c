#include<stdio.h>
void main()
{
int x;
printf(" enter a number range +-100000");
scanf("%d",&x);
if(x>100000)
printf("enter again");
else if(x<0)
printf("Negative");
else if(x=0)
printf("Zero");
else
printf("positive");
}
