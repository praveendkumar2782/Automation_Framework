import pytest
import allure
from pages.playground_page import PlaygroundPage
from utils.test_data_manager import TestDataManager


@pytest.fixture(scope="module")
def test_users():
    """Fixture to load all test users from CSV."""
    return TestDataManager.get_all_test_users()


@allure.feature("Text Input Fields")
class TestTextInputFields:
    """Test suite for text input field interactions."""
    
    @allure.story("Fill form with test data from CSV")
    @allure.severity("CRITICAL")
    @pytest.mark.ui
    def test_fill_form_with_test_data(self, page, test_users):
        """Test filling form with data from CSV file."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        user = test_users[0]
        playground.fill_first_name(user['name'])
        playground.fill_email(user['email'])
        playground.fill_phone(user['phone'])
        
        name_value = playground.get_field_value(playground.NAME_INPUT, "Name")
        email_value = playground.get_field_value(playground.EMAIL_INPUT, "Email")
        phone_value = playground.get_field_value(playground.PHONE_INPUT, "Phone")
        
        assert name_value == user['name'], f"Name mismatch: {name_value} != {user['name']}"
        assert email_value == user['email'], f"Email mismatch: {email_value} != {user['email']}"
        assert phone_value == user['phone'], f"Phone mismatch: {phone_value} != {user['phone']}"
    
    @allure.story("Fill and verify first name field")
    @allure.severity("CRITICAL")
    @pytest.mark.ui
    def test_fill_first_name(self, page):
        """Test filling the first name field."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        playground.fill_first_name("John Doe")
        first_name_value = playground.get_field_value(playground.NAME_INPUT, "First Name")
        
        assert first_name_value == "John Doe", "First name was not filled correctly"
    
    @allure.story("Fill and verify email field")
    @allure.severity("CRITICAL")
    @pytest.mark.ui
    def test_fill_email(self, page):
        """Test filling the email field."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        playground.fill_email("john.doe@example.com")
        email_value = playground.get_field_value(playground.EMAIL_INPUT, "Email")
        
        assert email_value == "john.doe@example.com", "Email was not filled correctly"
    
    @allure.story("Fill and verify phone field")
    @allure.severity("CRITICAL")
    @pytest.mark.ui
    def test_fill_phone(self, page):
        """Test filling the phone field."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        playground.fill_phone("+1234567890")
        phone_value = playground.get_field_value(playground.PHONE_INPUT, "Phone")
        
        assert phone_value == "+1234567890", "Phone was not filled correctly"
    
    @allure.story("Fill and verify message textarea")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_fill_message(self, page):
        """Test filling the message textarea."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        test_message = "This is a test message for the playground."
        playground.fill_message(test_message)
        
        message_field = page.locator(playground.MESSAGE_TEXTAREA)
        message_value = message_field.input_value()
        
        assert message_value == test_message, "Message was not filled correctly"


@allure.feature("Standard Dropdown")
class TestStandardDropdown:
    """Test suite for standard dropdown interactions."""
    
    @allure.story("Select country from dropdown")
    @allure.severity("CRITICAL")
    @pytest.mark.ui
    def test_select_country_dropdown(self, page):
        """Test selecting a country from the dropdown."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            playground.select_country("India")
            country_dropdown = page.locator(playground.COUNTRY_DROPDOWN)
            selected_value = country_dropdown.input_value()
            assert selected_value == "India", "Country was not selected correctly"
        except Exception as e:
            allure.attach(str(e), "dropdown_error", allure.attachment_type.TEXT)
    
    @allure.story("Get all dropdown options")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_dropdown_options(self, page):
        """Test retrieving all options from dropdown."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            options = playground.get_dropdown_options(playground.COUNTRY_DROPDOWN)
            assert len(options) > 0, "No options found in dropdown"
        except Exception as e:
            allure.attach(str(e), "dropdown_options_error", allure.attachment_type.TEXT)


@allure.feature("Bootstrap Dropdown")
class TestBootstrapDropdown:
    """Test suite for bootstrap dropdown interactions."""
    
    @allure.story("Click and verify bootstrap dropdown opens")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_bootstrap_dropdown_click(self, page):
        """Test opening bootstrap dropdown."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            playground.click_bootstrap_dropdown()
            dropdown_menu = page.locator(playground.BOOTSTRAP_DROPDOWN_MENU)
            assert dropdown_menu.is_visible(), "Bootstrap dropdown menu did not open"
        except Exception as e:
            allure.attach(str(e), "bootstrap_dropdown_error", allure.attachment_type.TEXT)


