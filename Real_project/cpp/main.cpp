#include <iostream>
#include "auth.h"
#include "utils.h"

int main() {
    std::string id, password;

    print_welcome();

    std::cout << "Enter ID       : ";
    std::cin >> id;

    std::cout << "Enter password : ";
    std::cin >> password;

    if (authenticate(id, password)) {
        std::cout << "Login successful!\n";
    } else {
        std::cout << "Login failed!\n";
    }

    return 0;
}
