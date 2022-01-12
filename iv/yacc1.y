%{
#include<stdio.h>
#include<stdlib.h>
int yylex();
%}

%token digit letter NL;

%%
start: s NL  {printf("Valid Identifier \n"); exit(0);};
s: letter c| letter;
c: letter c| letter| digit| digit c;
%%

int yyerror()
{
printf("Invalid Identifier \n");
exit(0);
}

int main()
{
printf("Enter the string: \t");
yyparse();
return 1;
}

int yywrap() 
 {
 return(1);
 }
