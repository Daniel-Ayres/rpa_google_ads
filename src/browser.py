"""

  Inicializa e configura o navegador Chrome de forma automatizada.

    - Abre o navegador maximizado.
    - Bloqueia pop-ups e notificações.
    - Define tempo máximo de carregamento de página (40s).
    - Usa o 'undetected_chromedriver' para evitar bloqueios automáticos do Google.

    Retorna:
        driver (uc.Chrome): instância do navegador pronta para uso.

"""

import undetected_chromedriver as uc

def iniciar_navegador():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    driver = uc.Chrome(options=options)
    driver.set_page_load_timeout(40)
    return driver
