# lobo_steam.py
import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    def submit(self, form_data):
        return rx.toast(form_data)

def navbar() -> rx.Component:
    """Create a navigation bar."""
    return rx.hstack(
        rx.link("Home", href="#"),
        rx.link("About Us", href="#about-us",),
        rx.link("Services", href="#services",),
        spacing="4",
        margin="4",
    )

def about_us() -> rx.Component:
    """Create About Us section."""
    return rx.container(
        rx.heading("About Us", size="7"),
        rx.text("At Lobo-STEAM, we are dedicated to promoting STEAM education through engaging activities and resources."),
        margin="4",
    )

def services() -> rx.Component:
    """Create Services section."""
    return rx.container(
        rx.heading("Our Services", size="7"),
        rx.text("We offer a variety of services, including:"),
        rx.unordered_list(
            [
                rx.list_item("Workshops"),
                rx.list_item("Mentorship Programs"),
                rx.list_item("Online Resources"),
                rx.list_item("Community Events"),
            ]
        ),
        margin="4",
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        navbar(),  # Add the navigation bar


        rx.vstack(
            rx.heading("Lobo-STEAM!", size="9"),
            rx.text(
                "Tu inicio al mundo STEAM",
                # rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),

            rx.link(
                rx.button("Contactanos!"),
                href="https://www.instagram.com/lobo_steam/",
                is_external=True,
            ),
            
            rx.card(
                rx.form(
                    rx.hstack(
                        # rx.image(src="/envelope.png"),
                        rx.vstack(
                            rx.heading("Send us a message"),
                            rx.text(
                                "Fill the form and we’ll back to you shortly.",
                            ),
                        ),
                    ),
                    rx.vstack(
                        rx.text(
                            "Name ",
                            rx.text.span("*", color="red"),
                        ),
                        rx.input(
                            name="name",
                            required=True,
                        ),
                    ),
                    rx.vstack(
                        rx.text(
                            "Email ",
                            rx.text.span("*", color="red"),
                        ),
                        rx.input(
                            name="email",
                            type="email",
                            required=True,
                        ),
                    ),
                    rx.vstack(
                        rx.text("Message"),
                        rx.text_area(
                            name="message",
                        ),
                    ),
                    rx.button("Send", type="submit"),
                    on_submit=State.submit,
                ),
            ),
          

            spacing="5",
            justify="center",
            min_height="85vh",
        ),

        # About Us and Services sections
        about_us(),
        
        services(),

    )


app = rx.App()
app.add_page(index)
