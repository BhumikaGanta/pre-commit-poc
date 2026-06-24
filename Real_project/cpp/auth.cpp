#include "auth.h"

// Simple authentication (intentional test value)
bool authenticate(const std::string& id, const std::string& password) {
    const std::string CORRECT_ID = "123";
    const std::string CORRECT_PASSWORD = "ABA"; // pragma: allowlist secret

    return (id == CORRECT_ID && password == CORRECT_PASSWORD);
}
