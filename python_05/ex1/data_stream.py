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
        super().__init__(stream_id)

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
        super().__init__(stream_id)

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
        super().__init__(stream_id)

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

            return f"Event analysis: {len(data_batch)} events, {errors_count} " +\
                "error detected" if errors_count <= 1 else "errors detected"

        except (ValueError, TypeError):
            return "ERROR processing data"


class StreamProcessor():
    def __init__(self) -> None:
        self.streams: List[DataStream] = []
        self.stream_data: Dict[str, List[Any]] = {}

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def add_stream_data(self, stream_id: str, data_batch: List[Any]) -> None:
        self.stream_data[stream_id] = data_batch

    def process_all(self) -> List[str]:
        results: List[str] = []
        for stream in self.streams:
            if stream.stream_id in self.stream_data:
                batch = self.stream_data[stream.stream_id]
                result = stream.process_batch(batch)
                results.append(result)
            else:
                results.append(f"ERROR: No data found for {stream.stream_id}")

        return results

    def display_results(self, results: List[str]) -> None:
        print("Batch 1 Results:")

        try:
            for i, stream in enumerate(self.streams):
                stream_type = stream.__class__.__name__.replace("Stream", "")
                result = results[i]

                if "Sensor" in result:
                    count = int(result.split()[2])
                    print(f"- {stream_type} data: {count} readings processed")
                elif "Transaction" in result:
                    count = int(result.split()[2])
                    print(f"- {stream_type} data: {count} operations processed")
                elif "Event" in result:
                    count = int(result.split()[2])
                    print(f"- {stream_type} data: {count} events processed")
                else:
                    print(f"ERROR: UNKNOWN STREAM TYPE")

        except Exception:
            print("Error processing data")

    def filter_streams(self, criteria: str) -> Dict[str, List[Any]]:
        filtered_results: Dict[str, List[Any]] = {}

        for stream in self.streams:
            if stream.stream_id in self.stream_data:
                batch = self.stream_data[stream.stream_id]
                filtered = stream.filter_data(batch, criteria)
                filtered_results[stream.stream_id] = filtered

        return filtered_results

    def display_filter_results(self, filtered_results: Dict[str, List[Any]],
                               criteria: str) -> None:
        print()
        print(f"Stream filtering active: {criteria.capitalize()} data only")
        print("Filtered results: ", end="")

        summaries: List[str] = []

        for stream in self.streams:
            stream_id: str = stream.stream_id
            filtered_items: List[Any] = filtered_results.get(stream_id, [])
            count = len(filtered_items)

            if count > 0:
                stream_type: str = stream.__class__.__name__.replace(
                    "Stream", "").lower()

                if "sensor" in stream_type:
                    summaries.append(f"{count} critical sensor alerts")
                elif "transaction" in stream_type:
                    summaries.append(f"{count} large transaction")
                elif "event" in stream_type:
                    summaries.append(f"{count} critical events")

        if summaries:
            print(", ".join(summaries))
        else:
            print("No items matched the filter criteria")

    def get_stats(self) -> Dict[str, Dict[str, Any]]:
        all_stats: Dict[str, Dict[str, Any]] = {}

        for stream in self.streams:
            stats = stream.get_stats()
            all_stats[stream.stream_id] = stats

        return all_stats

    def display_stats(self) -> None:
        all_stats: Dict[str, Dict[str, Any]] = self.get_stats()

        print("\n=== Stream Statistics ===")
        for stream_id, stats in all_stats.items():
            print(f"\nStream: {stream_id}")
            for key, value in stats.items():
                print(f"  {key.replace('_', ' ').title()}: {value}")


if __name__ == '__main__':
    sensor = SensorStream('SENSOR_001')
    sensor1 = SensorStream('SENSOR_002')
    transaction = TransactionStream("TRANS_001")
    transaction1 = TransactionStream("TRANS_002")
    event = EventStream('EVENT_001')

    batch_sensor: List[str] = ['temp:22.5', 'humidity:65', 'pressure:1013']
    batch_transaction: List[str] = ['buy:100', 'sell:150', 'buy:75']
    batch_event: List[str] = ['login', 'error', 'logout']

    processor = StreamProcessor()
    


    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
    print(f"Processing sensor batch: [", end='')
    print(*batch_sensor, sep=', ', end=']\n')
    print(sensor.process_batch(batch_sensor))
    print()

    print("Initializing Transaction Stream...")
    print(f"Stream ID: {transaction.stream_id}, Type: Financial Data")
    print(f"Processing transaction batch: [", end='')
    print(*batch_transaction, sep=', ', end=']\n')
    print(transaction.process_batch(batch_transaction))
    print()

    print("Initializing Event Stream...")
    print(f"Stream ID: {event.stream_id}, Type: System Events")
    print(f"Processing event batch: [", end='')
    print(*batch_event, sep=', ', end=']\n')
    print(event.process_batch(batch_event))
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()
    

    processor.add_stream(sensor1)
    processor.add_stream(transaction1)
    processor.add_stream(event)

    processor.add_stream_data("SENSOR_002",
                              ["temp:52.5", "pressure:2013"])
    processor.add_stream_data("TRANS_002", ["buy:1000", "sell:150", "buy:75", "sell:50"])
    processor.add_stream_data("EVENT_001", batch_event)
    
    results: List[str] = processor.process_all()
    processor.display_results(results)
    
    filtered: Dict[str, Any] = processor.filter_streams("high-priority")
    processor.display_filter_results(filtered, "high-priority")
    
    print()
    print("All streams processed successfully. Nexus throughput optimal.")
