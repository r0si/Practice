#include <stdio.h>
#include<unistd.h>/*#包含<unistd.h>*/
#include<sys/types.h>/*#包含<sys/types.h>*/
int main(int argc, char const* argv[])
{
  int i;
  for (int i = 0; i < 3; i++) {
    fork();
    printf("*\n");
  }
  return 0;
}
