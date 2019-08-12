#include <string.h>
#include <stdlib.h>
#include <stdio.h>

char* reverse_string(char* s) {
    if (s == NULL) return NULL;
    int N = strlen(s);
    char* rev = (char*)malloc(N);
    for (int i = N-1; i >= 0; i--) rev[N-i-1] = s[i];
    rev[N] = '\0';
    return rev;
}

int main() {
    char* s = reverse_string("123456789");
    printf("%s\n", s);
    return 0;
}

