# La Pesca en Cuba

aca puede verlo: <https://albert03.streamlit.app>

para abrirlo local:

git clone <https://github.com/ALbertE03/data_product.git>

## pip install -r requirements.txt

## pip install scikit-learn

en la carpeta .streamlit crear un archivo secrets.toml y para configurar las variables de entorno:

token = "..."

chat_id = "..."

token_scraping= "..."

pesca = "..."

-- token: se obtiene creando un bot en telegram (@BotFhater).

-- chat_id: se obtiene usado el bot '@userinfobot' en telegram y obtenga su chat_id

-- token_scraping: se obtiene creandose una cuenta en <https://api.scraperapi.com>

-- pesca: puede poner la que guste

### iniciarlo

#### streamlit run dataproduct.py

##### nota

es posible que tenga que configurar las rutas de los archivos que se abren en los diferentes archivos .py
