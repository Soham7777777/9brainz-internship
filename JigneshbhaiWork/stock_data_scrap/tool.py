import click
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
import os
import shutil
import csv


def print_error(message: str) -> None:
    click.echo(click.style(message, fg='red', bold=True))


def print_success(message: str) -> None:
    click.echo(click.style(message, fg='green', bold=True))


def print_warning(message: str) -> None:
    click.echo(click.style(message, fg='yellow', bold=True))


def print_info(message: str) -> None:
    click.echo(click.style(message, fg='blue', bold=True))


def print_default(message: str) -> None:
    click.echo(click.style(message, fg='white', bold=True))


# @contextmanager
def driver_context(is_headless: bool) -> WebDriver:
    """The driver context manager"""
    print_info("Initializing the browser...")
    firefox_profile = FirefoxProfile()
    firefox_profile.set_preference("browser.download.folderList", 2)
    firefox_profile.set_preference("browser.download.dir", DOWNLOAD_DIR) 
    firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/octet-stream")
    firefox_profile.set_preference("pdfjs.disabled", True)
    options = Options()
    if is_headless: options.add_argument("--headless")
    options.binary_location = FIREFOX_BIN
    options.profile = firefox_profile
    driver = webdriver.Firefox(options=options)
    print_info("Done initializing the browser")
    print()
    return driver
    # try:
    #     yield driver
    # finally:
    #     print_warning("Closing the browser...")
    #     driver.quit()


BASE_URL = "https://chartink.com/screener/52-week-high-stocks"
DOWNLOAD_DIR = "/home/soham/Documents/Internships/9brainz/Jigneshbhai_scrapping_work/downloads"
FIREFOX_BIN = "./firefox/firefox"

def verbose_driver_get(driver: WebDriver, url: str) -> None:
    """Perform driver.get verbosely"""
    print_info(f"GET: {url}")
    driver.get(url)
    print_info(f"Done getting the page")
    print()


def press_CSV_button(driver: WebDriver) -> None:
    print_warning("Clicking the button...")
    button_css_path = "button.btn-default:nth-child(3) > span:nth-child(1)"
    button_element = driver.find_element(By.CSS_SELECTOR, button_css_path)
    button_element.click()


def verbose_time_sleep(t_sec: int) -> None:
    """Verbosely wait to pass t_sec amount of seconds"""
    print_info(f"Waiting for {t_sec} seconds...")
    for i in range(1, t_sec + 1):
        time.sleep(1)
        print_info(f"{i} seconds passed.")
    print_info("Done waiting")
    print()


def clear_directory(directory_path):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        if os.path.isfile(file_path):
            os.remove(file_path)

        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    print_success("Ready to download...")


def rename_first_file(directory_path):
    # Loop through the files in the given directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            # Construct the new file path
            new_file_path = os.path.join(directory_path, "data.csv")
            
            # Rename the file
            os.rename(file_path, new_file_path)
            print(f"Renamed '{filename}' to 'data.csv'")
            break  # Exit the loop after renaming the first file
    print_success("File is downloaded properly...")


def csv_to_json(csv_file_path) -> list[dict[str, str]]:
    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        json_data = []
        
        for row in csv_reader:
            json_data.append(row)
    
    print_success(str(json_data))
    return json_data


def main(url: str | None, driver: WebDriver) -> list[dict[str, str]]:
    global BASE_URL
    if url is not None : BASE_URL = url
    clear_directory(DOWNLOAD_DIR)
    verbose_driver_get(driver, BASE_URL)
    verbose_time_sleep(1)
    press_CSV_button(driver)
    verbose_time_sleep(1)
    rename_first_file(DOWNLOAD_DIR)
    return csv_to_json(os.path.join(DOWNLOAD_DIR, 'data.csv'))


# if __name__ == "__main__":
#     main(None)
