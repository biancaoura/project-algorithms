def study_schedule(permanence_period: list[tuple], target_time: int):
    count = 0
    try:
        for period in permanence_period:
            if (period[0] <= target_time <= period[1]):
                count += 1
        return count
    except TypeError:
        return None
