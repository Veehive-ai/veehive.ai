/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./public/**/*.html"],
    theme: {
        extend: {
            fontFamily: {
                sans: ['Inter', 'system-ui', 'sans-serif'],
                display: ['Satoshi', 'Inter', 'sans-serif'],
            },
            colors: {
                brand: {
                    DEFAULT: '#3B5BFF',
                    light: '#6B82FF',
                    dark: '#2A45CC',
                },
                accent: '#8B5CFF',
                surface: {
                    DEFAULT: '#0F1A20',
                    raised: 'rgba(255,255,255,0.03)',
                    overlay: 'rgba(255,255,255,0.06)',
                },
                planner: '#3B5BFF',
                orchestrator: '#8B5CFF',
                creator: '#3B5BFF',
                distributor: '#3B5BFF',
                labs: '#8B5CFF',
                mustard: {
                    DEFAULT: '#3B5BFF',
                    light: '#6B82FF',
                    dark: '#2A45CC',
                },
            }
        }
    },
    plugins: [],
}
