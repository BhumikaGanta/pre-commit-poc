#include <cctype>
#include <conio.h>
#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int a = 0;

struct Register {
  string id;
  string name;
  string email;
  string password;
} R[25];

void registerAccount() {
  cout << "Register Account" << endl;
  cin >> R[a].id;
  cin >> R[a].name;
  cin >> R[a].email;
  cin >> R[a].password;
  a++;
  cout << "Account Registered Successfully" << endl;
}

void loginAccount() {
  string t_email, t_password;
  int found = 0;

  cout << "Enter Email: ";
  cin >> t_email;
  cout << "Enter Password: ";
  cin >> t_password;

  for (int k = 0; k < a; k++) {
    if (t_email == R[k].email && t_password == R[k].password) {
      cout << "Login Successful" << endl;
      found = 1;
      break;
    }
  }

  if (found == 0) {
    cout << "Invalid User Data" << endl;
  }
}

int main() {
  int choice;

  while (true) {
    cout << "\n1. Register Account";
    cout << "\n2. Login Account";
    cout << "\n3. Exit";
    cout << "\nEnter Choice: ";
    cin >> choice;

    switch (choice) {
    case 1:
      registerAccount();
      break;
    case 2:
      loginAccount();
      break;
    case 3:
      exit(0);
    default:
      cout << "Invalid Choice" << endl;
    }
  }

  return 0;
}
