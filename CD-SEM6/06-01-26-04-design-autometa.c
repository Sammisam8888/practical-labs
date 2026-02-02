// wap to design autometa for the following language :
// L(m) = { a^n b^n | n>=1 }
#include <stdio.h>
#include <string.h>

#define MAX 100

int main() {
    char s[MAX];
    char stack[MAX];
    int top = -1;
    int i = 0;

    printf("Enter the input string for Language L: ");
    scanf("%s", s);

    int len = strlen(s);

    if (len == 0)
    {
        printf("Rejected\n");
        return 0;
    }

    while (s[i] == 'a') {
        stack[++top] = 'A';
        i++;
    }

    if (top == -1)
    {
        printf("Rejected\n");
        return 0;
    }

    while (s[i] == 'b') {
        if (top == -1) {
            printf("Rejected\n");
            return 0;
        }
        top--;
        i++;
    }

    if (i == len && top == -1)
        printf("Accepted\n");
    else
        printf("Rejected\n");

    return 0;
}
