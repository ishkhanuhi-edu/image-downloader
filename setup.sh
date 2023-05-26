mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"ishkhanuhi.hakobyan@edu.ysu.am\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=true\n\
port = 8501\n\
" > ~/.streamlit/config.toml