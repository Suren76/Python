from selenium import webdriver
from time import sleep

def test_w_d():
    chrom_dr = webdriver.Chrome()
    chrom_dr.get("https://youtube.com")
    #sleep(111)
