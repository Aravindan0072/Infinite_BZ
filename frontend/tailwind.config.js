/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            colors: {
                // Mapping 'sky' to 'Royal Purple' (#551A8B) for accents/text
                sky: {
                    50: '#f5f3ff',
                    100: '#ede9fe',
                    200: '#ddd6fe',
                    300: '#c4b5fd',
                    400: '#a78bfa',
                    500: '#551A8B', // Royal Purple (Primary Brand)
                    600: '#4c1d95',
                    700: '#301934', // Dark Purple
                    800: '#2e1065',
                    900: '#1e1b4b',
                },
                // Adding 'Gold' for CTAs
                gold: {
                    400: '#ffe066',
                    500: '#FFD700', // Royal Gold
                    600: '#e6c200', // Darker Gold for hover
                },
                // Mapping 'slate' text to Dark Charcoal
                slate: {
                    800: '#212529', // Headlines/Text
                    900: '#1a1d20',
                }
            }
        },
    },
    plugins: [],
}
