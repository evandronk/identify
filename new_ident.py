import flet as ft
import key


def main(page, binary_class):
    page.views.clear()
    first_btn = ft.ElevatedButton(text=binary_class.matrizij,
                                  on_click=lambda _: __first_btn__(False, first_btn, second_btn, binary_class))
    second_btn = ft.ElevatedButton(text=binary_class.matrizik,
                                   on_click=lambda _: __second_btn__(False, first_btn, second_btn, binary_class))
    back_btn = ft.ElevatedButton(text="Voltar",
                                 on_click=lambda _: __btn_back__(False, first_btn, second_btn, binary_class, page))
    identification_view = ft.View(
        "/store",
        [
            ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
            # ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
            first_btn,
            second_btn,
            back_btn
        ],
    )
    page.update()
    return identification_view


def __first_btn__(classificou, first_btn, second_btn, binary_class):
    if not classificou:
        binary_class.i = binary_class.i + 1
        binary_class.k = 2 * binary_class.j + 1
        binary_class.j = 2 * binary_class.j
        key.__update_text(binary_class)
        first_btn.text = binary_class.matrizij
        second_btn.text = binary_class.matrizik
        first_btn.update()
        second_btn.update()


def __second_btn__(classificou, first_btn, second_btn, binary_class):
    if not classificou:
        binary_class.i = binary_class.i + 1
        binary_class.j = 2 * binary_class.k
        binary_class.k = 2 * binary_class.k + 1
        key.__update_text(binary_class)
        first_btn.text = binary_class.matrizij
        second_btn.text = binary_class.matrizik
        first_btn.update()
        second_btn.update()


def __btn_back__(classificou, first_btn, second_btn, binary_class, page):
  return 0