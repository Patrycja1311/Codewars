def work_needed(project_minutes, free_lancers):
    remaining = project_minutes - sum(h * 60 + m for h, m in free_lancers)
    return "Easy Money!" if remaining <= 0 else f"I need to work {remaining // 60} hour(s) and {remaining % 60} minute(s)"
