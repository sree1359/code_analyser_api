def chunk_code(code: str, max_chars: int = 2000) -> list[str]:
    """Chunk code by lines so each chunk is <= max_chars."""
    lines = code.splitlines(keepends=True)
    chunks, current, size = [], [], 0
    for line in lines:
        if size + len(line) > max_chars:
            chunks.append(''.join(current))
            current, size = [], 0
        current.append(line)
        size += len(line)
    if current:
        chunks.append(''.join(current))
    return chunks