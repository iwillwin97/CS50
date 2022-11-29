#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
int main(void)
{
    string s = get_string("Text: ");

  //function for average number of letters in the given text
    int index;
    float x;
    float number_of_words = 0;
    float number_of_sentences = 0;
    float number_of_letters = 0;
    int n = strlen(s);
    string s1;
    for (int i = 0; i < n; i++)
    {

        if (s[i] == ' ' || s[i] == '\0')
        {
            number_of_words++;
        }

        if (s[i] == '.' || s[i] == '?' || s[i] == '!')
        {
            number_of_sentences++;
        }
        if((s[i] > 64 && s[i] <91) || (s[i] > 96 && s[i] < 123))
        {
            number_of_letters++;
        }
    }

//converting the numbers we got to 100 avg words to fit into the expression
float L = (number_of_letters * 100)/(number_of_words + 1);
float S = (number_of_sentences * 100)/(number_of_words + 1);

// using the formula to get the grade

x = (0.0588 * L) - (0.296 * S) - 15.8;
index = round(x);

if (index < 0)
{
   printf("Before Grade 1\n");

   return 0;
}
if (index > 16)
{
    printf("Grade 16+\n");
}
else
{
    printf("Grade %d\n",index);
}


}