mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
\n\
[theme]\n\
primaryColor = '#E694FF'\n\
backgroundColor = '#00172B'\n\
secondaryBackgroundColor = '#0083B8'\n\
textColor = '#FFF'\n\
font = 'sans serif'\n\
\n\
" > ~/.streamlit/config.toml