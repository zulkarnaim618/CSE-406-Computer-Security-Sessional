#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


#define PARAM_1 30
#define PARAM_2 50
#define PARAM_3 400

// cannot use this in payload
#define PASS 5004

void get_service(char *user, char *pass) {
	printf("Service running on!\n");
	char buffer[PARAM_1];
	strcpy(buffer, pass);
	execve("/bin/sh", NULL, 0);
}

void check_password(char *user, char *pass) {
	int pass_int = atoi(pass);
	if (pass_int == PASS) {
		get_service(user, pass);
	}
	else {
		printf("Wrong password!\n");
	}
}

void execute(char *name, char *password) {
	char username[PARAM_2];
	char pass[PARAM_3];
	strcpy(pass, password);
	strcpy(username, name);
	check_password(username, pass);
}

int main() {
	printf("In main function\n");
	char username[PARAM_3];
	char password[PARAM_3];
	FILE *username_file, *password_file;
	username_file = fopen("username", "r");
	password_file = fopen("password", "r");
	fread(username, sizeof(char), PARAM_3, username_file);
	fread(password, sizeof(char), PARAM_3, password_file);
	char dummy[PARAM_3*4];
	execute(username, password);
	return 0;
}
