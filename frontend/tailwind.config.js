/** @type {import('tailwindcss').Config} */
export default {
  darkMode: ["class"],
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: '#2563EB',
          foreground: '#ffffff',
        },
        secondary: {
          DEFAULT: '#10B981',
          foreground: '#ffffff',
        },
        destructive: {
          DEFAULT: '#EF4444',
          foreground: '#ffffff',
        },
        muted: {
          DEFAULT: '#F9FAFB',
          foreground: '#6B7280',
        },
        background: '#F9FAFB',
        foreground: '#111827',
        border: '#E5E7EB',
      },
      fontFamily: {
        sans: ['Pretendard', '-apple-system', 'BlinkMacSystemFont', 'sans-serif'],
      },
      borderRadius: {
        lg: '12px',
        md: '8px',
        sm: '4px',
      },
    },
  },
  plugins: [],
}
