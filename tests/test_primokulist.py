import pytest
from playwright.sync_api import Page, expect

# Otevření hlavní stránky a kliknutí na cookies
@pytest.fixture
def open_homepage(page: Page):
    page.goto("https://www.primokulist.cz/")
    cookies = page.locator(".cmplz-accept")
    if cookies.is_visible():
        cookies.click()
    return page

def test_redirect_to_ocni_centrum_dejvice(open_homepage: Page):
    page = open_homepage
    # Kliknutí na odkaz "Oční centrum Dejvice"
    ocni = page.get_by_role("link", name="Oční centrum Dejvice")
    ocni.click()
    # Ověření URL
    expect(page).to_have_url("https://www.primokulist.cz/ocni-centrum-dejvice/", timeout=5000)

def test_navigation_menu(open_homepage: Page):
    page = open_homepage
    # Navigace do "Oční centrum Dejvice"
    ocni = page.get_by_role("link", name="Oční centrum Dejvice")
    ocni.click()

    # Kliknutí na "O nás" v menu
    o_nas = page.get_by_role("link", name="O nás")
    o_nas.click()
    # Kontrola nadpisu stránky
    expect(page.locator("h1")).to_have_text("O očním centru PRIM OKULIST Dejvice")

    # Kliknutí na "Objednání" a kontrola URL
    objednani = page.get_by_role("link", name="Objednání", exact=True)
    objednani.click()
    expect(page).to_have_url("https://www.primokulist.cz/ocni-centrum-dejvice/#!/objednani", timeout=5000)


def test_contact_form_validation(open_homepage: Page):
    page = open_homepage

    # Navigace na Kontakt
    page.get_by_role("link", name="Oční centrum Dejvice").click()
    page.get_by_role("link", name="Kontakt").click()

    # Vyplnění formuláře
    page.get_by_role("textbox", name="Jméno").fill("John")
    page.get_by_role("textbox", name="Příjmení").fill("Smith")
    page.get_by_role("textbox", name="E-mail").fill("test@test.com")
    page.get_by_placeholder("Žádost o objednání, dotaz nebo jiná zpráva").fill(
        "Dobrý den, žádám o termín na oční vyšetření."
    )
    page.get_by_role("checkbox").check()

    # Kliknutí na Odeslat 
    submit = page.locator('input[type="submit"]')
    submit.click()

    # Ověření chybové zprávy
    error = page.locator(".wpcf7-not-valid-tip-text")
    expect(error).to_be_visible(timeout=10000)
    expect(error).to_have_text(
        "Některá pole obsahují chybu. Opravte prosím zadané údaje a zkuste to znovu.",
        timeout=10000
    )

  