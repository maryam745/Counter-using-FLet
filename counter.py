import flet as ft

def main(page: ft.Page):
    page.title = "Advanced Counter App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Load previous value (if any)
    saved_value = page.client_storage.get("counter_value")
    counter_value = int(saved_value) if saved_value else 0

    # UI Elements
    counter = ft.Text(value=str(counter_value), size=40, weight=ft.FontWeight.BOLD)
    theme_icon = ft.IconButton(icon=ft.Icons.DARK_MODE, tooltip="Switch Theme")

    # Function to update and save counter
    def update_counter(new_value):
        counter.value = str(new_value)
        page.client_storage.set("counter_value", new_value)
        page.update()

    # Button functions
    def increment(e):
        value = int(counter.value)
        if value < 10:
            update_counter(value + 1)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("🚫 Max limit reached (10)!"))
            page.snack_bar.open = True
            page.update()

    def decrement(e):
        value = int(counter.value)
        if value > 0:
            update_counter(value - 1)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Minimum limit reached (0)!"))
            page.snack_bar.open = True
            page.update()

    def reset(e):
        def confirm_reset(e):
            update_counter(0)
            page.dialog.open = False
            page.update()

        def cancel_reset(e):
            page.dialog.open = False
            page.update()

        page.dialog = ft.AlertDialog(
            title=ft.Text("Reset Counter?"),
            content=ft.Text("Are you sure you want to reset the counter to zero?"),
            actions=[
                ft.TextButton("Yes", on_click=confirm_reset),
                ft.TextButton("No", on_click=cancel_reset)
            ],
        )
        page.dialog.open = True
        page.update()

    # Theme toggle
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_icon.icon = ft.Icons.LIGHT_MODE
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_icon.icon = ft.Icons.DARK_MODE
        page.update()

    theme_icon.on_click = toggle_theme

    # Layout
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("🔥 Counter App", size=28, weight=ft.FontWeight.BOLD),
                        theme_icon
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                counter,
                ft.Row(
                    [
                        ft.ElevatedButton("➕ Increment", on_click=increment),
                        ft.ElevatedButton("➖ Decrement", on_click=decrement),
                        ft.ElevatedButton("🔄 Reset", on_click=reset),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Text(
                    "💾 Count is automatically saved locally",
                    size=12,
                    italic=True,
                    color=ft.Colors.GREY,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.app(target=main)
