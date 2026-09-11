/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        display: ['"SF Pro Display"', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
        body:    ['"SF Pro Text"',    'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
      },
      borderRadius: { DEFAULT: '0px' },   /* sharp corners */
      colors: {
        accent: { DEFAULT: '#5856d6', dark: '#7d7aff', hover: '#3634c7' },
        ink:    { DEFAULT: '#1d1d1f', muted: '#6e6e73', faint: '#aeaeb2' },
      }
    }
  },
  plugins: []
};
