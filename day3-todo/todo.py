import argparse
import json
from pathlib import Path
from typing import List


TASKS_FILE = Path(__file__).resolve().parent / "tasks.json"


def load_tasks(file_path: Path = TASKS_FILE) -> List[str]:
    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return [str(task) for task in data]
    except json.JSONDecodeError:
        pass

    return []


def save_tasks(tasks: List[str], file_path: Path = TASKS_FILE) -> None:
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(task: str) -> None:
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {task}")


def remove_task(task_number: int) -> None:
    tasks = load_tasks()

    if task_number < 1 or task_number > len(tasks):
        print(
            f"Task number {task_number} does not exist. "
            f"Please choose a number between 1 and {len(tasks)}."
        )
        return

    removed = tasks.pop(task_number - 1)
    save_tasks(tasks)
    print(f"Removed task: {removed}")


def list_tasks() -> None:
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple CLI to-do application")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", nargs="+", help="Task text")

    remove_parser = subparsers.add_parser("remove", help="Remove task by number")
    remove_parser.add_argument("number", type=int, help="Task number to remove")

    subparsers.add_parser("list", help="List all tasks")
    return parser


def main() -> None:
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    if args.command == "add":
        add_task(" ".join(args.task).strip())
    elif args.command == "remove":
        remove_task(args.number)
    elif args.command == "list":
        list_tasks()


if __name__ == "__main__":
    main()