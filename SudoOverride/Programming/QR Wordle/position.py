from selenium import webdriver
import time

def get_correct_positions(url):

    # Find all elements with 'green' as one of their classes
    green_elements = driver.find_elements_by_css_selector('.green')

    # Extract the positions of the green elements with their IDs
    green_positions = {extract_position(element): element.get_attribute('id') for element in green_elements}
    time.sleep(0.25)
    return green_positions

def extract_position(element):
    # Extract the style attribute value
    style = element.get_attribute('style')

    # Extract the values of 'left' and 'top' from the style attribute
    left = int(style.split(';')[0].split(':')[1].strip().replace('vmin', ''))
    top = int(style.split(';')[1].split(':')[1].strip().replace('vmin', ''))

    # Calculate the position based on the formula {top}*8+{left}
    position = (top/10) * 8 + (left/10)
    return int(position)

def click_button(url):
    button = driver.find_element_by_class_name('button')  # Find and click the button
    button.click()
    time.sleep(1)


url = "https://qr.sudooverride.tech/"
save_path = "/images"
output_path = "merged_image.png"

# Open the URL in the browser
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get(url)
time.wait(5)
# Initialize an empty dictionary to store correct positions
all_correct_positions = {}

while len(all_correct_positions) < 64:

    correct_positions = get_correct_positions(url)
    if correct_positions:
        # Update the dictionary with correct positions found in this iteration
        all_correct_positions.update(correct_positions)

    click_button(url)
    
driver.close()

print("All correct positions found!")
print("Final correct positions:", all_correct_positions)

with open('positions.txt', 'w') as f:
    f.write(str(all_correct_positions))

