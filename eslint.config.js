export default [
  {
    files: ["**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      globals: {
        console: "readonly",
      },
    },
    rules: {
      "no-undef": "error",
    },
  },
];
