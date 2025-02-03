def kill_count(counselors, jason):
    return [name for name, intel in counselors if intel < jason]
