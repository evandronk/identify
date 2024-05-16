import flet as ft
import key
import binary_key
import new_ident


def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(route):
        page.views.clear()
        binary_class = key.MatrizOrdemHexapoda()
        print(binary_class.matriztexto)
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(title=ft.Text("Flet app"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Visit Store", on_click=lambda _: page.go("/store")),
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                new_ident.main(page, binary_class)
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
