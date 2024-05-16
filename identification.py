import flet as ft
import binary_key as binary


def main(page, binary_class):
    page.views.clear()
    first_btn = ft.ElevatedButton(text=binary.__get_text__(0, 0),
                                  on_click=lambda _: __first_btn__(first_btn, second_btn, binary_class))
    second_btn = ft.ElevatedButton(text=binary.__get_text__(0, 1),
                                   on_click=lambda _: __second_btn__(first_btn, second_btn, binary_class))
    back_btn = ft.ElevatedButton(text="Voltar",
                                   on_click=lambda _: __btn_back__(first_btn, second_btn, binary_class, page))
    identification_view = ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        #ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                        first_btn,
                        second_btn,
                        back_btn
                    ],
                )
    page.update()
    return identification_view


def __first_btn__(btn1, btn2, binary_class):
    if not binary_class.identified:
        binary_class.prev_i = binary_class.index_i
        binary_class.prev_j = binary_class.index_j

        binary_class.index_i = binary_class.index_i + 1
        binary_class.index_j = 2 * binary_class.index_j

        i = binary_class.index_i
        j = binary_class.index_j
        print("i " + str(i))
        print("j " + str(j))
        btn1.text = binary.__get_text__(i, j)
        btn2.text = binary.__get_text__(i, j + 1)
        if binary.__get_text__(i, j + 1) == "classificou":
            btn2.visible = False
            binary_class.identified = True
        btn1.update()
        btn2.update()

    else:
        print("Identificado")


def __second_btn__(btn1, btn2, binary_class):

    if not binary_class.identified:
        binary_class.prev_i = binary_class.index_i
        binary_class.prev_j = binary_class.index_j

        binary_class.index_j = 2*binary_class.index_j2
        binary_class.index_i = binary_class.index_i + 1
        binary_class.index_j2 = binary_class.index_j + 1

        i = binary_class.index_i
        j1 = binary_class.index_j
        j2 = binary_class.index_j2
        print("i " + str(i))
        print("j " + str(j1))
        btn1.text = binary.__get_text__(i, j1)
        btn2.text = binary.__get_text__(i, j2)
        if binary.__get_text__(i, j2) == "classificou":
            btn2.visible = False
            binary_class.identified = True
        btn1.update()
        btn2.update()

    else:
        print("Identificado")


def __btn_back__(btn1, btn2, binary_class, page):
    if binary_class.index_i == 0:
        page.go("/")
    else:
        binary_class.index_i = binary_class.prev_i
        binary_class.index_j = binary_class.prev_j
        binary_class.index_j2 = binary_class.index_j + 1
        binary_class.prev_i = binary_class.prev_i - 1
        binary_class.prev_j = int(binary_class.prev_j/2)
        i = binary_class.index_i
        j = binary_class.index_j
        j2 = binary_class.index_j2
        btn1.text = binary.__get_text__(i, j)
        btn2.text = binary.__get_text__(i, j2)
        btn2.visible = True
        binary_class.identified = False
        btn1.update()
        btn2.update()

