#include <iostream>
#include <string>

// Function to authenticate user
bool authenticate(const std::string& id, const std::string& password) {
    const std::string CORRECT_ID = "123";
    const std::string CORRECT_PASSWORD = "ABA";// pragma: allowlist secret

    return (id == CORRECT_ID && password == CORRECT_PASSWORD);
}

int main() {
    std::string id_input, password_input;
    int attempts = 0;
    const int MAX_ATTEMPTS = 3;

    std::cout << "\tWELCOME TO SMART ATTENDANCE SYSTEM\n";

    while (attempts < MAX_ATTEMPTS) {
        std::cout << "\tEnter ID       : ";
        std::cin >> id_input;

        std::cout << "\tEnter password : ";
        std::cin >> password_input;

        if (authenticate(id_input, password_input)) {
            std::cout << "\n\tLogin successful!\n";
            return 0;
        } else {
            attempts++;
            std::cout << "\n\tInvalid ID or Password!";
            std::cout << "\n\tAttempts remaining: "
                      << (MAX_ATTEMPTS - attempts) << "\n";

            if (attempts >= MAX_ATTEMPTS) {
                std::cout << "\n\tNo attempts left!\n";
                return 0;
            }

            std::cout << "\n\tPress Enter to continue...";
            std::cin.ignore(1000, '\n');
            std::cin.get();
        }
    }

    return 0;
}
