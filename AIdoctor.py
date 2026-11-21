#ttk is the more mordern version of tkinter. Just using tkinter will give you the older version of tkinter
import tkinter as tk
from tkinter import ttk, messagebox
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

training_texts = [
    "sneezing and runny nose",
    "cough and stuffy nose",
    "sore throat and runny nose",
    "coughing with blocked nose",
    "sneezing with watery nose",
 
    "itchy eyes and sneezing",
    "itchy nose and watery eyes",
    "sneezing around dust",
    "itchy skin after pollen exposure",
    "watery eyes and itchy nose",
 
    "stomach ache after eating",
    "feeling bloated after lunch",
    "upset stomach and nausea",
    "stomach feels uncomfortable",
    "feeling sick after a meal",
 
    "feeling tired and weak",
    "body feels uncomfortable",
    "feeling generally unwell",
    "mild body discomfort",
    "feeling unwell and tired",
 
    "feeling sleepy during the day",
    "tired after staying up late",
    "yawning and feeling sleepy",
    "not enough sleep last night",
    "feeling tired after little sleep"
]
 
training_labels = [
    "Cold-like Pattern",
    "Cold-like Pattern",
    "Cold-like Pattern",
    "Cold-like Pattern",
    "Cold-like Pattern",
 
    "Allergy-like Pattern",
    "Allergy-like Pattern",
    "Allergy-like Pattern",
    "Allergy-like Pattern",
    "Allergy-like Pattern",
 
    "Digestive Discomfort",
    "Digestive Discomfort",
    "Digestive Discomfort",
    "Digestive Discomfort",
    "Digestive Discomfort",
 
    "General Discomfort",
    "General Discomfort",
    "General Discomfort",
    "General Discomfort",
    "General Discomfort",
 
    "Sleep-related Tiredness",
    "Sleep-related Tiredness",
    "Sleep-related Tiredness",
    "Sleep-related Tiredness",
    "Sleep-related Tiredness"
]

#convert text into numbers
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(training_texts)

#create and train the model
model = MultinomialNB()
model.fit(X_train, training_labels)

#create the application window
root = tk.Tk()
root.title("AI Doctor | Supervised Learning Lab")
root.geometry("1000x760")
root.minsize(780, 620)
root.configure(bg="#F1F5F9")

#colors
NAVY = "#123B5D"
TEAL = "#0F766E"
BACKGROUND = "#F1F5F9"
WHITE = "#FFFFFF"
TEXT = "#243447"
MUTED = "#64748B"
BLUE_LIGHT = "#DBEAFE"

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TNotebook",
    background=BACKGROUND,
    borderwidth=0
)

style.configure(
    "TNotebook.Tab",
    padding=(18, 12),
    font=("Arial", 11, "bold")
)

style.configure(
    "Treeview",
    font=("Arial", 10),
    rowheight=30,
    background=WHITE,
    fieldbackground=WHITE
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 10, "bold")
)

def load_sample(text):
    """Load a sample description into the input box."""
    symptom_box.delete("1.0", tk.END)
    symptom_box.insert(tk.END, text)

    result_title.config(
        text="Ready to analyze",
        fg=TEAL
    )

    result_details.config(
        text="Click Analyze Text to see the model's prediction."
    )

def analyze_text():
    """Predict a category using the trained model."""

    user_text = symptom_box.get("1.0", tk.END).strip()

    if not user_text:
        messagebox.showwarning(
            "Input Required",
            "Please enter a description or choose a sample."
        )
        return

    new_features = vectorizer.transform([user_text])

    prediction = model.predict(new_features)[0]

    probabilities = model.predict_proba(new_features)[0]

    prediction_index = list(model.classes_).index(prediction)
    estimated_score = probabilities[prediction_index] * 100

    result_title.config(
        text=(
            f"Model-estimated probability: {estimated_score:.1f}%\n\n"
            "Why this result? The model compares the words in your "
            "description with patterns learned from its training examples.\n\n"
            "Important: This score is not medical accuracy. The model "
            "uses a small educational dataset and may make mistakes."
        )
    )

def clear_input():
    """Clear the input and prediction."""
    symptom_box.delete("1.0", tk.END)

    result_title.config(
        text="Your prediction will appear here",
        fg=TEXT
    )

    result_details.config(
        text="Enter a description and click Analyze Text."
    )

