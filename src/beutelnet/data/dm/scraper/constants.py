from pathlib import Path, PurePath

# Paths
URL = "https://www.dm.de/haushalt/haushaltsartikel/staubsaugerbeutel#finder"
DRIVER = "/home/furukawa/programming/chrome_for_testing/chromedriver-linux64/chromedriver"
BINARY = "/home/furukawa/programming/chrome_for_testing/chrome"

# Cookie Elements
SHADOW_HOST = '[id="usercentrics-root"]'
COOKIE = '[data-testid="uc-accept-all-button"]'

# HTML Elements
PRODUCT_BUTTON = 'button[data-dmid="fm-vcbf-product-footer-button"]'
FURTHER_PRODUCTS_BUTTON = '[data-dmid="fm-vcbf-vaccummodelslist-button"]'
PRODUCT_NAMES_BOX = '[data-dmid="layer-content"]'
BRAND_NAMES = '[data-dmid="fm-vcbf-logo"]'
SIZE = '[data-dmid="layer-header"]'
BRAND_IMAGE = 'edico_image-jQO_Q edico_imageOriginal-Mqa5A'
