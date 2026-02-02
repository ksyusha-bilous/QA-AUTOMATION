from datetime import datetime


def analyze_heartbeat_log(input_file: str, output_file: str, key: str):
    filtered_lines = []

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            if key not in line:
                continue

            idx = line.find("Timestamp ")
            if idx == -1:
                continue

            time_str = line[idx + len("Timestamp ") : idx + len("Timestamp ") + 8]

            timestamp = datetime.strptime(time_str, "%H:%M:%S")
            filtered_lines.append((timestamp, line.strip()))

    with open(output_file, "w", encoding="utf-8") as log:
        for i in range(1, len(filtered_lines)):
            prev_time, _ = filtered_lines[i - 1]
            curr_time, _ = filtered_lines[i]

            diff = (prev_time - curr_time).total_seconds()

            if diff < 0:
                diff += 24 * 60 * 60

            if 31 < diff < 33:
                log.write(
                    f"WARNING: heartbeat {diff:.0f}s at {curr_time.strftime('%H:%M:%S')}\n"
                )
            elif diff >= 33:
                log.write(
                    f"ERROR: heartbeat {diff:.0f}s at {curr_time.strftime('%H:%M:%S')}\n"
                )
if __name__ == "__main__":
    input_file = "hblog.txt"  # твій вхідний лог
    output_file = "hb_test.log"  # файл для результату
    key = "TSTFEED0300|7E3E|0400"  # ключ потоку

    analyze_heartbeat_log(input_file, output_file, key)
    print(f"Аналіз завершено. Результат у файлі {output_file}")