header = tk.Frame(root, bg=NAVY, height=115)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="🤖 AI Doctor",
    font=("Arial", 27, "bold"),
    bg=NAVY,
    fg=WHITE
).pack(pady=(17, 4))

tk.Label(
    header,
    text="Supervised Learning Lab | Lesson 13 | Grade 5-6",
    font=("Arial", 12),
    bg=NAVY,
    fg="#D8EAFE"
).pack()

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=20, pady=18)

analyzer_tab = tk.Frame(notebook, bg=BACKGROUND)
dataset_tab = tk.Frame(notebook, bg=BACKGROUND)
learning_tab = tk.Frame(notebook, bg=BACKGROUND)

notebook.add(analyzer_tab, text="AI Analyze")
notebook.add(dataset_tab, text="Training Dataset")
notebook.add(learning_tab, text="How AI Learns")

#1st tab - AI analyzer
tk.Label(
    analyzer_tab,
    text="Let's explore how AI learns!",
    font=("Arial", 18, "bold"),
    bg=BACKGROUND,
    fg=NAVY
).pack(anchor="w", padx=18, pady=(15, 4))

tk.Label(
    analyzer_tab, text=(
        "Enter an example description or choose a sample below."
        "The trained model will predict an educational category."
    ),
    font=("Arial", 10),
    bg=BACKGROUND,
    fg=MUTED,
    wraplength=850,
    justify="left"
).pack(anchor="w", padx=18, pady=(0, 12))

input_card = tk.Frame(
    analyzer_tab,
    bg=WHITE,
    highlightbackground="#D7E4F0",
    highlightthickness=1
)
input_card.pack(fill="x", padx=18, pady=4)

tk.Label(
    input_card, text="Describe the example:",
    font=("Arial", 11, "bold"),
    bg=WHITE,
    fg=NAVY
).pack(anchor="w", padx=14, pady=(12, 6))

symptom_box = tk.Text(
    input_card,
    height=3,
    font=("Arial", 12),
    wrap="word",
    relief="solid",
    bd=1,
    padx=10,
    pady=8
)
symptom_box.pack(fill="x", padx=14, pady=(0, 12))

tk.Label(
    analyzer_tab,
    text="Try a sample:",
    font=("Arial", 10, "bold"),
    bg=BACKGROUND,
    fg=TEXT
).pack(anchor="w", padx=18, pady=(10, 4))

sample_frame = tk.Frame(analyzer_tab, bg=BACKGROUND)
sample_frame.pack(fill="x", padx=18)

samples = [
     "sneezing and runny nose",
    "itchy eyes and sneezing",
    "stomach ache after eating",
    "feeling tired and weak",
    "sleepy after staying up late"
]

for sample in samples:
    tk.Button(
        sample_frame,
        text=sample,
        font=("Arial", 9),
        bg=BLUE_LIGHT,
        fg="#1E3A8A",
        activebackground="#BFDBFE",
        relief="flat",
        padx=8,
        pady=7,
        cursor="hand2",
        command=lambda s=sample: load_sample(s)
    ).pack(side="left", padx=(0, 5), pady=4)

button_frame = tk.Frame(analyzer_tab, bg=BACKGROUND)
button_frame.pack(fill="x", padx=18, pady=12)

tk.Button(
    button_frame,
    text="Analyze Text",
    font=("Arial", 11, "bold"),
    bg=TEAL,
    fg=WHITE,
    activebackground="#115E59",
    activeforeground=WHITE,
    relief="flat",
    padx=24,
    pady=10,
    cursor="hand2",
    command=analyze_text
).pack(side="left", padx=(0, 10))

tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 11, "bold"),
    bg="#E2E8F0",
    fg=TEXT,
    relief="flat",
    padx=24,
    pady=10,
    cursor="hand2",
    command=clear_input
).pack(side="left")

result_card = tk.Frame(
    analyzer_tab,
    bg=WHITE,
    highlightbackground="#B9D7E9",
    highlightthickness=1
)
result_card.pack(fill="x", padx=18, pady=(0, 12))

tk.Label(
    result_card,
    text="AI MODEL OUTPUT",
    font=("Arial", 10, "bold"),
    bg=WHITE,
    fg=MUTED
).pack(anchor="w", padx=14, pady=(12, 5))

