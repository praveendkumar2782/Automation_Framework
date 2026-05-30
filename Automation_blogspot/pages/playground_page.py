import self
from playwright.sync_api import Page


class PlaygroundPage(Page):
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://testautomationpractice.blogspot.com/"
        self.name_input = page.locator("#name")
        self.email_input = page.locator("#email")
        self.phone_input = page.locator("#phone")
        self.address_input = page.locator("#textarea")
        self.country_dropdown = page.locator("#country")
        self.colors_dropdown = page.locator("#colors")
        self.datepicker_input = page.locator("#datepicker")


    def navigate(self):
        self.page.goto(self.url)


    def fill_contact_form(self, name: str, email: str, phone: str, address: str,):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.phone_input.fill(phone)
        self.address_input.fill(address)

    def select_gender(selfself, gender: str):
        self.page.locator(f"input[value='{gender.lower()}']").check()


    def select_days(self, days: list):

        for day in days: 
            self.page.locator(f"input#{day.lower()}]").check()

    def select_country_and_colors(self, country: str,  colors: list):
        self.country_dropdown.select_option(label=country)
        self.colors_dropdown.select_option(value=colors)


    def select_calendar_date(self, date: str, target_month_year=None, target_day=None):
        self.datepicker_input.click()
        while True:
            current_header = self.page.locator(".ui-datepicker-title").inner_text()

            current_header_clean= " ".join(current_header.split())
            if target_month_year.lower( in current_header_clean.lower()):
                break
            self.page.locator(".ui-datepicker-next").click()

        self.page.locator(f"table.ui-datepicker-calendar a:text-is()'{target_day}')").click()


    def verify_table_price(self, book_title: str) -> str:
        row = self.page.locator(f"table[name='Book table'] tr:has-text('{book_title}')")
        price = row.locator("td").nth(3).inner_text()
        return price


    def handle_native_alert(self) -> str:
        alert_text =[]


        def  listener(dialog):
            alert_text.append(dialog.message)
            dialog.accept()

        self.page.on("dialog", listener)
        self.page.locator("button: has text ('Alert')").click()

        self.page.remove_listener("dialog", listener)
        return alert_text[0] if alert_text else ("")


