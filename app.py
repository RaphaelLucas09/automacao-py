from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.instagram.com/accounts/login/")
    page.get_by_label("Telefone, nome de usuário ou email").click()
    page.get_by_label("Telefone, nome de usuário ou email").fill(
        "fael9591@gmail.com")
    page.get_by_label("Telefone, nome de usuário ou email").press("Tab")
    page.get_by_label("Senha").fill("@uama1252")
    page.get_by_role("button", name="Entrar", exact=True).click()
    page.get_by_role("button", name="Agora não").click()
    page.get_by_role("button", name="Agora não").click()
    page.get_by_role("link", name="Nova publicação Criar").click()
    page.get_by_role("button", name="Selecionar do computador",
                     exact=True).click()
    page.get_by_role("button", name="alibaba").click()
    # ---------------------
    context.storage_state(path="state.json")
    
    x = 0
    for x in range(10):
        return x
    if x == 10:
        context.close()
        browser.close()


with sync_playwright() as playwright:
    run(playwright)