result_title = tk.Label(
    result_card,
    text="Your prediction will appear here",
    font=("Arial", 17, "bold"),
    bg=WHITE,
    fg=TEXT,
    wraplength=850,
    justify="left"
)
result_title.pack(anchor="w", padx=14, pady=5)

result_details = tk.Label(
    result_card,
    text="Enter a description and click Analyze Text.",
    font=("Arial", 10),
    bg=WHITE,
    fg=TEXT,
    wraplength=850,
    justify="left"
)
result_details.pack(anchor="w", padx=14, pady=(0, 12))

tk.Label(
    analyzer_tab,
    text=(
        "EDUCATIONAL DEMO ONLY: This application cannot diagnose "
        "illnesses. Predictions may be incorrect. Discuss real health "
        "concerns with a trusted adult or healthcare professional."
    ),
    font=("Arial", 9, "bold"),
    bg="#FFF7ED",
    fg="#9A3412",
    wraplength=850,
    justify="left",
    padx=12,
    pady=10
).pack(fill="x", padx=18, pady=(0, 10))


#2nd tab - training dataset
tk.Label(
    dataset_tab,
    text="Explore the Training Dataset",
    font=("Arial", 17, "bold"),
    bg=BACKGROUND,
    fg=NAVY
).pack(anchor="w", padx=18, pady=(18, 5))

tk.Label(
    dataset_tab,
    text=("Each row contains an example input and its known label. "
          "The model learns patterns from these labeled examples."
    ),
    font=("Arial", 10),
    bg=BACKGROUND,
    fg=MUTED,
    wraplength=850,
    justify="left"
).pack(anchor="w", padx=18, pady=(0, 12))

table_frame = tk.Frame(dataset_tab, bg=BACKGROUND)
table_frame.pack(fill="both", expand=True, padx=18, pady=(0, 18))

columns = ("number", "example", "label")

dataset_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
)

dataset_table.heading("number", text="No.")
dataset_table.heading("example", text="Training Example / Input")
dataset_table.heading("label", text="Known Label / Category")

dataset_table.column("number", width=55, anchor="center")
dataset_table.column("example", width=300)
dataset_table.column("label", width=300)

scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=dataset_table.yview
)

dataset_table.configure(yscrollcommand=scrollbar.set)

dataset_table.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

for index, (example,label) in enumerate(
    zip(training_texts, training_labels), 
    start=1
):
    dataset_table.insert(
        "",
        "end",
        values=(index, example, label)
    )


#3rd tab - how ai learns
tk.Label(
    learning_tab,
    text="How Does Surpervised Learning Work?",
    font=("Arial", 17, "bold"),
    bg=BACKGROUND,
    fg=NAVY
).pack(anchor="w", padx=18, pady=(18, 10))

learning_steps = [
    (
        "1. DATASET",
        "A collection of examples used to teach the computer."
    ),
    (
        "2. FEATURES",
        "CountVectorizer converts words into numerical features."
    ),
    (
        "3. LABELS",
        "Known categories attached to the training examples."
    ),
    (
        "4. TRAINING",
        "MultinomialNB learns statistical patterns from the "
        "features and their known labels."
    ),
    (
        "5. PREDICTION",
        "The trained model predicts a category for new text."
    )
]

for heading , description in learning_steps:
    step_card = tk.Frame(
        learning_tab,
        bg=WHITE,
        highlightbackground="#D7E4F0",
        highlightthickness=1
    )
    step_card.pack(fill="x", padx=18, pady=5)

    tk.Label(
        step_card,
        text=heading,
        font=("Arial", 11, "bold"),
        bg=WHITE,
        fg=TEAL
    ).pack(anchor="w", padx=12, pady=(9, 2))

    tk.Label(
        step_card,
        text=description,
        font=("Arial", 10),
        bg=WHITE,
        fg=TEXT,
        wraplength=850,
        justify="left"
    ).pack(anchor="w", padx=12, pady=(0, 9))

tk.Label(
    learning_tab,
    text=(
        "Remember: supervised learning uses examples with known "
        "answers. The model learns statistical patterns, but it "
        "does not understand or diagnose medical conditions."
    ),
    font=("Arial", 10, "bold"),
    bg=BLUE_LIGHT,
    fg="#1E3A8A",
    wraplength=850,
    justify="left",
    padx=12,
    pady=12
).pack(fill="x", padx=18, pady=12)













root.mainloop()