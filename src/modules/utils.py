
# truncate text
def truncate_text(text: str, max_length: int) -> str:
  if len(text) > max_length:
    return text[:max_length - 3] + "..."
  return text

# format date
def format_date(date: str) -> str:
  return date.strftime("%Y-%m-%d")