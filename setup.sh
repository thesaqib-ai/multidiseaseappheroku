mkdir -p ~/.streamlit/

scho '\
[general]\n\
email = \"md.saqib370@gmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS  false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml