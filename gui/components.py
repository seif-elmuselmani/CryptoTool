"""
Custom components and helper widgets for the GUI
"""
import customtkinter as ctk

class CipherButton(ctk.CTkButton):
    """Styled button for cipher selection"""
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            height=40,
            corner_radius=8,
            font=("Roboto", 13),
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            **kwargs
        )


class ActionButton(ctk.CTkButton):
    """Styled button for encrypt/decrypt actions"""
    def __init__(self, master, button_type="encrypt", **kwargs):
        if button_type == "encrypt":
            fg_color = ("#2ecc71", "#27ae60")
            hover_color = ("#27ae60", "#229954")
        else:  # decrypt
            fg_color = ("#3498db", "#2980b9")
            hover_color = ("#2980b9", "#1f618d")
        
        super().__init__(
            master,
            height=45,
            corner_radius=10,
            font=("Roboto Medium", 14),
            fg_color=fg_color,
            hover_color=hover_color,
            **kwargs
        )


class StyledEntry(ctk.CTkEntry):
    """Styled entry widget"""
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            height=40,
            corner_radius=8,
            border_width=2,
            font=("Roboto", 13),
            **kwargs
        )


class StyledTextbox(ctk.CTkTextbox):
    """Styled textbox widget"""
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            corner_radius=8,
            border_width=2,
            font=("Consolas", 12),
            wrap="word",
            **kwargs
        )


class SectionLabel(ctk.CTkLabel):
    """Styled label for sections"""
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            font=("Roboto Medium", 14),
            **kwargs
        )


class TitleLabel(ctk.CTkLabel):
    """Styled label for titles"""
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            font=("Roboto Bold", 24),
            **kwargs
        )
