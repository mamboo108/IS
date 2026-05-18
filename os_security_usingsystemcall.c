#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <dirent.h>
#include <stdlib.h>

int main() {

    pid_t pid = fork();

    if(pid == 0) {

        printf("Child PID: %d\n", getpid());

        // stat()
        struct stat s;
        stat("test.txt", &s);
        printf("File size: %ld bytes\n", s.st_size);

        // opendir() and readdir()
        DIR *d = opendir(".");
        struct dirent *dir;

        printf("Files:\n");

        while((dir = readdir(d)) != NULL) {
            printf("%s\n", dir->d_name);
        }

        closedir(d);

        // exec()
        execlp("ls", "ls", NULL);

        // exit()
        exit(0);
    }

    else {

        // wait()
        wait(NULL);

        printf("Parent PID: %d\n", getpid());
    }

    return 0;
}
