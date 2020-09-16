import os

class Config:
    
    NEWS_API_SOURCES_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_KEY = '727ad312082947e6862f37059a25d415'
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