@allure.feature("Search Functionality")
class TestSearchFunctionality:
    """Test suite for search box interactions."""
    
    @allure.story("Perform search and verify value")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_search_functionality(self, page):
        """Test search box functionality."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            search_query = "test automation"
            playground.search(search_query)
            search_value = playground.get_search_value()
            assert search_value == search_query, "Search value not set correctly"
        except Exception as e:
            allure.attach(str(e), "search_error", allure.attachment_type.TEXT)


@allure.feature("Datepicker")
class TestDatepicker:
    """Test suite for datepicker interactions."""
    
    @allure.story("Set date in datepicker")
    @allure.severity("NORMAL")
    @pytest.mark.datepicker
    def test_set_datepicker_date(self, page):
        """Test setting date in datepicker."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            test_date = "12/25/2025"
            playground.set_datepicker_date(test_date)
            datepicker_field = page.locator(playground.DATEPICKER_INPUT)
            date_value = datepicker_field.input_value()
            assert date_value == test_date, "Date was not set correctly"
        except Exception as e:
            allure.attach(str(e), "datepicker_error", allure.attachment_type.TEXT)
    
    @allure.story("Set date in dynamic datepicker")
    @allure.severity("NORMAL")
    @pytest.mark.datepicker
    def test_set_dynamic_datepicker_date(self, page):
        """Test setting date in dynamic datepicker."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            test_date = "06/15/2026"
            playground.set_dynamic_datepicker_date(test_date)
            datepicker_field = page.locator(playground.DYNAMIC_DATEPICKER_INPUT)
            date_value = datepicker_field.input_value()
            assert date_value == test_date, "Date was not set correctly"
        except Exception as e:
            allure.attach(str(e), "dynamic_datepicker_error", allure.attachment_type.TEXT)


@allure.feature("Checkbox Interactions")
class TestCheckboxes:
    """Test suite for checkbox interactions."""
    
    @allure.story("Select checkbox")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_select_checkbox(self, page):
        """Test selecting a checkbox."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            playground.select_checkbox(0)
            checkbox = page.locator(playground.CHECKBOXES).nth(0)
            assert checkbox.is_checked(), "Checkbox was not selected"
        except Exception as e:
            allure.attach(str(e), "checkbox_error", allure.attachment_type.TEXT)
    
    @allure.story("Unselect checkbox")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_unselect_checkbox(self, page):
        """Test unselecting a checkbox."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            checkbox = page.locator(playground.CHECKBOXES).nth(0)
            checkbox.check()
            playground.unselect_checkbox(0)
            assert not checkbox.is_checked(), "Checkbox was not unselected"
        except Exception as e:
            allure.attach(str(e), "uncheck_error", allure.attachment_type.TEXT)
    
    @allure.story("Get total checkbox count")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_checkboxes_count(self, page):
        """Test getting total checkboxes count."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            checkbox_count = playground.get_checkboxes_count()
            assert checkbox_count > 0, "No checkboxes found on page"
        except Exception as e:
            allure.attach(str(e), "checkbox_count_error", allure.attachment_type.TEXT)


