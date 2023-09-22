from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.instagram.com/accounts/login/")
    page.get_by_label("Telefone, nome de usuário ou email").click()
    page.get_by_label("Telefone, nome de usuário ou email").fill("fael9591@gmail.com")
    page.get_by_label("Telefone, nome de usuário ou email").press("Tab")
    page.get_by_label("Senha").fill("@uama1252")
    page.get_by_role("button", name="Entrar", exact=True).click()
    page.get_by_label("Nova publicação").click()
    page.get_by_role("button", name="Selecionar do computador", exact=True).click()
    # ---------------------
    context.storage_state(path="state.json")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
