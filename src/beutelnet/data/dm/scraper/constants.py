from pathlib import Path, PurePath

# Paths
URL = "https://www.dm.de/haushalt/haushaltsartikel/staubsaugerbeutel#finder"
DRIVER = "/home/furukawa/programming/chrome_for_testing/chromedriver-linux64/chromedriver"
BINARY = "/home/furukawa/programming/chrome_for_testing/chrome"

# Cookie Elements
SHADOW_HOST = '[id="usercentrics-root"]'
COOKIE = '[data-testid="uc-accept-all-button"]'

# HTML Elements

## Specify product module to scrape
PRODUCT_MODULE = "/html/body/div[1]/div/main/div[2]/div/div/div[6]"
PRODUCT_GRID = '[data-dmid="fm-vcbf-productgrid"]'
PRODUCT_TILES = '[data-dmid="product-tile"]'

## Click buttons
PRODUCT_BUTTON = 'button[data-dmid="fm-vcbf-product-footer-button"]'
FURTHER_PRODUCTS_BUTTON = '[data-dmid="fm-vcbf-vaccummodelslist-button"]'

## Extract text
PRODUCT_NAMES_BOX = '[data-dmid="layer-content"]'
BRAND_NAMES = '[data-dmid="fm-vcbf-logo"]'
SIZE = '[data-dmid="layer-header"]'
BRAND_IMAGE = 'edico_image-jQO_Q edico_imageOriginal-Mqa5A'
CLOSE_BUTTON = '[data-dmid="layer-header-close-button"]'
