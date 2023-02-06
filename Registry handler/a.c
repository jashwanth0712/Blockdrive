#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    int i;
    if (argc < 2)
    {
        printf("Error: Missing arguments\n");
        return 1;
    }
   
    printf("\n");
    
    int j;
    for (j = 1; j < argc; j++)
    {
        printf("Argument %d: %s\n", j, argv[j]);
    }
    for (i = 0; i <= 30; i++)
    {
        printf("\rLoading... %3d%%", i);
        fflush(stdout);
        sleep(1);
    }
    return 0;
}
