import time
import winsound
from pathlib import Path

def load_timers(config_path):
    """config.txt からタイマー時間を読み込む"""
    timers = []
    try:
        with open(config_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and line.isdigit():
                    timers.append(int(line))
    except FileNotFoundError:
        print(f"エラー: {config_path} が見つかりません")
        return None
    
    if not timers:
        print("エラー: config.txt にタイマー時間が設定されていません")
        return None
    
    return timers

def run_timer(seconds, timer_number, total_timers):
    """指定秒数のタイマーを実行"""
    print(f"\n--- タイマー {timer_number}/{total_timers}: {seconds} 秒 ---")
    
    for remaining in range(seconds, 0, -1):
        print(f"\r残り時間: {remaining:3d} 秒", end="", flush=True)
        time.sleep(1)
    
    print("\r✓ タイマー完了！    ")
    # タイマー終了時に音を鳴らす
    winsound.Beep(880, 500)  # 周波数1000Hz、500ミリ秒

def main():
    dir_path = Path(__file__).parent
    config_path = dir_path.parent / 'data' / 'config.txt'
    
    timers = load_timers(config_path)
    if timers is None:
        return
    
    print(f"設定されたタイマー: {timers}")
    print("タイマーを開始します...")
    print("（Ctrl+C で停止）\n")
    
    cycle = 1
    try:
        while True:
            for i, seconds in enumerate(timers, 1):
                print(f"\n【サイクル {cycle}】")
                run_timer(seconds, i, len(timers))
            cycle += 1
    except KeyboardInterrupt:
        print("\n\nタイマーを中断しました。")

if __name__ == "__main__":
    main()

