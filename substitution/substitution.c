#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>


int N = 26;
string base_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
string base_l = "abcdefghijklmnopqrstuvwxyz";
string letters;
int k = 0;



int main(int argc, string argv[])
{

    if (argc != 2)
    {
      printf("Usage: ./substitution key\n");
      return 1;
    }

//checking for if there are 26 letters in the given argument or not

   if (strlen(argv[1]) < 26)

   {
      printf("Key must contain 26 charecters.\n");
      return 1;
   }

//checking if entered arguments are letters

for (int i = 0; i < N; i++)
{
   if (argv[1][i] < 65 || argv[1][i] > 122)
   {
      printf("The key must only be a combination of letters.\n");
      return 1;
   }
//checking if there are any repeated letters

   for (int j = 0; j < N; j++)
   {
      if (argv[1][i] == argv[1][j])
      {
         k++;
      }

   }

   if (islower(argv[1][i]) != 0)
   {
      argv[1][i] = (argv[1][i]) - 32;
   }
}
if (k != 26)
{
   printf("Key has repeated letters.\n");
   return 1;
}

{
   string plain_text = get_string("plain text: ");
   int l = strlen(plain_text);


//Converting plain to ciphered text
printf("ciphertext: ");

   for (int i = 0; i < strlen(plain_text); i++)
   {
      for(int j = 0; j < 26; j++)
      {
         if (isupper(plain_text[i]))
         {
            if (plain_text[i] == base_u[j])
         {
            printf("%c",argv[1][j]);
         }
         }

         else if (plain_text[i] == base_l[j])
         {
            printf("%c",(argv[1][j] + 32));
         }
      }
          if (!isalpha(plain_text[i]))
         {
            printf("%c", plain_text[i]);
         }



   }
}
printf("\n");



}