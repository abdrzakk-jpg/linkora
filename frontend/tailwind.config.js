export default {
  darkMode: 'class',
  content: ['./src/**/*.{svelte,html,js,ts}'],
  theme: {
    extend: {
      fontFamily: {
        display: ['"SF Pro Display"', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
        body:    ['"SF Pro Text"',    'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
      },
    },
  },
};