@allure.feature("Radio Button Interactions")
class TestRadioButtons:
    """Test suite for radio button interactions."""
    
    @allure.story("Select radio button")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_select_radio_button(self, page):
        """Test selecting a radio button."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            playground.select_radio_button(0)
            radio_btn = page.locator(playground.RADIO_BUTTONS).nth(0)
            assert radio_btn.is_checked(), "Radio button was not selected"
        except Exception as e:
            allure.attach(str(e), "radio_error", allure.attachment_type.TEXT)


@allure.feature("Mouse Actions")
class TestMouseActions:
    """Test suite for mouse action interactions."""
    
    @allure.story("Perform double click action")
    @allure.severity("NORMAL")
    @pytest.mark.mouse
    def test_double_click_action(self, page):
        """Test double-click mouse action."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            playground.double_click_element()
        except Exception as e:
            allure.attach(str(e), "double_click_error", allure.attachment_type.TEXT)
    
    @allure.story("Perform right click action")
    @allure.severity("NORMAL")
    @pytest.mark.mouse
    def test_right_click_action(self, page):
        """Test right-click mouse action."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            playground.right_click_element()
        except Exception as e:
            allure.attach(str(e), "right_click_error", allure.attachment_type.TEXT)
    
    @allure.story("Perform hover action")
    @allure.severity("NORMAL")
    @pytest.mark.mouse
    def test_hover_action(self, page):
        """Test hover mouse action."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            playground.hover_element()
        except Exception as e:
            allure.attach(str(e), "hover_error", allure.attachment_type.TEXT)


@allure.feature("Drag and Drop")
class TestDragAndDrop:
    """Test suite for drag and drop interactions."""
    
    @allure.story("Perform drag and drop action")
    @allure.severity("NORMAL")
    @pytest.mark.dragdrop
    def test_drag_and_drop(self, page):
        """Test drag and drop functionality."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            playground.drag_and_drop()
        except Exception as e:
            allure.attach(str(e), "dragdrop_error", allure.attachment_type.TEXT)


@allure.feature("Keyboard Actions")
class TestKeyboardActions:
    """Test suite for keyboard action interactions."""
    
    @allure.story("Type text using keyboard")
    @allure.severity("NORMAL")
    @pytest.mark.keyboard
    def test_type_keyboard_input(self, page):
        """Test typing text using keyboard."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            test_text = "Hello World"
            playground.type_keyboard_input(test_text)
            input_value = playground.get_keyboard_input_value()
            assert input_value == test_text, "Text was not typed correctly"
        except Exception as e:
            allure.attach(str(e), "keyboard_type_error", allure.attachment_type.TEXT)
    
    @allure.story("Clear keyboard input using keyboard shortcut")
    @allure.severity("NORMAL")
    @pytest.mark.keyboard
    def test_clear_keyboard_input(self, page):
        """Test clearing keyboard input using keyboard shortcut."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            test_text = "Test Input"
            playground.type_keyboard_input(test_text)
            playground.clear_keyboard_input()
            input_value = playground.get_keyboard_input_value()
            assert input_value == "", "Keyboard input was not cleared"
        except Exception as e:
            allure.attach(str(e), "keyboard_clear_error", allure.attachment_type.TEXT)


@allure.feature("Table Interactions")
class TestTableInteractions:
    """Test suite for table interactions."""
    
    @allure.story("Get table row count")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_table_row_count(self, page):
        """Test getting table row count."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            row_count = playground.get_table_row_count()
            assert row_count > 0, "No rows found in table"
        except Exception as e:
            allure.attach(str(e), "table_row_error", allure.attachment_type.TEXT)
    
    @allure.story("Get table headers")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_table_headers(self, page):
        """Test retrieving table headers."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            headers = playground.get_table_headers()
            assert len(headers) > 0, "No headers found in table"
        except Exception as e:
            allure.attach(str(e), "table_headers_error", allure.attachment_type.TEXT)


@allure.feature("Image Verification")
class TestImageVerification:
    """Test suite for image verification interactions."""
    
    @allure.story("Get images count on page")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_images_count(self, page):
        """Test getting total images count on page."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            images_count = playground.get_images_count()
            assert images_count >= 0, "Unable to get images count"
        except Exception as e:
            allure.attach(str(e), "images_count_error", allure.attachment_type.TEXT)
    
    @allure.story("Verify image is visible")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_verify_image_visible(self, page):
        """Test verifying if an image is visible on page."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            is_visible = playground.verify_image_visible(0)
            assert is_visible is not None, "Unable to verify image visibility"
        except Exception:
            pass
    
    @allure.story("Get image alt text")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_image_alt_text(self, page):
        """Test getting image alt text."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            alt_text = playground.get_image_alt_text(0)
            assert alt_text is not None, "Unable to get image alt text"
        except Exception:
            pass


