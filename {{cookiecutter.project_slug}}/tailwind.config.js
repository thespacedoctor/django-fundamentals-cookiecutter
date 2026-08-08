/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./apps/**/templates/**/*.html",
    "./.venv/lib/**/django_fundamentals/templates/**/*.html",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
