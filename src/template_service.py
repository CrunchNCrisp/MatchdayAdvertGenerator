from ics import Event
from jinja2 import Environment, FileSystemLoader
# from weasyprint import HTML
# from pdf2image import convert_from_path

# Sample event data (from webcal source)
events = [
    {"date": "2025-03-15", "title": "Meeting with John"},
    {"date": "2025-03-16", "title": "Project Deadline"},
    {"date": "2025-03-18", "title": "Conference Call"},
]

def fill_template_with_event_data(event: Event, template_file_name: str = "template.html"):

    # Load template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_file_name)

    # Render HTML with data
    html_content = template.render(event=event)

    # Save HTML to a file (optional)
    with open("output.html", "w") as f:
        f.write(html_content)

    # # Convert HTML to PDF
    # HTML(string=html_content).write_pdf("output.pdf")
    #
    # # Convert PDF to PNG
    # images = convert_from_path("output.pdf")
    # images[0].save("output.png", "PNG")

    print("PDF and PNG generated successfully!")