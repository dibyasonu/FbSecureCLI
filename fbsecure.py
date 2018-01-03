import click
import time
import os
import sys
import getpass
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.phantomjs.webdriver import WebDriver


@click.group()
def cli():
    pass

def get_title(driver):
    html_page = driver.page_source
    soup = BeautifulSoup(html_page,'html.parser')
    return soup.title.string


@cli.command('edit',short_help='Edits the fb password')
@click.option('--email',prompt=True,help="Email for fb account")
def change_pass(email):
    email=email.strip()
    Ppass=input("Enter your current password: ")
    if os.name == 'nt':
        pathr = 'phantomjs.exe'
    else:
        pathr = './phantomjs'
    driver = webdriver.PhantomJS(pathr, service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any'])
    url = "https://mbasic.facebook.com/"
    driver.get(url)
    # time.sleep(2)
    EMAIL=driver.find_element_by_name("email")
    EMAIL.send_keys(email)
    PASSWORD=driver.find_element_by_name("pass")
    PASSWORD.send_keys(Ppass)

    LOGIN=driver.find_element_by_name("login")
    LOGIN.click()
    # time.sleep(5)
    

    if get_title(driver) != "Log in to Facebook | Facebook":
        click.secho("Login succesful !",fg='green',bold=True)
        driver.get('https://mbasic.facebook.com/settings/security/password/') 
        PREPASS=driver.find_element_by_name("password_old")
        NEWPASS=driver.find_element_by_name("password_new")
        CONPASS=driver.find_element_by_name("password_confirm")

        click.secho("Enter your New password: ",fg='blue',bold=True)
        Npass=input()
        PREPASS.send_keys(Ppass)
        NEWPASS.send_keys(Npass)
        CONPASS.send_keys(Npass)
        SUBMIT=driver.find_element_by_name("save")
        SUBMIT.click()
        # time.sleep(5)
        driver.quit()
        click.secho("Password changed succesfuly !",fg='green',bold=True)
        sys.exit(0)
    else:
        click.secho("Invalid Email Id or Password, Try Login Again!",fg='red',bold=True)
        sys.exit(0)