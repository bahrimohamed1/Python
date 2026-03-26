from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        
        return []

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_type": self.__class__.__name__,
            "Stream_id": self.stream_id
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "ERROR: Data_batch is empty!"
        default_sensors: List[str] = ['temp', 'humidity', 'pressure']
        try:
            sensor_type: List[str] = []
            sensor_value: List[int | float] = []
            sum_temp: float = 0
            count_temp: int = 0
            for item in data_batch:
                if not isinstance(item, str) or ':' not in item:
                    return f"ERROR: Invalid sensor reading format: {item}"
                type, value = item.split(':', 1)
                if type not in default_sensors:
                    return f"ERROR: {type} is not a sensor type"
                sensor_type.append(type)
                if type == 'temp':
                    count_temp += 1
                    sum_temp += float(value)
                    sensor_value.append(float(value))
                else:
                    sensor_value.append(int(value))
            avg_temp: float = sum_temp / count_temp

            return f"Sensor analysis: {len(data_batch)} readings processed, " +\
                f"avg temp: {avg_temp:.1f}°C"

        except (ValueError, TypeError, ZeroDivisionError):
            return "ERROR processing data"
        
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        
        filtered: List[Any] = []
        if criteria.lower() == 'high-priority':
            for item in data_batch:
                if 'temp' in item:
                    temp: float = float(item.split(':')[1])
                    if temp > 40 or temp < -10:
                        filtered.append(item)
                if 'pressure' in item:
                    pressure: int = int(item.split(':', 1)[1])
                    if pressure > 2000:
                        filtered.append(item)
            return filtered
        
        return []


class TransactionStream(DataStream):
    def __init__(self, stream_id) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "ERROR: Data batch is empty"
        ops: List[str] = ['buy', 'sell']
        total_units: int = 0
        try:
            for transaction in data_batch:
                if not isinstance(transaction, str) or ':' not in transaction:
                    return f"ERROR: {transaction} is of bad format"
                op, unit = transaction.split(':', 1)
                op: str = op.lower()
                if op not in ops:
                    return f"ERROR: Operation unknown: {op}"
                if int(unit) < 0:
                    return f"ERROR: Units can't be negative: {unit}"
                units: int = int(unit)
                if op == 'buy':
                    total_units += units
                else:
                    total_units -= units
            return f"Transaction analysis: {len(data_batch)} operations, net flow: " +\
                f"+{total_units} units" if total_units > 0 else f"-{total_units} units"

        except (ValueError, TypeError):
            return "ERROR processing data"
        
    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        
        filtered: List[str] = []
        if criteria.lower() == 'high-priority':
            for item in data_batch:
                op, value = item.split(':', 1)
                op: str = op.lower()
                value: int = int(value)
                if op in ['buy', 'sell']:
                    if value > 200:
                        filtered.append(item)
            return filtered
        
        return []
        


class EventStream(DataStream):
    def __init__(self, stream_id) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "ERROR: Data batch empty"
        errors_count: int = 0
        try:
            for event in data_batch:
                if not isinstance(event, str):
                    return f"ERROR: {event} is of wrong format"
                if event.lower() == 'error':
                    errors_count += 1

            return f"Event analysis: {len(data_batch)} events, {errors_count}"+\
                "error detedcted" if errors_count <= 1 else "errors detected"

        except (ValueError, TypeError):
            return "ERROR processing data"


class StreamProcessor():
    pass


if __name__ == '__main__':
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    print("Initializing Sensor Stream...")
    sensor = SensorStream('SENSOR_001')
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    batch_sensor: List[str] = ['temp:22.5', 'humidity:65', 'pressure:1013']
    print(f"Processing sensor batch: [", end='')
    print(*batch_sensor, sep=', ', end=']\n')
    print(sensor.process_batch(batch_sensor))
    print()

    print("Initializing Transaction Stream...")
    Transaction = TransactionStream("TRANS_001")
    print(f"Stream ID: {Transaction.stream_id}, Type: Financial Data")
    batch_transaction: List[str] = ['buy:100', 'sell:150', 'buy:75']
    print(f"Processing transaction batch: [", end='')
    print(*batch_transaction, sep=', ', end=']\n')
    print(Transaction.process_batch(batch_transaction))
    print()

    print("Initializing Event Stream...")
    Event = EventStream('EVENT_001')
    print(f"Stream ID: {Event.stream_id}, Type: System Events")
    batch_event: List[str] = ['login', 'error', 'logout']
    print(f"Processing event batch: [", end='')
    print(*batch_event, sep=', ', end=']\n')
    print(Event.process_batch(batch_event))
    print()
    
    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()
    
    print()
    print()
    print()
    print()
