from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            sum1: int = sum(data)
            len1: int = len(data)
            avg: float = sum1 / len1
            return f"Processed {len1} numeric values, sum={sum1}, avg={avg}"

        except (ValueError, TypeError):
            return "Data provided of wrong type. Expected int!"

    def validate(self, data: Any) -> bool:
        if not data:
            return False

        for i in data:
            if not isinstance(i, int) and not isinstance(i, float):
                return False

        return True


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            len1: int = len(data)
            words: List[str] = data.split()
            return f"Processed text: {len1} characters, {len(words)} words"

        except (ValueError, TypeError):
            return "Data provided of wrong type. Expected String!"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if ':' not in data:
                raise TypeError
            level, message = data.split(':', 1)
            level: str = level.upper()
            message: str = message.strip()
            if level == 'ERROR':
                output_level = 'ALERT'
            else:
                output_level = level
            return f"[{output_level}] {level} level detected: {message}"

        except (ValueError, TypeError):
            return "Data provided of wrong format: 'LEVEL: MESSAGE'"

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or ':' not in data:
            return False

        return True


if __name__ == '__main__':
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()

    print("Initializing Numeric Processor...")
    numeric = NumericProcessor()
    nums: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {nums}")
    print("Validation: ", end="")
    print("Numeric data verified" if numeric.validate(nums)
          else "[ERROR] EXPECTED DATA OF TYPE INT")
    print(numeric.format_output(numeric.process(nums)))

    print()
    print("Initializing Text Processor...")
    text = TextProcessor()
    sample: str = "Hello Nexus World"
    print(f'Processing data: "{sample}"')
    print("Validation: ", end="")
    print("Text data verified" if text.validate(sample)
          else "[ERROR] EXPECTED DATA OF TYPE STRING")
    print(text.format_output(text.process(sample)))

    print()
    print("Initializing Log Processor...")
    log = LogProcessor()
    message: str = "ERROR: Connection timeout"
    print(f'Processing data: "{message}"')
    print("Validation: ", end='')
    print("Log entry verified" if log.validate(message)
          else "[ERROR] EXPECTED DATA OF FORMAT 'LEVEL: MESSAGE'")
    print(log.format_output(log.process(message)))

    print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    print("Result 1: ", end="")
    print(numeric.process([1, 2, 3]))
    print("Result 2: ", end="")
    print(text.process("Hello world"))
    print("Result 3: ", end="")
    print(log.process("info: System ready"))

    print()
    print("Foundation systems online. Nexus ready for advanced streams.")
