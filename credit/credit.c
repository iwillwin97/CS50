#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    int i = 0;
    int j;
    int k;
    int noi;
    long cc;
    long num;
    long cf1;
    int sum1=0;
    int sum2=0;
    long cf2;
    int sum;

    do
    {
      // getting the credit card number from the user.
        cc = get_long("Number: ");
        num = cc;
    }
    while(cc < 0);
    do
{
   cc=cc/10;
    i++;
    noi = 1/2;
}
while(cc > 1);


 // giving the result back of invalid if the number of digits does not match 13 or 15 or 16


 if (i != 13 && i != 15 && i != 16)
 {
printf("INVALID\n");
return 0;
 }

// applyig Lunhs algorithm

// for the even position of numbers

for(j=1; j <= i/2; j++)
{
  long ten1 = pow(10 , 2*j);
  long ten11 = pow(10,(2*j)-1);

  cf1 = num % ten1;


  if (cf1 < ten11)
{
  cf1 = 0;
}

else
{
  while(cf1>9)
  {
    cf1 = cf1/10;
  }
}

cf1 = 2*cf1;
if (cf1 > 9)
{
  cf1 = (cf1 % 10) + (cf1/10);
}
  sum1 += cf1;
}

// for the odd positon of digits.

  for (k = 0; k <= i/2 ; k++)
{
  long ten2 = pow(10, (2*k)+1);
  long ten22 = pow(10,(2*k));
  cf2 = num % ten2;

  if (cf2 < ten22)
{
  cf2 = 0;
}

else
{

  while (cf2 > 9)
  {
    cf2 = cf2/10;
  }
}
  sum2 += cf2;
}

sum = sum1 + sum2;


// figuring out the card type using all the parameter we have

do
{
  num = num/10;
}

while (num >100);

if (sum % 10 !=0)
{
  printf("INVALID\n");
}

else if ((i = 15) && (num / 10 == 3) && ((num % 10 == 4) || (num % 10 == 7)))
{
  printf("AMEX\n");

}
else if(((i=13) || (i=16)) && (num / 10 == 4) )
{
  printf("VISA\n");
}
else if((i=15) && (num / 10 == 5) && (0 < num % 10 && num % 10 < 6))
{
  printf("MASTERCARD\n");
}
else
{
  printf("INVALID\n");
}
}