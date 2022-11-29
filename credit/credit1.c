// checking for the type of card using the total numbner of digits and also the starting number patterns.

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







