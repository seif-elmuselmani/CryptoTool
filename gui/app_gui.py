"""
Main GUI Application using CustomTkinter
"""
import customtkinter as ctk
from gui.components import *
import importlib
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


class CryptoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Cryptography Tool")
        self.geometry("1200x700")
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Cipher list
        self.ciphers = {
            "Caesar Cipher": "ciphers.caesar",
            "Monoalphabetic": "ciphers.monoalphabetic",
            "Playfair Cipher": "ciphers.playfair",
            "Vigenère Cipher": "ciphers.vigenere",
            "One-Time Pad": "ciphers.otp",
            "Hill Cipher": "ciphers.hill",
            "Row Transposition": "ciphers.row_transposition",
            "Permutation": "ciphers.permutation",
            "DES": "ciphers.des_cipher",
            "AES": "ciphers.aes_cipher"
        }
        
        self.current_cipher = None
        self.current_cipher_name = None
        
        # Create GUI layout
        self.create_layout()
        
        # Select first cipher by default
        first_cipher = list(self.ciphers.keys())[0]
        self.select_cipher(first_cipher)
    
    def create_layout(self):
        """Create the main layout with sidebar and content area"""
        # Configure grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create sidebar
        self.create_sidebar()
        
        # Create main content area
        self.create_content_area()
    
    def create_sidebar(self):
        """Create left sidebar with cipher selection"""
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.sidebar.grid_rowconfigure(len(self.ciphers) + 2, weight=1)
        
        # App title
        title = TitleLabel(self.sidebar, text="🔐 CryptoTool")
        title.grid(row=0, column=0, padx=20, pady=(30, 10))
        
        subtitle = ctk.CTkLabel(
            self.sidebar,
            text="Select a Cipher",
            font=("Roboto", 12),
            text_color="gray"
        )
        subtitle.grid(row=1, column=0, padx=20, pady=(0, 20))
        
        # Cipher buttons
        self.cipher_buttons = {}
        for idx, cipher_name in enumerate(self.ciphers.keys()):
            btn = CipherButton(
                self.sidebar,
                text=f"  {cipher_name}",
                command=lambda c=cipher_name: self.select_cipher(c)
            )
            btn.grid(row=idx + 2, column=0, padx=15, pady=5, sticky="ew")
            self.cipher_buttons[cipher_name] = btn
    
    def create_content_area(self):
        """Create main content area"""
        self.content = ctk.CTkFrame(self, corner_radius=0)
        self.content.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(4, weight=1)
        
        # Title
        self.cipher_title = TitleLabel(self.content, text="Select a Cipher")
        self.cipher_title.grid(row=0, column=0, padx=40, pady=(40, 30), sticky="w")
        
        # Text input section
        text_label = SectionLabel(self.content, text="Enter your text:")
        text_label.grid(row=1, column=0, padx=40, pady=(10, 5), sticky="w")
        
        self.text_input = StyledTextbox(self.content, height=120)
        self.text_input.grid(row=2, column=0, padx=40, pady=(0, 20), sticky="ew")
        
        # OTP-specific UI elements (initially hidden)
        self.otp_mode_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        self.otp_mode_frame.grid(row=3, column=0, padx=40, pady=(0, 10), sticky="ew")
        self.otp_mode_frame.grid_columnconfigure(1, weight=1)
        self.otp_mode_frame.grid_remove()  # Hidden by default
        
        otp_mode_label = ctk.CTkLabel(self.otp_mode_frame, text="Mode:", font=("Roboto Medium", 14))
        otp_mode_label.grid(row=0, column=0, padx=(0, 10), sticky="w")
        
        self.otp_mode_var = ctk.StringVar(value="letters")
        self.otp_mode_dropdown = ctk.CTkComboBox(
            self.otp_mode_frame,
            values=["Letters (A-Z)", "XOR (bytes)"],
            variable=self.otp_mode_var,
            width=150,
            command=self._on_otp_mode_change
        )
        self.otp_mode_dropdown.grid(row=0, column=1, sticky="w")
        
        # OTP format frame for XOR mode (initially hidden)
        self.otp_format_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        self.otp_format_frame.grid(row=4, column=0, padx=40, pady=(0, 10), sticky="ew")
        self.otp_format_frame.grid_remove()  # Hidden by default
        
        otp_format_label = ctk.CTkLabel(self.otp_format_frame, text="Output Format:", font=("Roboto Medium", 14))
        otp_format_label.grid(row=0, column=0, padx=(0, 10), sticky="w")
        
        self.otp_format_var = ctk.StringVar(value="hex")
        self.otp_format_radio_hex = ctk.CTkRadioButton(
            self.otp_format_frame,
            text="Hex",
            variable=self.otp_format_var,
            value="hex",
            font=("Roboto", 13)
        )
        self.otp_format_radio_hex.grid(row=0, column=1, padx=(0, 15), sticky="w")
        
        self.otp_format_radio_base64 = ctk.CTkRadioButton(
            self.otp_format_frame,
            text="Base64",
            variable=self.otp_format_var,
            value="base64",
            font=("Roboto", 13)
        )
        self.otp_format_radio_base64.grid(row=0, column=2, sticky="w")
        
        # Key input section
        self.key_label = SectionLabel(self.content, text="Enter your key:")
        self.key_label.grid(row=5, column=0, padx=40, pady=(10, 5), sticky="w")
        
        self.key_input = StyledEntry(self.content, placeholder_text="Enter encryption key")
        self.key_input.grid(row=6, column=0, padx=40, pady=(0, 10), sticky="ew")
        

        
        # Buttons frame
        button_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        button_frame.grid(row=8, column=0, padx=40, pady=10, sticky="ew")
        button_frame.grid_columnconfigure((0, 1), weight=1)
        
        self.encrypt_btn = ActionButton(
            button_frame,
            text="🔒 Encrypt",
            button_type="encrypt",
            command=self.perform_encrypt
        )
        self.encrypt_btn.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        
        self.decrypt_btn = ActionButton(
            button_frame,
            text="🔓 Decrypt",
            button_type="decrypt",
            command=self.perform_decrypt
        )
        self.decrypt_btn.grid(row=0, column=1, padx=(10, 0), sticky="ew")
        
        # Output section
        output_label = SectionLabel(self.content, text="Output:")
        output_label.grid(row=9, column=0, padx=40, pady=(20, 5), sticky="w")
        
        self.output_text = StyledTextbox(self.content, height=150)
        self.output_text.grid(row=10, column=0, padx=40, pady=(0, 30), sticky="ew")
    
    def select_cipher(self, cipher_name):
        """Select and load a cipher module"""
        # Update button states
        for name, btn in self.cipher_buttons.items():
            if name == cipher_name:
                btn.configure(fg_color=("gray75", "gray25"))
            else:
                btn.configure(fg_color="transparent")
        
        # Load cipher module
        try:
            module_name = self.ciphers[cipher_name]
            self.current_cipher = importlib.import_module(module_name)
            self.current_cipher_name = cipher_name
            
            # Update title
            self.cipher_title.configure(text=cipher_name)
            
            # Clear inputs and outputs
            self.text_input.delete("1.0", "end")
            self.key_input.delete(0, "end")
            self.output_text.delete("1.0", "end")
            
            # Handle OTP-specific UI
            if cipher_name == "One-Time Pad":
                self._show_otp_ui()
            else:
                self._hide_otp_ui()
            
            # Update key placeholder based on cipher
            self.update_key_placeholder(cipher_name)
            
        except Exception as e:
            self.show_error(f"Error loading cipher: {str(e)}")
    
    def _show_otp_ui(self):
        """Show OTP-specific UI elements"""
        self.otp_mode_frame.grid()
        self._on_otp_mode_change(self.otp_mode_var.get())
    
    def _hide_otp_ui(self):
        """Hide OTP-specific UI elements"""
        self.otp_mode_frame.grid_remove()
        self.otp_format_frame.grid_remove()
    
    def _on_otp_mode_change(self, mode):
        """Handle OTP mode change"""
        # Update key placeholder
        if mode == "Letters (A-Z)":
            self.key_input.configure(placeholder_text="Enter letters key (A-Z only)")
            self.otp_format_frame.grid_remove()
        else:  # XOR (bytes)
            self.key_input.configure(placeholder_text="Enter key (raw text, hex, or base64)")
            self.otp_format_frame.grid()
    

    
    def update_key_placeholder(self, cipher_name):
        """Update key input placeholder based on cipher type"""
        placeholders = {
            "Caesar Cipher": "Enter shift number (e.g., 3)",
            "Monoalphabetic": "Enter 26-letter substitution key",
            "Playfair Cipher": "Enter keyword",
            "Vigenère Cipher": "Enter keyword",
            "One-Time Pad": "Enter key (≥ text length)",
            "Hill Cipher": "Enter matrix (e.g., 6,24,1,13 for 2x2)",
            "Row Transposition": "Enter numeric key (e.g., 3142)",
            "Permutation": "Enter permutation (e.g., 3,1,4,2)",
            "DES": "Enter 8-byte key",
            "AES": "Enter encryption key"
        }
        
        placeholder = placeholders.get(cipher_name, "Enter encryption key")
        self.key_input.configure(placeholder_text=placeholder)
    
    def perform_encrypt(self):
        """Perform encryption"""
        if not self.current_cipher:
            self.show_error("Please select a cipher first")
            return
        
        text = self.text_input.get("1.0", "end-1c").strip()
        key = self.key_input.get().strip()
        
        if not text:
            self.show_error("Please enter text to encrypt")
            return
        
        if not key:
            self.show_error("Please enter a key")
            return
        
        # Handle OTP with special parameters
        if self.current_cipher_name == "One-Time Pad":
            try:
                mode = "letters" if self.otp_mode_var.get() == "Letters (A-Z)" else "xor"
                fmt = self.otp_format_var.get() if mode == "xor" else "hex"  # fmt not used for letters mode
                
                result = self.current_cipher.encrypt(text, key, mode=mode, fmt=fmt)
                self.output_text.delete("1.0", "end")
                self.output_text.insert("1.0", result)
            except Exception as e:
                self.show_error(f"Encryption error: {str(e)}")
        else:
            # Standard encryption for other ciphers
            try:
                result = self.current_cipher.encrypt(text, key)
                self.output_text.delete("1.0", "end")
                self.output_text.insert("1.0", result)
            except Exception as e:
                self.show_error(f"Encryption error: {str(e)}")
    
    def perform_decrypt(self):
        """Perform decryption"""
        if not self.current_cipher:
            self.show_error("Please select a cipher first")
            return
        
        text = self.text_input.get("1.0", "end-1c").strip()
        key = self.key_input.get().strip()
        
        if not text:
            self.show_error("Please enter text to decrypt")
            return
        
        if not key:
            self.show_error("Please enter a key")
            return
        
        # Handle OTP with special parameters
        if self.current_cipher_name == "One-Time Pad":
            try:
                mode = "letters" if self.otp_mode_var.get() == "Letters (A-Z)" else "xor"
                fmt = self.otp_format_var.get() if mode == "xor" else "hex"  # fmt not used for letters mode
                
                result = self.current_cipher.decrypt(text, key, mode=mode, fmt=fmt)
                self.output_text.delete("1.0", "end")
                self.output_text.insert("1.0", result)
            except Exception as e:
                self.show_error(f"Decryption error: {str(e)}")
        else:
            # Standard decryption for other ciphers
            try:
                result = self.current_cipher.decrypt(text, key)
                self.output_text.delete("1.0", "end")
                self.output_text.insert("1.0", result)
            except Exception as e:
                self.show_error(f"Decryption error: {str(e)}")

    def show_error(self, message):
        """Show error message in output"""
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", f"❌ Error: {message}")
    
    def show_success(self, message):
        """Show success message in output"""
        current = self.output_text.get("1.0", "end-1c")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", f"✅ {message}\n\n{current}")


def run_app():
    """Run the application"""
    app = CryptoApp()
    app.mainloop()
