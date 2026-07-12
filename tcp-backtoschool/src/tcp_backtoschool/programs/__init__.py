"""Program registry for tcp_backtoschool challenges."""

from dataclasses import dataclass
from importlib import import_module


@dataclass
class Program:
    """Represents a runnable challenge program."""

    id: int
    name: str
    description: str
    module: str

    def run(self) -> None:
        """Import and run the program."""
        mod = import_module(f".{self.module}", package=__name__)
        mod.run()


# Registry of all available programs
PROGRAMS: list[Program] = [
    Program(1, "Back to School", "TCP challenge: calculate square root and multiply", "back_to_school"),
    Program(2, "Program 02", "Placeholder program", "program_02"),
    Program(3, "Program 03", "Placeholder program", "program_03"),
    Program(4, "Program 04", "Placeholder program", "program_04"),
    Program(5, "Program 05", "Placeholder program", "program_05"),
    Program(6, "Program 06", "Placeholder program", "program_06"),
    Program(7, "Program 07", "Placeholder program", "program_07"),
    Program(8, "Program 08", "Placeholder program", "program_08"),
    Program(9, "Program 09", "Placeholder program", "program_09"),
    Program(10, "Program 10", "Placeholder program", "program_10"),
    Program(11, "Program 11", "Placeholder program", "program_11"),
    Program(12, "Program 12", "Placeholder program", "program_12"),
    Program(13, "Program 13", "Placeholder program", "program_13"),
    Program(14, "Program 14", "Placeholder program", "program_14"),
    Program(15, "Program 15", "Placeholder program", "program_15"),
    Program(16, "Program 16", "Placeholder program", "program_16"),
    Program(17, "Program 17", "Placeholder program", "program_17"),
    Program(18, "Program 18", "Placeholder program", "program_18"),
    Program(19, "Program 19", "Placeholder program", "program_19"),
    Program(20, "Program 20", "Placeholder program", "program_20"),
    Program(21, "Program 21", "Placeholder program", "program_21"),
    Program(22, "Program 22", "Placeholder program", "program_22"),
    Program(23, "Program 23", "Placeholder program", "program_23"),
    Program(24, "Program 24", "Placeholder program", "program_24"),
    Program(25, "Program 25", "Placeholder program", "program_25"),
    Program(26, "Program 26", "Placeholder program", "program_26"),
    Program(27, "Program 27", "Placeholder program", "program_27"),
    Program(28, "Program 28", "Placeholder program", "program_28"),
    Program(29, "Program 29", "Placeholder program", "program_29"),
    Program(30, "Program 30", "Placeholder program", "program_30"),
]


def get_program(program_id: int) -> Program | None:
    """Get a program by its ID (1-based)."""
    for program in PROGRAMS:
        if program.id == program_id:
            return program
    return None


def get_all_programs() -> list[Program]:
    """Get all registered programs."""
    return PROGRAMS
