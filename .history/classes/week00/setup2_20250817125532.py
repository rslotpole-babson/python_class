from fpdf import FPDF

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Babson Coding Environment Setup", ln=True, align="C")
pdf.ln(5)

# Font for body text
pdf.set_font("Arial", '', 12)

# Steps with inline images
steps = [
    "Log into your GitHub account.",
    "Open the Canvas assignment link and accept the assignment.",
    "You now have your own copy of the class repo called python-YOUR_GITHUB_USER_NAME.",
    "Go back to github.com, refresh, and click on your repo.",
    "Click Code -> Codespaces -> Create codespace on main.",
    "Open Settings: hamburger menu -> File -> Preferences -> Settings.",
    "Search for git.untrack, change MIXED to HIDDEN, then close settings.",
    ("Visual reference for Settings panel:", "vs_code_LHS.png"),
    "Click Extensions in the left sidebar, search 'Live Server', install by Ritwick Dey.",
    "In the terminal (once for the course) enter:\n    git remote add upstream https://github.com/rslotpole-babson/python_class.git",
    ("Commit message reference in VS Code:", "commit.png")
]

for i, step in enumerate(steps, 1):
    if isinstance(step, tuple):
        # Add image with caption
        caption, img_file = step
        pdf.multi_cell(0, 8, f"{caption}")
        pdf.image(img_file, w=100)  # smaller width
        pdf.ln(5)
    else:
        pdf.multi_cell(0, 8, f"Step {i}: {step}")
        pdf.ln(2)

# Additional explanation
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "What's Going On?", ln=True)
pdf.set_font("Arial", '', 12)
explanation = (
    "A repo is a repository that holds all your files. "
    "You created your own priv
