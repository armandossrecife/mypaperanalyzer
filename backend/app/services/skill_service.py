from pathlib import Path
from app.core.config import settings

def load_skill1():
    path = Path(settings.SKILLS_DIR) / "skill1.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")

def load_skill2():
    path = Path(settings.SKILLS_DIR) / "skill2.md"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")

def load_all_skills():
    return {
        "skill1": load_skill1(),
        "skill2": load_skill2()
    }
