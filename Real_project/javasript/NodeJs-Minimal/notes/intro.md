## Intro

### What is Node.js?

Node.js is a powerful runtime environment that allows you to execute JavaScript code outside of a web browser. This capability is significant because it expands the potential uses of JavaScript, making it a versatile language for server-side development.

### Why is Node.js Important?

Node.js has revolutionized web development for two major reasons:

1. **Package Management**: Node.js comes with npm (Node Package Manager), which allows developers to download and manage a wide range of libraries and frameworks. For instance, before starting a project with React, you typically install Node.js to easily manage dependencies and tools needed for development.

   - **Example**: By using npm, you can quickly set up a React project with `npx create-react-app my-app`.

2. **Server-Side Scripting**: Node.js enables the execution of JavaScript on the server side, allowing developers to handle server-side logic, interact with databases, and manage backend operations using JavaScript.

   - **Example**: You can create a simple web server using Node.js with just a few lines of code:

     ```javascript
     const http = require("http");

     const server = http.createServer((req, res) => {
       res.statusCode = 200;
       res.setHeader("Content-Type", "text/plain");
       res.end("Hello, World!\n");
     });

     server.listen(3000, "127.0.0.1", () => {
       console.log("Server running at http://127.0.0.1:3000/");
     });
     ```

The takeaway here is that Node.js is a fundamental tool for modern web development. Understanding how it works and how it integrates with other tools like React is crucial for any web developer.

## Installation

### Under Linux

To install Node.js on a Linux system, follow these steps:

1. **Update your package index**:

   ```sh
   sudo apt update
   ```

2. **Install Node.js**:

   ```sh
   sudo apt install nodejs
   ```

3. **Verify the installation**:

   ```sh
   node -v
   ```

4. **Install npm (if not included)**:
   ```sh
   sudo apt install npm
   ```

### Under Windows (using VS Code)

To install Node.js on a Windows system, follow these steps:

1. **Download the Node.js installer** from the [official Node.js website](https://nodejs.org/).

2. **Run the installer**:

   - Double-click the downloaded installer.
   - Follow the setup instructions. During the installation, you may be prompted to install additional tools for native module support. It's recommended to check this option to ensure you have all the necessary components like Python and Visual Studio Build Tools.

3. **Verify the installation**:

   - Open Command Prompt or PowerShell and type the following command to check the installed Node.js version:
     ```sh
     node -v
     ```
   - To check the npm version, use:
     ```sh
     npm -v
     ```

4. **Set up Visual Studio Code**:
   - If you haven't installed Visual Studio Code yet, download and install it from the [Visual Studio Code website](https://code.visualstudio.com/).
   - Open Visual Studio Code.
   - Open the terminal within VS Code by navigating to `View > Terminal` or using the shortcut `` Ctrl+` ``.
   - In the terminal, verify that Node.js and npm are recognized by typing:
     ```sh
     node -v
     npm -v
     ```