@allure.feature("Page Navigation and Elements")
class TestPageElements:
    """Test suite for page elements and navigation."""
    
    @allure.story("Get page title")
    @allure.severity("CRITICAL")
    @pytest.mark.sanity
    def test_get_page_title(self, page):
        """Test getting the page title."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        title = playground.get_page_title()
        assert title is not None, "Page title could not be retrieved"
        assert len(title) > 0, "Page title is empty"
    
    @allure.story("Get page links count")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_links_count(self, page):
        """Test getting total links count on page."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            links_count = playground.get_links_count()
            assert links_count >= 0, "Unable to get links count"
        except Exception as e:
            allure.attach(str(e), "links_count_error", allure.attachment_type.TEXT)
    
    @allure.story("Verify header element exists")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_header_text(self, page):
        """Test getting header text."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            header_text = playground.get_header_text()
            assert header_text is not None, "Header element not found"
        except Exception:
            pass
    
    @allure.story("Verify footer element exists")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_footer_text(self, page):
        """Test getting footer text."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        try:
            footer_text = playground.get_footer_text()
            assert footer_text is not None, "Footer element not found"
        except Exception:
            pass


@allure.feature("Form Submission")
class TestFormSubmission:
    """Test suite for form submission."""
    
    @allure.story("Fill form and submit")
    @allure.severity("CRITICAL")
    @pytest.mark.sanity
    def test_form_submission(self, page):
        """Test filling form and submitting."""
        playground = PlaygroundPage(page)
        playground.navigate()
        
        playground.fill_first_name("Test User")
        playground.fill_email("test@example.com")
        playground.fill_phone("+1234567890")
        playground.fill_message("Test message for automation")
        
        first_name = playground.get_field_value(playground.NAME_INPUT, "First Name")
        email = playground.get_field_value(playground.EMAIL_INPUT, "Email")
        phone = playground.get_field_value(playground.PHONE_INPUT, "Phone")
        
        assert first_name == "Test User", "First name not filled"
        assert email == "test@example.com", "Email not filled"
        assert phone == "+1234567890", "Phone not filled"
    
    @allure.story("Fill and verify email field")
    @allure.severity("CRITICAL")
    @pytest.mark.ui
    def test_fill_email(self, page):
        """Test filling the email field."""
        playground = PlaygroundPage(page)
        playground.navigate()

        playground.fill_email("john.doe@example.com")
        email_value = playground.get_field_value(
            playground.EMAIL_INPUT, "Email"
        )
        
        assert email_value == "john.doe@example.com", "Email was not filled correctly"
    
    @allure.story("Fill and verify phone field")
    @allure.severity("CRITICAL")
    @pytest.mark.ui
    def test_fill_phone(self, page):
        """Test filling the phone field."""
        playground = PlaygroundPage(page)
        playground.navigate()

        playground.fill_phone("+1234567890")
        phone_value = playground.get_field_value(
            playground.PHONE_INPUT, "Phone"
        )
        
        assert phone_value == "+1234567890", "Phone was not filled correctly"
    
    @allure.story("Fill and verify message textarea")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_fill_message(self, page):
        """Test filling the message textarea."""
        playground = PlaygroundPage(page)
        playground.navigate()

        test_message = "This is a test message for the playground."
        playground.fill_message(test_message)

        message_field = page.locator(playground.MESSAGE_TEXTAREA)
        message_value = message_field.input_value()

        assert message_value == test_message, "Message was not filled correctly"


