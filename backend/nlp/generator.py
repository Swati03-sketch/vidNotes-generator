def generate_notes(summaries: list):
    if not summaries:
        return "No notes generated."

    notes = []
    for s in summaries:
        # Split into sentences if no bullet exists
        if "•" in s:
            bullets = [b.strip() for b in s.split("•") if b.strip()]
        else:
            bullets = [sentence.strip() for sentence in s.split(". ") if sentence.strip()]
        
        for note in bullets:
            # Ignore placeholder sentences without skipping everything
            if "here are" in note.lower() and "bullet points" in note.lower():
                continue
            notes.append(note)

    # Remove duplicates but keep order
    seen = set()
    unique_notes = []
    for n in notes:
        if n not in seen:
            unique_notes.append(n)
            seen.add(n)

    # Add bullet points
    return "\n".join(f"• {n}" for n in unique_notes)
