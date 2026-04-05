/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        serif: ['Newsreader', 'serif'],
        body: ['Manrope', 'sans-serif'],
        label: ['Manrope', 'sans-serif'],
      },
      colors: {
        primary: '#012d1d',
        'primary-container': '#1b4332',
        secondary: '#4c616c',
        'secondary-container': '#cfe6f2',
        background: '#f8f9fa',
        'on-surface': '#191c1d',
        'surface-container-low': '#f3f4f5',
      },
    },
  },
  plugins: [],
}
