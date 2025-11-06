def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, person in enumerate(attendees, start=1):
        filled = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = person.get(key)
            filled = filled.replace(f"{{{key}}}", str(value) if value else "N/A")

        filename = f"output_{i}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(filled)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
