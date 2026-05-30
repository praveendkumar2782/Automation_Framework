import allure
from playwright.sync_api import Page, expect
from typing import List, Optional


class PlaygroundPage:
    """
    Page Object Model for testautomationpractice.blogspot.com (Synchronous)
    Encapsulates all locators and interactions with the Playground page.
    """
    
    # URL
    URL = "https://testautomationpractice.blogspot.com/"
    
    # Text Input Fields
    NAME_INPUT = "input[placeholder='First Name']"
    EMAIL_INPUT = "input[placeholder='Email']"
    PHONE_INPUT = "input[placeholder='Phone']"
    MESSAGE_TEXTAREA = "textarea[placeholder='Message']"
    
    # Standard Dropdown
    COUNTRY_DROPDOWN = "select#country"
    
    # Bootstrap Dropdown
    BOOTSTRAP_DROPDOWN = "div.dropdown"
    BOOTSTRAP_DROPDOWN_TOGGLE = "button.dropdown-toggle"
    BOOTSTRAP_DROPDOWN_MENU = "div.dropdown-menu"
    
    # Search Box
    SEARCH_BOX = "input[placeholder='Search']"
    SEARCH_BUTTON = "button.search-btn"
    
    # Datepicker
    DATEPICKER_INPUT = "input.datepicker"
    DATEPICKER_CALENDAR = "div.datepicker"
    
    # Dynamic Datepicker
    DYNAMIC_DATEPICKER_INPUT = "input#datepicker"
    
    # File Upload
    SINGLE_FILE_UPLOAD = "input[type='file']#file"
    MULTI_FILE_UPLOAD = "input[type='file'][multiple]"
    
    # Table Elements
    TABLE = "table.table"
    TABLE_ROWS = "table.table tbody tr"
    TABLE_HEADERS = "table.table thead th"
    
    # Dynamic Table
    DYNAMIC_TABLE = "div.dynamic-table"
    
    # Mouse Actions
    DOUBLE_CLICK_BUTTON = "button#doubleClickBtn"
    RIGHT_CLICK_BUTTON = "button#rightClickBtn"
    MOUSE_HOVER_ELEMENT = "div.hover-box"
    
    # Drag and Drop
    DRAGGABLE_ELEMENT = "div.draggable"
    DROP_ZONE = "div.drop-zone"
    
    # Keyboard Actions
    KEYBOARD_INPUT = "input#keyboardInput"
    
    # Header Footer
    HEADER = "header"
    FOOTER = "footer"
    
    # Image Elements
    IMAGES = "img"
    
    # Links
    LINK_ELEMENT = "a"
    
    # Buttons
    SUBMIT_BUTTON = "button[type='submit']"
    RESET_BUTTON = "button[type='reset']"
    
    # Labels
    RADIO_BUTTONS = "input[type='radio']"
    CHECKBOXES = "input[type='checkbox']"
    
    def __init__(self, page: Page):
        """Initialize with Playwright page instance (synchronous)."""
        self.page = page
    
    @allure.step("Navigate to Playground page")
    def navigate(self):
        """Navigate to the target application URL."""
        self.page.goto(self.URL, wait_until="domcontentloaded")
        self.page.wait_for_load_state("networkidle")
    
    @allure.step("Fill text field: {field_name} with value: {value}")
    def fill_text_field(self, selector: str, value: str, field_name: str):
        """Fill a text input field with the provided value."""
        field = self.page.locator(selector)
        field.fill(value)
        expect(field).to_have_value(value)
    
    @allure.step("Get text from field: {field_name}")
    def get_field_value(self, selector: str, field_name: str) -> str:
        """Get value from a text field."""
        field = self.page.locator(selector)
        return field.input_value()
    
    @allure.step("Fill First Name with: {value}")
    def fill_first_name(self, value: str):
        """Fill the First Name field."""
        self.fill_text_field(self.NAME_INPUT, value, "First Name")
    
    @allure.step("Fill Email with: {value}")
    def fill_email(self, value: str):
        """Fill the Email field."""
        self.fill_text_field(self.EMAIL_INPUT, value, "Email")
    
    @allure.step("Fill Phone with: {value}")
    def fill_phone(self, value: str):
        """Fill the Phone field."""
        self.fill_text_field(self.PHONE_INPUT, value, "Phone")
    
    @allure.step("Fill Message with: {value}")
    def fill_message(self, value: str):
        """Fill the Message textarea."""
        message_field = self.page.locator(self.MESSAGE_TEXTAREA)
        message_field.fill(value)
    
    @allure.step("Select from standard dropdown: {option}")
    def select_from_dropdown(self, selector: str, option: str):
        """Select an option from a standard dropdown."""
        dropdown = self.page.locator(selector)
        dropdown.select_option(option)
    
    @allure.step("Select country: {country}")
    def select_country(self, country: str):
        """Select a country from the country dropdown."""
        self.select_from_dropdown(self.COUNTRY_DROPDOWN, country)
    
    @allure.step("Get all dropdown options")
    def get_dropdown_options(self, selector: str) -> List[str]:
        """Get all available options from a dropdown."""
        dropdown = self.page.locator(selector)
        options = dropdown.locator("option").all_text_contents()
        return options
    
    @allure.step("Click bootstrap dropdown")
    def click_bootstrap_dropdown(self):
        """Click on bootstrap dropdown toggle."""
        toggle = self.page.locator(self.BOOTSTRAP_DROPDOWN).locator(self.BOOTSTRAP_DROPDOWN_TOGGLE)
        toggle.click()
        self.page.wait_for_timeout(500)
    
    @allure.step("Select bootstrap dropdown option: {option}")
    def select_bootstrap_option(self, option: str):
        """Select an option from bootstrap dropdown."""
        self.click_bootstrap_dropdown()
        option_element = self.page.locator(self.BOOTSTRAP_DROPDOWN_MENU).locator(f"a:has-text('{option}')")
        option_element.click()
    
    @allure.step("Search in searchbox: {query}")
    def search(self, query: str):
        """Fill the search box and submit."""
        search_field = self.page.locator(self.SEARCH_BOX)
        search_field.fill(query)
        search_btn = self.page.locator(self.SEARCH_BUTTON)
        search_btn.click()
    
    @allure.step("Get search box value")
    def get_search_value(self) -> str:
        """Get the value from the search box."""
        search_field = self.page.locator(self.SEARCH_BOX)
        return search_field.input_value()
    
    @allure.step("Set datepicker date: {date}")
    def set_datepicker_date(self, date: str):
        """Set a date in the datepicker field."""
        datepicker = self.page.locator(self.DATEPICKER_INPUT)
        datepicker.fill(date)
    
    @allure.step("Set dynamic datepicker date: {date}")
    def set_dynamic_datepicker_date(self, date: str):
        """Set a date in the dynamic datepicker field."""
        datepicker = self.page.locator(self.DYNAMIC_DATEPICKER_INPUT)
        datepicker.click()
        self.page.wait_for_timeout(500)
        datepicker.fill(date)
    
    @allure.step("Upload single file: {file_path}")
    def upload_single_file(self, file_path: str):
        """Upload a single file."""
        file_input = self.page.locator(self.SINGLE_FILE_UPLOAD)
        file_input.set_input_files(file_path)
    
    @allure.step("Upload multiple files")
    def upload_multiple_files(self, file_paths: List[str]):
        """Upload multiple files."""
        file_input = self.page.locator(self.MULTI_FILE_UPLOAD)
        file_input.set_input_files(file_paths)
    
    @allure.step("Get table row count")
    def get_table_row_count(self) -> int:
        """Get the number of rows in the table."""
        rows = self.page.locator(self.TABLE_ROWS)
        return rows.count()
    
    @allure.step("Get table cell value at row: {row}, column: {column}")
    def get_table_cell_value(self, row: int, column: int) -> str:
        """Get value from a specific cell in the table."""
        cell = self.page.locator(f"{self.TABLE_ROWS} >> nth={row-1} >> td >> nth={column-1}")
        return cell.text_content()
    
    @allure.step("Get all table headers")
    def get_table_headers(self) -> List[str]:
        """Get all table header values."""
        headers = self.page.locator(self.TABLE_HEADERS)
        return headers.all_text_contents()
    
    @allure.step("Double click element")
    def double_click_element(self):
        """Double click on an element."""
        button = self.page.locator(self.DOUBLE_CLICK_BUTTON)
        button.dblclick()
    
    @allure.step("Right click element")
    def right_click_element(self):
        """Right click on an element."""
        button = self.page.locator(self.RIGHT_CLICK_BUTTON)
        button.click(button="right")
    
    @allure.step("Hover over element")
    def hover_element(self):
        """Hover over an element."""
        element = self.page.locator(self.MOUSE_HOVER_ELEMENT)
        element.hover()
        self.page.wait_for_timeout(500)
    
    @allure.step("Drag element to drop zone")
    def drag_and_drop(self):
        """Perform drag and drop action."""
        draggable = self.page.locator(self.DRAGGABLE_ELEMENT)
        drop_zone = self.page.locator(self.DROP_ZONE)
        draggable.drag_to(drop_zone)
    
    @allure.step("Type in keyboard input: {text}")
    def type_keyboard_input(self, text: str):
        """Type text using keyboard."""
        keyboard_input = self.page.locator(self.KEYBOARD_INPUT)
        keyboard_input.click()
        keyboard_input.type(text)
    
    @allure.step("Clear keyboard input field")
    def clear_keyboard_input(self):
        """Clear the keyboard input field using keyboard shortcut."""
        keyboard_input = self.page.locator(self.KEYBOARD_INPUT)
        keyboard_input.click()
        keyboard_input.press("Control+A")
        keyboard_input.press("Delete")
    
    @allure.step("Get keyboard input value")
    def get_keyboard_input_value(self) -> str:
        """Get value from keyboard input field."""
        keyboard_input = self.page.locator(self.KEYBOARD_INPUT)
        return keyboard_input.input_value()
    
    @allure.step("Select radio button: {index}")
    def select_radio_button(self, index: int = 0):
        """Select a radio button by index."""
        radio_buttons = self.page.locator(self.RADIO_BUTTONS)
        radio_buttons.nth(index).click()
    
    @allure.step("Select checkbox: {index}")
    def select_checkbox(self, index: int = 0):
        """Select a checkbox by index."""
        checkboxes = self.page.locator(self.CHECKBOXES)
        checkboxes.nth(index).check()
    
    @allure.step("Unselect checkbox: {index}")
    def unselect_checkbox(self, index: int = 0):
        """Unselect a checkbox by index."""
        checkboxes = self.page.locator(self.CHECKBOXES)
        checkboxes.nth(index).uncheck()
    
    @allure.step("Get all checkboxes count")
    def get_checkboxes_count(self) -> int:
        """Get total count of checkboxes on page."""
        checkboxes = self.page.locator(self.CHECKBOXES)
        return checkboxes.count()
    
    @allure.step("Get all images count")
    def get_images_count(self) -> int:
        """Get total count of images on page."""
        images = self.page.locator(self.IMAGES)
        return images.count()
    
    @allure.step("Get image alt text: {index}")
    def get_image_alt_text(self, index: int = 0) -> str:
        """Get alt text from an image."""
        image = self.page.locator(self.IMAGES).nth(index)
        return image.get_attribute("alt")
    
    @allure.step("Verify image is visible: {index}")
    def verify_image_visible(self, index: int = 0) -> bool:
        """Verify if an image is visible on page."""
        image = self.page.locator(self.IMAGES).nth(index)
        return image.is_visible()
    
    @allure.step("Click submit button")
    def click_submit_button(self):
        """Click the submit button."""
        submit_btn = self.page.locator(self.SUBMIT_BUTTON)
        submit_btn.click()
    
    @allure.step("Click reset button")
    def click_reset_button(self):
        """Click the reset button."""
        reset_btn = self.page.locator(self.RESET_BUTTON)
        reset_btn.click()
    
    @allure.step("Click link: {link_text}")
    def click_link(self, link_text: str):
        """Click a link by its text content."""
        link = self.page.locator(f"{self.LINK_ELEMENT}:has-text('{link_text}')")
        link.click()
    
    @allure.step("Get all links count")
    def get_links_count(self) -> int:
        """Get total count of links on page."""
        links = self.page.locator(self.LINK_ELEMENT)
        return links.count()
    
    @allure.step("Get header element")
    def get_header_text(self) -> str:
        """Get header text."""
        header = self.page.locator(self.HEADER)
        return header.text_content()
    
    @allure.step("Get footer element")
    def get_footer_text(self) -> str:
        """Get footer text."""
        footer = self.page.locator(self.FOOTER)
        return footer.text_content()
    
    @allure.step("Get page title")
    def get_page_title(self) -> str:
        """Get the page title."""
        return self.page.title()
    
    @allure.step("Switch to iframe")
    def switch_to_iframe(self, iframe_index: int = 0):
        """Switch to an iframe."""
        iframes = self.page.frames
        if len(iframes) > iframe_index + 1:
            return iframes[iframe_index + 1]
        return None
    
    @allure.step("Get element text: {selector}")
    def get_element_text(self, selector: str) -> str:
        """Get text content of an element."""
        element = self.page.locator(selector)
        return element.text_content()
    
    @allure.step("Wait for element to be visible: {selector}")
    def wait_for_element_visible(self, selector: str, timeout: int = 30000):
        """Wait for an element to become visible."""
        element = self.page.locator(selector)
        element.wait_for(state="visible", timeout=timeout)
    
    @allure.step("Check if element is enabled: {selector}")
    def is_element_enabled(self, selector: str) -> bool:
        """Check if an element is enabled."""
        element = self.page.locator(selector)
        return element.is_enabled()
    
    @allure.step("Get element count: {selector}")
    def get_element_count(self, selector: str) -> int:
        """Get count of elements matching selector."""
        elements = self.page.locator(selector)
        return elements.count()

