import pygame
import pygame_gui
import time
import numpy as np
from progowanie import run_prog
from przejscia import przejscia, opady, tornado, obniz_teren, zwroc_stan, tama


def dostosuj_opady(text):
    d_opady = {
        'Lekkie opady': 2,
        'Średnie opady': 10,
        'Ulewa': 100
    }
    return d_opady[text]

def rysuj_mape(scene, mapa_progowana, c_size):
    colors = {
        0: (0, 0 ,255),
        1: (0, 255, 0),
        2: (255, 255, 0),
        3: (255, 0, 0),
        4: (128, 128, 128),
        5: (51, 255, 255),
        6: (80, 40, 40)
    }

    for y in range(mapa_progowana.shape[0]):
        for x in range(mapa_progowana.shape[1]):
            stan_pixela = mapa_progowana[y,x]
            kolor = colors[stan_pixela]
            rt = pygame.Rect(x * c_size, y * c_size, c_size, c_size)
            pygame.draw.rect(scene, kolor, rt)

def main():
    counter = 0
    mapa_progowana = run_prog()

    c_size = 4
    pygame.init()
    scene = pygame.display.set_mode((mapa_progowana.shape[1] * c_size + 200, mapa_progowana.shape[0] * c_size))
    pygame.display.set_caption('Symulacja powodzi')

    p_gui = pygame_gui.UIManager((mapa_progowana.shape[1]*c_size + 200, mapa_progowana.shape[0]*c_size))

    start_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(mapa_progowana.shape[1] * c_size + 10, 10, 180, 30),
        text='Uruchom/zatrzymaj',
        manager=p_gui
    )

    lista1_opt = ['Brak opadów', 'Lekkie opady', 'Średnie opady', 'Ulewa']
    lista1 = pygame_gui.elements.UIDropDownMenu(
        lista1_opt,
        lista1_opt[0],
        pygame.Rect(mapa_progowana.shape[1] * c_size + 10, 50, 180, 30),
        manager=p_gui,
        expand_on_option_click=False)
    moc_opadow = 'Brak opadów'

    tornado_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(mapa_progowana.shape[1] * c_size + 10, 90, 180, 30),
        text='Podtopienie',
        manager=p_gui
    )

    obniz_teren_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(mapa_progowana.shape[1] * c_size + 10, 130, 180, 30),
        text='Obniż teren',
        manager=p_gui
    )

    tama_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(mapa_progowana.shape[1] * c_size + 10, 170, 180, 30),
        text='Tama',
        manager=p_gui
    )

    rysuj_mape(scene, mapa_progowana, c_size)

    pygame.display.flip()

    clock = pygame.time.Clock()

    tama_check = False
    obniz_teren_check = False
    tornado_check = False
    simulation = False
    run = True
    while run:
        delt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            p_gui.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    simulation = not simulation
                elif event.ui_element == tornado_button:
                    tornado_check = True
                    obniz_teren_check = False
                    tama_check = False
                elif event.ui_element == obniz_teren_button:
                    obniz_teren_check = True
                    tornado_check = False
                    tama_check = False
                elif event.ui_element == tama_button:
                    tama_check = True
                    tornado_check = False
                    obniz_teren_check = False

            if event.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                if event.ui_element == lista1:
                    moc_opadow = event.text

            if event.type == pygame.MOUSEBUTTONDOWN and tornado_check:
                m_x, m_y = event.pos
                if m_x < mapa_progowana.shape[1] * c_size and m_y < mapa_progowana.shape[0] * c_size:
                    x = m_x // c_size
                    y = m_y // c_size
                    mapa_progowana = tornado(mapa_progowana, y, x)
                    tornado_check = True

            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] and tornado_check:
                m_x, m_y = event.pos
                if m_x < mapa_progowana.shape[1] * c_size and m_y < mapa_progowana.shape[0] * c_size:
                    x = m_x // c_size
                    y = m_y // c_size
                    mapa_progowana = tornado(mapa_progowana, y, x)

            if event.type == pygame.MOUSEBUTTONDOWN and obniz_teren_check:
                m_x, m_y = event.pos
                if m_x < mapa_progowana.shape[1] * c_size and m_y < mapa_progowana.shape[0] * c_size:
                    x = m_x // c_size
                    y = m_y // c_size
                    obnizenie = zwroc_stan(mapa_progowana, y, x)
                    mapa_progowana = obniz_teren(mapa_progowana, obnizenie, y, x)
                    obniz_teren_check = True

            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] and obniz_teren_check:
                m_x, m_y = event.pos
                if m_x < mapa_progowana.shape[1] * c_size and m_y < mapa_progowana.shape[0] * c_size:
                    x = m_x // c_size
                    y = m_y // c_size
                    mapa_progowana = obniz_teren(mapa_progowana, obnizenie, y, x)

            if event.type == pygame.MOUSEBUTTONDOWN and tama_check:
                m_x, m_y = event.pos
                if m_x < mapa_progowana.shape[1] * c_size and m_y < mapa_progowana.shape[0] * c_size:
                    x = m_x // c_size
                    y = m_y // c_size
                    mapa_progowana = tama(mapa_progowana, y, x)
                    tama_check = True

            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] and tama_check:
                m_x, m_y = event.pos
                if m_x < mapa_progowana.shape[1] * c_size and m_y < mapa_progowana.shape[0] * c_size:
                    x = m_x // c_size
                    y = m_y // c_size
                    mapa_progowana = tama(mapa_progowana, y, x)


        if simulation:
            if moc_opadow != 'Brak opadów':
                mapa_progowana = opady(mapa_progowana, dostosuj_opady(moc_opadow))
            counter += 1
            mapa_progowana = przejscia(mapa_progowana, counter)


        scene.fill((0, 0, 0), pygame.Rect(mapa_progowana.shape[1] * c_size, 0, 200, mapa_progowana.shape[0] * c_size))
        rysuj_mape(scene, mapa_progowana, c_size)


        p_gui.update(delt)
        p_gui.draw_ui(scene)

        pygame.display.update()
        #pygame.time.wait(3000)


    pygame.quit()


main()

