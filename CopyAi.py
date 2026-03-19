import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import re

# default theme (light)
current_theme = "flatly"

app = ttk.Window(themename=current_theme)
app.title("CopyAI - Text Cleaner")
app.geometry("1000x600")


# ================= FUNCTION =================
def clean_text():
    text = input_box.get("1.0", END)

    text = re.sub(r'[-–—]', ' ', text)
    text = re.sub(r'[•*#]', '', text)
    text = re.sub(r'\s+([,.!?])', r'\1', text)
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    text = text.strip()

    output_box.delete("1.0", END)
    output_box.insert(END, text)


def copy_text():
    result = output_box.get("1.0", END)
    app.clipboard_clear()
    app.clipboard_append(result)


def toggle_theme():
    global current_theme

    if current_theme == "flatly":
        current_theme = "darkly"
        theme_btn.config(text="☀️ Light Mode")
    else:
        current_theme = "flatly"
        theme_btn.config(text="🌙 Dark Mode")

    app.style.theme_use(current_theme)


# ================= LAYOUT =================
app.columnconfigure(0, weight=1)
app.rowconfigure(1, weight=1)

# HEADER
header_frame = ttk.Frame(app)
header_frame.pack(fill=X, padx=20, pady=10)

title = ttk.Label(
    header_frame,
    text="CopyAI Text Cleaner",
    font=("Segoe UI", 18, "bold")
)
title.pack(side=LEFT)

# THEME BUTTON (kanan atas)
theme_btn = ttk.Button(
    header_frame,
    text="🌙 Dark Mode",
    bootstyle="outline-secondary",
    command=toggle_theme
)
theme_btn.pack(side=RIGHT)

# MAIN FRAME (card feel)
main_frame = ttk.Frame(app, padding=20, bootstyle="light")
main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(1, weight=1)

# LABEL
ttk.Label(
    main_frame,
    text="Input Text",
    font=("Segoe UI", 10, "bold")
).grid(row=0, column=0, sticky="w", pady=(0, 5))

ttk.Label(
    main_frame,
    text="Clean Result",
    font=("Segoe UI", 10, "bold")
).grid(row=0, column=1, sticky="w", pady=(0, 5))

# INPUT BOX
input_frame = ttk.Frame(main_frame)
input_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 10))

input_box = ttk.Text(
    input_frame,
    wrap="word",
    font=("Segoe UI", 10),
    relief="flat",
    borderwidth=8
)
input_box.pack(fill=BOTH, expand=True)

# OUTPUT BOX
output_frame = ttk.Frame(main_frame)
output_frame.grid(row=1, column=1, sticky="nsew")

output_box = ttk.Text(
    output_frame,
    wrap="word",
    font=("Segoe UI", 10),
    relief="flat",
    borderwidth=8
)
output_box.pack(fill=BOTH, expand=True)

# BUTTON FRAME (KANAN)
button_frame = ttk.Frame(app)
button_frame.pack(fill=X, padx=20, pady=10)

inner_btn_frame = ttk.Frame(button_frame)
inner_btn_frame.pack(side=RIGHT)

# BUTTON CLEAN (rounded feel via padding + style)
clean_button = ttk.Button(
    inner_btn_frame,
    text="Clean Text",
    bootstyle="primary",
    width=15,
    command=clean_text
)
clean_button.pack(side=LEFT, padx=5)

# BUTTON COPY
copy_button = ttk.Button(
    inner_btn_frame,
    text="Copy",
    bootstyle="success",
    width=15,
    command=copy_text
)
copy_button.pack(side=LEFT, padx=5)

app.mainloop()