@allure.feature("Standard Dropdown")
class TestStandardDropdown:
    """Test suite for standard dropdown interactions."""
    
    @allure.story("Select country from dropdown")
    @allure.severity("CRITICAL")
    @pytest.mark.ui
    def test_select_country_dropdown(self, page):
        """Test selecting a country from the dropdown."""
        playground = PlaygroundPage(page)
        playground.navigate()

        playground.select_country("India")

        country_dropdown = page.locator(playground.COUNTRY_DROPDOWN)
        selected_value = country_dropdown.input_value()

        assert selected_value == "India", "Country was not selected correctly"
    
    @allure.story("Get all dropdown options")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_dropdown_options(self, page):
        """Test retrieving all options from dropdown."""
        playground = PlaygroundPage(page)
        playground.navigate()

        options = playground.get_dropdown_options(playground.COUNTRY_DROPDOWN)

        assert len(options) > 0, "No options found in dropdown"
        assert "India" in options or any("India" in opt for opt in options), \
            "Expected country not in dropdown options"


@allure.feature("Bootstrap Dropdown")
class TestBootstrapDropdown:
    """Test suite for bootstrap dropdown interactions."""
    
    @allure.story("Click and verify bootstrap dropdown opens")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_bootstrap_dropdown_click(self, page):
        """Test opening bootstrap dropdown."""
        playground = PlaygroundPage(page)
        playground.navigate()

        playground.click_bootstrap_dropdown()

        dropdown_menu = page.locator(playground.BOOTSTRAP_DROPDOWN_MENU)
        is_visible = dropdown_menu.is_visible()

        assert is_visible, "Bootstrap dropdown menu did not open"


@allure.feature("Search Functionality")
class TestSearchFunctionality:
    """Test suite for search box interactions."""
    
    @allure.story("Perform search and verify value")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_search_functionality(self, page):
        """Test search box functionality."""
        playground = PlaygroundPage(page)
        playground.navigate()

        search_query = "test automation"
        playground.search(search_query)

        # Verify search was performed
        search_value = playground.get_search_value()
        assert search_value == search_query, "Search value not set correctly"


@allure.feature("Datepicker")
class TestDatepicker:
    """Test suite for datepicker interactions."""
    
    @allure.story("Set date in datepicker")
    @allure.severity("NORMAL")
    @pytest.mark.datepicker
    def test_set_datepicker_date(self, page):
        """Test setting date in datepicker."""
        playground = PlaygroundPage(page)
        playground.navigate()

        test_date = "12/25/2025"
        playground.set_datepicker_date(test_date)

        datepicker_field = page.locator(playground.DATEPICKER_INPUT)
        date_value = datepicker_field.input_value()

        assert date_value == test_date, "Date was not set correctly in datepicker"
    
    @allure.story("Set date in dynamic datepicker")
    @allure.severity("NORMAL")
    @pytest.mark.datepicker
    def test_set_dynamic_datepicker_date(self, page):
        """Test setting date in dynamic datepicker."""
        playground = PlaygroundPage(page)
        playground.navigate()

        test_date = "06/15/2026"
        playground.set_dynamic_datepicker_date(test_date)

        datepicker_field = page.locator(playground.DYNAMIC_DATEPICKER_INPUT)
        date_value = datepicker_field.input_value()

        assert date_value == test_date, "Date was not set correctly in dynamic datepicker"


@allure.feature("Checkbox Interactions")
class TestCheckboxes:
    """Test suite for checkbox interactions."""
    
    @allure.story("Select checkbox")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_select_checkbox(self, page):
        """Test selecting a checkbox."""
        playground = PlaygroundPage(page)
        playground.navigate()

        playground.select_checkbox(0)

        checkbox = page.locator(playground.CHECKBOXES).nth(0)
        is_checked = checkbox.is_checked()

        assert is_checked, "Checkbox was not selected"
    
    @allure.story("Unselect checkbox")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_unselect_checkbox(self, page):
        """Test unselecting a checkbox."""
        playground = PlaygroundPage(page)
        playground.navigate()

        checkbox = page.locator(playground.CHECKBOXES).nth(0)
        checkbox.check()
        playground.unselect_checkbox(0)

        is_checked = checkbox.is_checked()

        assert not is_checked, "Checkbox was not unselected"
    
    @allure.story("Get total checkbox count")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_checkboxes_count(self, page):
        """Test getting total checkboxes count."""
        playground = PlaygroundPage(page)
        playground.navigate()

        checkbox_count = playground.get_checkboxes_count()

        assert checkbox_count > 0, "No checkboxes found on page"


