const colors = require('tailwindcss/colors')

module.exports = {
  purge: [
    './nnamm.work/templates/*.html',
    './nnamm.work/templates/**/*.html'
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
  corePlugins: {
    fontFamily: false,
  }
}
