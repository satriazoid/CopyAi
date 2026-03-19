import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import re

app = ttk.Window(themename="darkly")
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


# ================= LAYOUT =================
app.columnconfigure(0, weight=1)
app.rowconfigure(1, weight=1)

# HEADER
header = ttk.Label(
    app,
    text="CopyAI Text Cleaner",
    font=("Segoe UI", 20, "bold")
)
header.pack(pady=15)

# MAIN FRAME
main_frame = ttk.Frame(app, padding=20)
main_frame.pack(fill=BOTH, expand=True)

main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(1, weight=1)

# LABEL
ttk.Label(
    main_frame,
    text="Input Text",
    font=("Segoe UI", 11, "bold")
).grid(row=0, column=0, sticky="w", pady=(0, 5))

ttk.Label(
    main_frame,
    text="Clean Result",
    font=("Segoe UI", 11, "bold")
).grid(row=0, column=1, sticky="w", pady=(0, 5))

# INPUT BOX + SCROLL
input_frame = ttk.Frame(main_frame)
input_frame.grid(row=1, column=0, sticky="nsew", padx=(0, 10))

input_box = ttk.Text(input_frame, wrap="word")
input_box.pack(side=LEFT, fill=BOTH, expand=True)

scroll_input = ttk.Scrollbar(input_frame, command=input_box.yview)
scroll_input.pack(side=RIGHT, fill=Y)
input_box.config(yscrollcommand=scroll_input.set)

# OUTPUT BOX + SCROLL
output_frame = ttk.Frame(main_frame)
output_frame.grid(row=1, column=1, sticky="nsew")

output_box = ttk.Text(output_frame, wrap="word")
output_box.pack(side=LEFT, fill=BOTH, expand=True)

scroll_output = ttk.Scrollbar(output_frame, command=output_box.yview)
scroll_output.pack(side=RIGHT, fill=Y)
output_box.config(yscrollcommand=scroll_output.set)

# BUTTON SECTION
button_frame = ttk.Frame(app)
button_frame.pack(pady=15)

clean_button = ttk.Button(
    button_frame,
    text="Clean Text",
    bootstyle="primary",
    width=20,
    command=clean_text
)
clean_button.pack(side=LEFT, padx=10)

copy_button = ttk.Button(
    button_frame,
    text="Copy Result",
    bootstyle="success",
    width=20,
    command=copy_text
)
copy_button.pack(side=LEFT, padx=10)

app.mainloop()