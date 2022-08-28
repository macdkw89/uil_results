from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

# set up the driver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome("/Users/macdkw/Downloads/chromedriver")

# Navigate to the page
def home():
    driver.get("https://www.texasmusicforms.com/csrrptUILpublic.asp")

# get results button function
def click_results_button():
    get_results_button = driver.find_element(by=By.CLASS_NAME, value="btn-success")
    get_results_button.click()


# "Search again" button function
def click_search_button():
    search_again_button = driver.find_element(by=By.NAME, value="chan")
    search_again_button.click()
    driver.implicitly_wait(10)

# find the drop down menus and fill them out
def form_completer(year, region, contest_item):
    year_menu = driver.find_element(by=By.NAME, value="yr")
    region_menu = driver.find_element(by=By.NAME, value="reg")
    event_menu = driver.find_element(by=By.NAME, value="ev")
    year_menu.send_keys(year)
    region_menu.send_keys(f"Region {region}")
    event_menu.send_keys("Band")

    # find the hidden drop down menu, and collect its contents
    contest_menu = driver.find_element(by=By.NAME, value="cn")
    contest_menu_contents = contest_menu.find_elements(by=By.TAG_NAME, value="option")
    contest_menu_length = len(contest_menu_contents)
    contest_menu.send_keys(contest_menu_contents[contest_item].text)


# scrape the data
def scraper_loop():
    # make sure that were seeing all results, not just the top 20
    show_all_button = driver.find_element(by=By.NAME, value="DataTables_Table_0_length")
    show_all_button.send_keys("All")
    # get the table
    table = driver.find_elements(by=By.TAG_NAME, value="tbody")[1]
    table_rows = table.find_elements(by=By.TAG_NAME, value="tr")
    # loop through table contents
    for row in table_rows:
        cells = row.find_elements(by=By.TAG_NAME, value="td")
        column_content = []
        for cell in cells:
            cell_content_full = cell.text
            cell_content = cell_content_full.split("\n")
            for i in cell_content:
                column_content.append(i)
            #column_content.append(cell_content)
        row_content.append(column_content)

# convert to dataframe
def convert_to_dataframe():
    df = pd.DataFrame(row_content)
    if len(df.columns) == 21:
        df.columns = columns_21
    elif len(df.columns) == 22:
        df.columns = columns_22
    # export to csv
    df.to_csv(f"full_run/texas_music_forms_{year}_{region}_{contest_item}_band.csv")

columns_21 = ['Event', 'School', 'TEA', 'City', 'Directors', 'Conference', 'Classification', 'Year', 'ID', 
    'Stage Judge 1', 'Stage Judge 2', 'Stage Judge 3', 'Stage Final', 
    'SR Judge 1', 'SR Judge 2', 'SR Judge 3', 'SR Final', 'Award', 
    'Selection 1', 'Selection 2', 'Selection 3']

columns_22 = ['Event', 'School', 'TEA', 'City', 'Directors', 'Conference', 'Classification', 'Year', 'ID', 
    'Stage Judge 1', 'Stage Judge 2', 'Stage Judge 3', 'Stage Final', 
    'SR Judge 1', 'SR Judge 2', 'SR Judge 3', 'SR Final', 'Award', 
    'Selection 1', 'Selection 2', 'Selection 3', 'oops']

row_content = []

# Define year and region variables
year = 2005
region = 0

for y in range(2005, 2023):
    for r in range(0, 33):
        try:
            contest_item = 1
            region = region + 1
            for i in range(1, 15):
                try:
                    home()
                    form_completer(year, region, contest_item)
                    click_results_button()
                    scraper_loop()
                    convert_to_dataframe()
                    contest_item = contest_item + 1
                    row_content = []
                except:
                    print(f"{year}, {region}, {contest_item}")
                    break
        except:
            break
    year = year + 1
    region = 0