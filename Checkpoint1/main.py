import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
class Homework:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed


class HomeworkList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def all_finished(self):
        # Lọc ra các bài tập chưa hoàn thành
        unfinished = [item.name for item in self.items if not item.completed]

        if unfinished:
            print("Các bài tập chưa hoàn thành:")
            for name in unfinished:
                print(f"- {name}")
        else:
            print("All finished")


# Tạo danh sách bài tập
homework_list = HomeworkList()

homework_list.add_item(Homework("Lập trình App Producer", 3, False))   # Cao - chưa hoàn thành
homework_list.add_item(Homework("Làm văn", 2, True))                   # Trung bình - đã hoàn thành
homework_list.add_item(Homework("Lập trình Gamemaker", 1, False))      # Thấp - chưa hoàn thành

# Kiểm tra trạng thái
homework_list.all_finished()