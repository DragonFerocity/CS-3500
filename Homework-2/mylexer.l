		               /* ---- PROLOGUE ---- */
%{
#include <iostream>
using namespace std;

int no_lines = 0;
int i = 0;
%}
		              /* ---- DEFINITIONS ---- */
%option noyywrap
DIGIT		[0-9]

%%  		              /* ---- REGULAR EXPRESSIONS ---- */

\n                                  { no_lines++; }
["#@\!\.\'\^]                       { cout << "#" << i << ": TOKEN: ?\t\tLEXEME: " << yytext << endl; i++; }
(if|else|func|let|print|while)      { cout << "#" << i << ": TOKEN: KEYWORD\tLEXEME: " << yytext << endl; i++; }
(\+|\-)?[0-9]+                      { cout << "#" << i << ": TOKEN: INTCONST\tLEXEME: " << yytext << endl; i++; }
(\+|\-)?[0-9]+\.[0-9]+              { cout << "#" << i << ": TOKEN: DECCONST\tLEXEME: " << yytext << endl; i++; }
(\+|\-)?[0-9]+\.[0-9]+*E\-?[0-9]+   { cout << "#" << i << ": TOKEN: SCICONST\tLEXEME: " << yytext << endl; i++; }
[ABCDEF0-9]+H                       { cout << "#" << i << ": TOKEN: HEXADECIMAL\tLEXEME: " << yytext << endl; i++; }
[A-Za-z][A-Za-z0-9]*                { cout << "#" << i << ": TOKEN: IDENT\tLEXEME: " << yytext << endl; i++; }
[01]+B                              { cout << "#" << i << ": TOKEN: BICONST\tLEXEME: " << yytext << endl; i++; }
\([0-9]{3}\)[0-9]{3}\-[0-9]{4}      { cout << "#" << i << ": TOKEN: PHCONST\tLEXEME: " << yytext << endl; i++; }
[0-9]{3}\-[0-9]{3}\-[0-9]{4}        { cout << "#" << i << ": TOKEN: PHCONST\tLEXEME: " << yytext << endl; i++; }
[0-9]{3}\.[0-9]{3}\.[0-9]{4}        { cout << "#" << i << ": TOKEN: PHCONST\tLEXEME: " << yytext << endl; i++; }
\"[a-zA-Z0-9 ]*\"                   { cout << "#" << i << ": TOKEN: STRCONST\tLEXEME: " << yytext << endl; i++; }
[\+\-\*/<>&]                        { cout << "#" << i << ": TOKEN: OPERATOR\tLEXEME: " << yytext << endl; i++; }
\%.*\n                              ;
[ \t]                               ;

%%  		              /* ---- EPILOGUE ---- */

int main()
{
    cout << "Hello FLEX" << endl;
    yylex();
    cout << no_lines << " lines processed." << endl;
    return 0;
}
