from scraper import scrape_text
from extractor import create_csv

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    data = scrape_text()
    create_csv(data, "dm.csv")

if __name__ == "__main__":
    main()