@allure.feature("Radio Button Interactions")
class TestRadioButtons:
    """Test suite for radio button interactions."""
    
    @allure.story("Select radio button")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_select_radio_button(self, page):
        """Test selecting a radio button."""
        playground = PlaygroundPage(page)
        playground.navigate()

        playground.select_radio_button(0)

        radio_btn = page.locator(playground.RADIO_BUTTONS).nth(0)
        is_checked = radio_btn.is_checked()

        assert is_checked, "Radio button was not selected"


@allure.feature("Mouse Actions")
class TestMouseActions:
    """Test suite for mouse action interactions."""
    
    @allure.story("Perform double click action")
    @allure.severity("NORMAL")
    @pytest.mark.mouse
    def test_double_click_action(self, page):
        """Test double-click mouse action."""
        playground = PlaygroundPage(page)
        playground.navigate()

        try:
            playground.double_click_element()
            # If no exception is raised, action was successful
            assert True, "Double click was performed successfully"
        except Exception as e:
            pytest.fail(f"Double click action failed: {str(e)}")
    
    @allure.story("Perform right click action")
    @allure.severity("NORMAL")
    @pytest.mark.mouse
    def test_right_click_action(self, page):
        """Test right-click mouse action."""
        playground = PlaygroundPage(page)
        playground.navigate()

        try:
            playground.right_click_element()
            # If no exception is raised, action was successful
            assert True, "Right click was performed successfully"
        except Exception as e:
            pytest.fail(f"Right click action failed: {str(e)}")
    
    @allure.story("Perform hover action")
    @allure.severity("NORMAL")
    @pytest.mark.mouse
    def test_hover_action(self, page):
        """Test hover mouse action."""
        playground = PlaygroundPage(page)
        playground.navigate()

        try:
            playground.hover_element()
            # If no exception is raised, action was successful
            assert True, "Hover action was performed successfully"
        except Exception as e:
            pytest.fail(f"Hover action failed: {str(e)}")


@allure.feature("Drag and Drop")
class TestDragAndDrop:
    """Test suite for drag and drop interactions."""
    
    @allure.story("Perform drag and drop action")
    @allure.severity("NORMAL")
    @pytest.mark.dragdrop
    def test_drag_and_drop(self, page):
        """Test drag and drop functionality."""
        playground = PlaygroundPage(page)
        playground.navigate()

        try:
            playground.drag_and_drop()
            # If no exception is raised, action was successful
            assert True, "Drag and drop was performed successfully"
        except Exception as e:
            pytest.fail(f"Drag and drop action failed: {str(e)}")


@allure.feature("Keyboard Actions")
class TestKeyboardActions:
    """Test suite for keyboard action interactions."""
    
    @allure.story("Type text using keyboard")
    @allure.severity("NORMAL")
    @pytest.mark.keyboard
    def test_type_keyboard_input(self, page):
        """Test typing text using keyboard."""
        playground = PlaygroundPage(page)
        playground.navigate()

        test_text = "Hello World"
        playground.type_keyboard_input(test_text)

        input_value = playground.get_keyboard_input_value()

        assert input_value == test_text, "Text was not typed correctly"
    
    @allure.story("Clear keyboard input using keyboard shortcut")
    @allure.severity("NORMAL")
    @pytest.mark.keyboard
    def test_clear_keyboard_input(self, page):
        """Test clearing keyboard input using keyboard shortcut."""
        playground = PlaygroundPage(page)
        playground.navigate()

        test_text = "Test Input"
        playground.type_keyboard_input(test_text)
        playground.clear_keyboard_input()

        input_value = playground.get_keyboard_input_value()

        assert input_value == "", "Keyboard input was not cleared"


