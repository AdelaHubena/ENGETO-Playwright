import pytest
from playwright.sync_api import Page, expect

# Otevře hlavní stránku a přijme cookies, aby neblokovaly další akce
@pytest.fixture(autouse=True)
def accept_cookies(page: Page):
    page.goto("https://vaspraktikpraha.cz/")
    cookies_banner = page.locator(".cookies-policy-banner")  
    cookies_banner.locator(".cookies-accept-btn", has_text="POVOLIT VŠE").click()

# Ověření, že po přijetí cookies se banner již nezobrazuje
def test_cookie_banner_hidden_after_accept(page: Page):
    expect(page.locator(".cookies-policy-banner")).to_be_hidden()

# Test navigace mezi ordinacemi – výběr ordinace Praha 15
def test_navigation_between_offices(page: Page):
    # Otevření menu "Naše ordinace"
    menu_nase_ordinace = page.get_by_role("button", name="Naše ordinace")
    menu_nase_ordinace.click()

    # Kliknutí na konkrétní ordinaci
    ordinace_praha15 = page.locator('a[href="/praha-15"]')
    ordinace_praha15.click()

    # Ověření správného nadpisu a URL stránky
    expect(page.locator(".main-carousel-h2").first).to_have_text("Váš praktik Praha 15")
    expect(page).to_have_url("https://vaspraktikpraha.cz/praha-15")

# Vyplnění základních osobních údajů při registraci
def test_registration_to_office(page: Page):

    # Přechod na registrační formulář
    zaregistrujte_se_knam = page.locator('.register-text-desktop:text-is("Zaregistrujte se k nám")')
    zaregistrujte_se_knam.click()

    # Výběr ordinace Národní
    ordinace_narodni = page.locator(".registration-office-narodni").locator(".checkmark")
    ordinace_narodni.check()

    # Vyplnění osobních údajů
    jmeno = page.locator(".registration-office-personal-information-wrapper").get_by_role("textbox", name="Jméno")
    jmeno.fill("John")

    prijmeni = page.locator(".registration-office-personal-information-wrapper").get_by_role("textbox", name="Příjmení")
    prijmeni.fill("Smith")

    email = page.locator(".registration-office-personal-information-wrapper").get_by_role("textbox", name="E-mail")
    email.fill("test@test.com")

    # Ověření, že se hodnoty správně propsaly do inputů
    expect(jmeno).to_have_value("John")
    expect(prijmeni).to_have_value("Smith")
    expect(email).to_have_value("test@test.com")

# Test výběru zdravotní pojišťovny v registračním formuláři
def test_select_insurance(page: Page):

    # Otevření registrační sekce
    zaregistrujte_se_knam = page.locator('.register-text-desktop:text-is("Zaregistrujte se k nám")')
    zaregistrujte_se_knam.click()

    # Výběr ordinace
    ordinace_narodni = page.locator(".registration-office-narodni").locator(".checkmark")
    ordinace_narodni.check()

    # Výběr zdravotní pojišťovny ze selectu
    vyber_pojistovny = page.locator(".registration-office-more-information-wrapper").locator("#insurance_id", has_text="Vyberte svou pojišťovnu")
    vyber_pojistovny.click()
    vyber_pojistovny.select_option(label="VoZP - Vojenská zdravotní pojišťovna ČR (201)")

    # Ověření, že je vybraná správná pojišťovna
    expect(vyber_pojistovny.locator("option:checked")).to_have_text("VoZP - Vojenská zdravotní pojišťovna ČR (201)")

# Test odkazu na Instagram
def test_contact_instagram(page: Page):
    menu_kontakt = page.get_by_role("button", name="Kontakt")
    menu_kontakt.click()

    menu_kontakt_ordinace = page.locator('.dropdown-menu.dropdown-2col.show >> a.dropdown-item[href="/kontakt"]')
    expect(menu_kontakt_ordinace).to_be_visible()
    menu_kontakt_ordinace.click()

    # Kliknutí na Instagram – otevření nové záložky
    instagram_btn = page.locator('.contact-office-items-wrapper a[href="https://www.instagram.com/vaspraktikpraha/"]').first
    with page.context.expect_page() as new_page_info:
        instagram_btn.click()
    new_page = new_page_info.value

    new_page.wait_for_url("https://www.instagram.com/vaspraktikpraha/")
    
    expect(new_page).to_have_url("https://www.instagram.com/vaspraktikpraha/")