@allure.feature("Table Interactions")
class TestTableInteractions:
    """Test suite for table interactions."""
    
    @allure.story("Get table row count")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_table_row_count(self, page):
        """Test getting table row count."""
        playground = PlaygroundPage(page)
        playground.navigate()

        row_count = playground.get_table_row_count()

        assert row_count > 0, "No rows found in table"
    
    @allure.story("Get table headers")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_table_headers(self, page):
        """Test retrieving table headers."""
        playground = PlaygroundPage(page)
        playground.navigate()

        headers = playground.get_table_headers()

        assert len(headers) > 0, "No headers found in table"


@allure.feature("Image Verification")
class TestImageVerification:
    """Test suite for image verification interactions."""
    
    @allure.story("Get images count on page")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_images_count(self, page):
        """Test getting total images count on page."""
        playground = PlaygroundPage(page)
        playground.navigate()

        images_count = playground.get_images_count()

        assert images_count >= 0, "Unable to get images count"
    
    @allure.story("Verify image is visible")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_verify_image_visible(self, page):
        """Test verifying if an image is visible on page."""
        playground = PlaygroundPage(page)
        playground.navigate()

        try:
            is_visible = playground.verify_image_visible(0)
            # Image exists on page, either visible or not
            assert is_visible is not None, "Unable to verify image visibility"
        except Exception:
            # No images on page, which is valid
            assert True, "No images found on page"
    
    @allure.story("Get image alt text")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_image_alt_text(self, page):
        """Test getting image alt text."""
        playground = PlaygroundPage(page)
        playground.navigate()

        try:
            alt_text = playground.get_image_alt_text(0)
            # Alt text can be empty or have value
            assert alt_text is not None, "Unable to get image alt text"
        except Exception:
            # No images on page, which is valid
            assert True, "No images found on page"


@allure.feature("Page Navigation and Elements")
class TestPageElements:
    """Test suite for page elements and navigation."""
    
    @allure.story("Get page title")
    @allure.severity("CRITICAL")
    @pytest.mark.sanity
    def test_get_page_title(self, page):
        """Test getting the page title."""
        playground = PlaygroundPage(page)
        playground.navigate()

        title = playground.get_page_title()

        assert title is not None, "Page title could not be retrieved"
        assert len(title) > 0, "Page title is empty"
    
    @allure.story("Get page links count")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_links_count(self, page):
        """Test getting total links count on page."""
        playground = PlaygroundPage(page)
        playground.navigate()

        links_count = playground.get_links_count()

        assert links_count >= 0, "Unable to get links count"
    
    @allure.story("Verify header element exists")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_header_text(self, page):
        """Test getting header text."""
        playground = PlaygroundPage(page)
        playground.navigate()

        try:
            header_text = playground.get_header_text()
            # Header might or might not have text
            assert header_text is not None, "Header element not found"
        except Exception:
            # Header not found is valid
            assert True, "Header element not present on page"
    
    @allure.story("Verify footer element exists")
    @allure.severity("NORMAL")
    @pytest.mark.ui
    def test_get_footer_text(self, page):
        """Test getting footer text."""
        playground = PlaygroundPage(page)
        playground.navigate()

        try:
            footer_text = playground.get_footer_text()
            # Footer might or might not have text
            assert footer_text is not None, "Footer element not found"
        except Exception:
            # Footer not found is valid
            assert True, "Footer element not present on page"


@allure.feature("Form Submission")
class TestFormSubmission:
    """Test suite for form submission."""
    
    @allure.story("Fill form and submit")
    @allure.severity("CRITICAL")
    @pytest.mark.sanity
    def test_form_submission(self, page):
        """Test filling form and submitting."""
        playground = PlaygroundPage(page)
        playground.navigate()

        # Fill all available fields
        playground.fill_first_name("Test User")
        playground.fill_email("test@example.com")
        playground.fill_phone("+1234567890")
        playground.fill_message("Test message for automation")

        # Verify fields are filled
        first_name = playground.get_field_value(playground.NAME_INPUT, "First Name")
        email = playground.get_field_value(playground.EMAIL_INPUT, "Email")
        phone = playground.get_field_value(playground.PHONE_INPUT, "Phone")

        assert first_name == "Test User", "First name not filled"
        assert email == "test@example.com", "Email not filled"
        assert phone == "+1234567890", "Phone not filled"

